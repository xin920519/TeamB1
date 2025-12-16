#model:https://drive.google.com/drive/folders/1yhmVA8Zezx7skUu_QirdOwhPgkMbPpi8?usp=drive_link
import torch
import torchvision.models as models
import torchvision.transforms as transforms
import torch.nn.functional as F
import cv2
import numpy as np
import time

from jetbot import Robot, Camera

# ============================================================
#               1. 讀取模型
# ============================================================

device = torch.device('cuda')

### (A) 路徑追蹤模型 (XY regression) -------------------------
steer_model = models.resnet18(pretrained=False)
steer_model.fc = torch.nn.Linear(512, 2)
steer_model.load_state_dict(torch.load("best_steering_model_xy_v4.pth"))
steer_model = steer_model.to(device)
steer_model.eval()

### (B) 避障模型 (分類 free / blocked) ------------------------
coll_model = models.alexnet(pretrained=False)
coll_model.classifier[6] = torch.nn.Linear(coll_model.classifier[6].in_features, 2)
coll_model.load_state_dict(torch.load("best_model_coll.pth"))
coll_model = coll_model.to(device)
coll_model.eval()

# ============================================================
#               2. 建立 Camera 與 Robot
# ============================================================

robot = Robot()
camera = Camera.instance(width=224, height=224)

# ============================================================
#               3. 前處理 function（兩模型共用）
# ============================================================

mean = np.array([0.485, 0.456, 0.406])
std = np.array([0.229, 0.224, 0.225])
normalize = transforms.Normalize(mean, std)


def preprocess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.transpose((2, 0, 1))
    img = torch.from_numpy(img).float() / 255.0
    img = normalize(img)
    return img[None, ...].to(device)


# ============================================================
#               4. 主控制迴圈
# ============================================================

# 手動可調參數
speed = 0.16
steer_gain = 0.18
bias = 0.00  # 如果右輪較弱，可 +0.01 ~ +0.03

try:
    while True:

        frame = camera.value
        x = preprocess(frame)

        # ---------- 避障判斷 ----------
        y_coll = coll_model(x)
        y_coll = F.softmax(y_coll, dim=1)
        prob_blocked = float(y_coll.flatten()[0])

        if prob_blocked > 0.75:
            print("🚫 遇到障礙物 → 左轉中...")
            # 遇到障礙物左轉
            robot.left(0.12)
            time.sleep(0.8)
            robot.forward(0.12)
            time.sleep(0.8)
            # 轉正到原本的直行方向
            robot.right(0.12)
            time.sleep(0.8)
            robot.forward(0.1)
            time.sleep(1.7)
            # 回到道路
            robot.right(0.1)
            time.sleep(0.7)
            robot.forward(0.1)
            time.sleep(1.7)
            # 轉正成道路直線
            robot.left(0.1)
            time.sleep(0.3)

            continue

        # ---------- 路徑追蹤 ----------
        xy = steer_model(x).detach().cpu().numpy().flatten()
        steer = float(xy[0])

        left = speed + steer * steer_gain
        right = speed - steer * steer_gain

        left += -bias  # 可手動調整偏移
        right += +bias

        robot.set_motors(left, right)

        time.sleep(0.02)

except KeyboardInterrupt:
    robot.stop()
    camera.stop()

print("done")

