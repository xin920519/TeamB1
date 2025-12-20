Function LocalAlignment
	Double p, deg, pos
	p = 3.14159265359
	deg = 0
   	
   	'revise
   	
    pos = Sin(deg * p / 180)
	P21 = XY(0, 0, 0, 0) /3
	P22 = XY(1, pos, 0, 0) /3
	P23 = XY(0, 1, 0, 0) /3
	Local 3, P21, P22, P23
	Go XY(30, 0, 1, 90, 180, 0) /3
Fend
Function CreateLocal
	Tool 1
	P31 = Here
	P32 = P31 +Y(50)
	P33 = P31 +X(-50)
	
	'revise
	Local 3, P31, P32, P33
Fend

