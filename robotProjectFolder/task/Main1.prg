Integer u, v, w
Function Main1
	Integer i, scale
	String list$(20)
	String gui_list$
	Do
		If Sw(0) = 1 Then
			TmReset 0
			Print 'starting'
			'use default stack
			If useGUI_stack = False Then
				For i = 0 To 19
					If (i Mod 2) = 1 Then
						list$(i) = "Block"
					Else
						list$(i) = "Token"
					EndIf
					Print list$(i), i
				Next
			'stack by gui list
			Else
				For i = 0 To 19
					GGet GUI_Task2.append_list.List(i), gui_list$
					list$(i) = gui_list$
					Print list$(i), i
				Next
			EndIf
			
			scale = 1
			Motor On
			Power High
			Speed 30 / scale
			Accel 30 / scale, 30 / scale
			SpeedS 500 / scale
			AccelS 5000 / scale
			Exit Do
		EndIf
	Loop
	
	Double x, y, obj_h
	String type$
	Integer read_i, Token_i, Block_i
	
	obj_h = 6.0
	Token_i = 10
	Block_i = 10
	u = 90
	v = 180
	w = 0
	
	Go XY(31, 24, 130, u, v, w) /1
	For read_i = 0 To 19
		Move XY(31, 24, 100, u, v, w) /1
		type$ = list$(read_i)
		Print read_i, type$
		If type$ = "Token" Then
			'tune--------
			x = 45
			y = 27
			'tune--------
			Move XY(x, y, (Token_i * obj_h - 6), u, v, w) /1
			Token_i = Token_i - 1
			Call pick_stack
		ElseIf type$ = "Block" Then
			'tune--------
			x = 20
			y = 20
			'tune--------
			Move XY(x, y, (Block_i * obj_h - 6), u, v, w) /1
			Block_i = Block_i - 1
			Call pick_stack
        Else
			Print("Unknown type")
			Go XY(31, 24, 130, u, v, w) /1
			Exit Function
		EndIf
		Move XY(x, y + 2, 150, u, v, w) /1
		Move XY(38, 30, 175, u, v, w) /3
		Move XY(38, 30, (read_i * 6 + 0), u, v, w) /3
		Wait 0.5
		Off 8
		Wait 0.5
		Move XY(31, 35, 175, u, v, w) /3
	Next read_i
	Print "Finish stack"
	Go XY(31, 24, 130, u, v, w) /1
	Home
	Print Tmr(0)
Fend
Function pick_stack
	CP Off
	TMove XY(0, 0, 1, 0)
	Wait 1
	On 8
	Wait .5
	TMove XY(0, 0, -1, 0)
	CP On
Fend
