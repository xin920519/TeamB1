# **Task 3**

## **Obstacle Avoidance Using Deep Learning**

This project adopts a deep learning–based approach to train an Autonomous Mobile Robot (AMR) for path following and obstacle contour recognition.
The trained model performs obstacle avoidance prediction based on visual input captured by the onboard camera.

When the obstacle detection confidence in the camera image and the trained model accuracy reach a threshold of 0.75, the system automatically triggers the obstacle avoidance decision-making process.

You can download the [Trained model](https://drive.google.com/drive/folders/1yhmVA8Zezx7skUu_QirdOwhPgkMbPpi8?usp=drive_link).

**1.** `best_steering_modev4.pth` : The trained model is mainly de

**2.** `best_model_coll.pth` : In this model, the classes **“free”** and **“blocked”** are trained to identify whether there is an obstacle on the road ahead.

<img width="491" height="498" alt="image" src="https://github.com/user-attachments/assets/ab1371ea-d177-4330-aad4-a0187c41fa25" />
<img width="491" height="498" alt="image1" src="https://github.com/user-attachments/assets/7b150d23-406b-4977-9063-f97fbc2a4d5e" />
