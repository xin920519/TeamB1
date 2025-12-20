Integer append_i
Integer limit_t
Integer limit_b
Global Boolean useGUI_stack
Function GUI_Task2_Load(Sender$ As String)
	append_i = 0
	limit_t = 1
	limit_b = 1
	Integer init
	Double scale
	
	scale = 1
	Motor On
	Power High
	Speed 30 / scale
	Accel 30 / scale, 30 / scale
	SpeedS 500 / scale
	AccelS 5000 / scale
	Tool 1
	
	For init = 0 To 19
		GSet GUI_Task2.append_list.AddItem, "-1"
	Next init
Fend

Function GUI_Task2_Token_Click(Sender$ As String)
	'append Token to gui list until limit(10)
	String check$
	If limit_t <= 10 Then
		GSet GUI_Task2.append_list.List(append_i), "Token"
		
		Do
			GGet GUI_Task2.append_list.List(append_i), check$
			If check$ = "Token" Then
				GSet GUI_Task2.Token.Enabled, False
				GSet GUI_Task2.Block.Enabled, False
				Exit Do
			EndIf
		Loop
		GSet GUI_Task2.Token.Enabled, True
		GSet GUI_Task2.Block.Enabled, True
		append_i = append_i + 1
		limit_t = limit_t + 1

	Else
		Print "Token is limit"
	EndIf
	
	If append_i = 20 Then
		Print "starting stack"
		useGUI_stack = True
		Call Main1
	EndIf
Fend

Function GUI_Task2_Block_Click(Sender$ As String)
	'append Block to gui list until limit(10)
	String check$
	If limit_b <= 10 Then
		GSet GUI_Task2.append_list.List(append_i), "Block"
		
		Do
			GGet GUI_Task2.append_list.List(append_i), check$
			If check$ = "Block" Then
				GSet GUI_Task2.Token.Enabled, False
				GSet GUI_Task2.Block.Enabled, False
				Exit Do
			EndIf
		Loop
		GSet GUI_Task2.Token.Enabled, True
		GSet GUI_Task2.Block.Enabled, True
		append_i = append_i + 1
		Print append_i
		limit_b = limit_b + 1
		Wait 0.5
	Else
		Print "Token is limit"
	EndIf

	If append_i = 20 Then
		Print "starting stack"
		useGUI_stack = True
		Call Main1
	EndIf
Fend
Function GUI_Task2_Closed(Sender$ As String)
	Home
Fend

Function GUI_Task2_Run_Default_Click(Sender$ As String)
	useGUI_stack = False
	Call Main1
Fend

