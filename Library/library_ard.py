import ardDriver as driver
import time

def conexion_ard():
	s= driver.conexion_ard()
	if (s==-1):
		return s
	else:
		mensaje2= formarMensaje(False, 137, 80, 80)
		driver.enviar_msj(mensaje2)
		return 0
#X, Y (int)
def touch_xy(X, Y):
	tupla= mapearCoords(X,Y, True)
	X_n= tupla[0] #right
	Y_n= tupla[1] #bottom
	Z_n= tupla[2] #left
	mensaje= formarMensaje(True, X_n, Y_n, Z_n)
	mensaje2= formarMensaje(False, 137, 80, 80)
	driver.enviar_msj(mensaje)
	driver.enviar_msj(mensaje2)

#tipoT: A, B, C y numero (int)
def touch_num(tipoT, numero):
	tupla= coordenadasNumero(tipoT, numero, True)
	X_n= tupla[0] #right
	Y_n= tupla[1] #bottom
	Z_n= tupla[2] #left
	mensaje= formarMensaje(True, X_n, Y_n, Z_n)
	mensaje2= formarMensaje(False, 137, 80, 80)
	driver.enviar_msj(mensaje)
	driver.enviar_msj(mensaje2)

#tipoT: A, B, C, (string), X, Y (int), tiempo en segundos (int).
def push_xy(X, Y, tiempo):
	tupla= mapearCoords(X,Y, True)
	X_n= tupla[0] #right
	Y_n= tupla[1] #bottom
	Z_n= tupla[2] #left
	mensaje= formarMensaje(True, X_n, Y_n, Z_n)
	driver.enviar_msj(mensaje)
	if tiempo<3:
		tiempo=0
	else:
		tiempo=tiempo-3
	time.sleep(tiempo)
	mensaje= formarMensaje(False, 137, 80, 80)
	driver.enviar_msj(mensaje)

#tipoT: A, B, C, (string), numero (int), tiempo en segundos (int).
def push_num(tipoT, numero, tiempo):
	tupla= coordenadasNumero(tipoT, numero, True)
	X_n= tupla[0] #right
	Y_n= tupla[1] #bottom
	Z_n= tupla[2] #left
	mensaje= formarMensaje(True, X_n, Y_n, Z_n)
	driver.enviar_msj(mensaje)
	if tiempo<3:
		tiempo=0
	else:
		tiempo=tiempo-3
	time.sleep(tiempo)
	mensaje= formarMensaje(False, 137, 80, 80)
	driver.enviar_msj(mensaje)

#X, Y (pos inicial)(int), repeats (cant repeticiones)(int)
def drag_xy(X,Y, repeats):
	tupla= mapearCoords(X,Y, True)
	X_n= tupla[0] #right
	Y_n= tupla[1] #bottom
	Z_n= tupla[2] #left
	mensaje1= formarMensaje(True, X_n, Y_n, Z_n)
	mensaje2= formarMensaje(True, 125, 65, 70)
	mensaje3= formarMensaje(False, 137, 80, 80)
	for i in range(repeats):
		driver.enviar_msj(mensaje1)
		time.sleep(3)
		driver.enviar_msj(mensaje2)
	driver.enviar_msj(mensaje3)

#X, Y (pos inicial)(int), repeats (cant repeticiones)(int)
def drag_num(tipoT, numero, repeats):
	tupla= coordenadasNumero(tipoT, numero, True)
	X_n= tupla[0] #right
	Y_n= tupla[1] #bottom
	Z_n= tupla[2] #left
	tupla2= coordenadasNumero(tipoT, 0, True)
	X_n2= tupla2[0] #right2
	Y_n2= tupla2[1] #bottom2
	Z_n2= tupla2[2] #left
	mensaje1= formarMensaje(True, X_n, Y_n, Z_n)
	mensaje2= formarMensaje(True, X_n2, Y_n2, Z_n2)
	mensaje3= formarMensaje(False, 137, 80, 80)
	for i in range(repeats):
		driver.enviar_msj(mensaje1)
		driver.enviar_msj(mensaje2)
	driver.enviar_msj(mensaje3)

def mapearCoords(X,Y, tocar):
	bottom=102-X #X puede ser numero de entre 0 y 42
	right= 147-Y #Y puede ser numero de entre 0 y 22
	left=0	
	if (tocar):
		left=70
 	else:
		left=80
	if (bottom<60):
		bottom=102
	if (right<125):
		right=147
	return (right, bottom, left)

def coordenadasNumero(tipoT, numero, tocar):
 right=0 #igual a Y (+:arriba cel)
 bottom=0 #igual a X (+:izquierda cel)
 left= 0 #igual a eje Z (+:arriba)
 if (tocar):
	left=70
 else:
	left=80
 if(tipoT == "A"):
	if (numero==0):
		right=135
		bottom=65
      	elif (numero==1):
		right=141
		bottom=102
		if (tocar):
			left=72
	elif (numero==2):
		right=144
		bottom=80
	elif (numero==3):
		right=143
		bottom=60
	elif (numero==4):
		right=138
		bottom=98
		if (tocar):
			left=71
	elif (numero==5):
		right=140
		bottom=80
	elif (numero==6):
		right=139
		bottom=65
	elif (numero==7):
		right=132
		bottom=102
		if (tocar):
			left=68
	elif (numero==8):
		right=135
		bottom=88
	elif (numero==9):
		right=135
		bottom=76
		if (tocar):
			left=70
 elif(tipoT == "B"):
	if (numero==0):
		right=126
		bottom=68
		if (tocar):
			left=68
      	elif (numero==1):
		right=140
		bottom=100
		if (tocar):
			left=71
	elif (numero==2):
		right=143
		bottom=80
	elif (numero==3):
		right=143
		bottom=60
	elif (numero==4):
		right=133
		bottom=99
		if (tocar):
			left=70
	elif (numero==5):
		right=135
		bottom=80
	elif (numero==6):
		right=135
		bottom=65
	elif (numero==7):
		right=125
		bottom=101
		if (tocar):
			left=65
	elif (numero==8):
		right=126
		bottom=90
		if (tocar):
			left=68
	elif (numero==9):
		right=128
		bottom=79
		if (tocar):
			left=66
 elif(tipoT == "C"):
	if (numero==0):
		right=124
		bottom=68
		if (tocar):
			left=65
      	elif (numero==1):
		right=139
		bottom=102
		if (tocar):
			left=72
	elif (numero==2):
		right=142
		bottom=80
	elif (numero==3):
		right=142
		bottom=61
	elif (numero==4):
		right=131
		bottom=96
		if (tocar):
			left=69
	elif (numero==5):
		right=134
		bottom=80
		if (tocar):
			left=66
	elif (numero==6):
		right=133
		bottom=66
		if (tocar):
			left=71
	elif (numero==7):
		right=123
		bottom=96
		if (tocar):
			left=65
	elif (numero==8):
		right=125
		bottom=86
		if (tocar):
			left=66
	elif (numero==9):
		right=124
		bottom=75
		if (tocar):
			left=65
 return (right, bottom, left)

def formarMensaje(tocar, X, Y, Z):
	mensaje=""
	x_str= str(X)
	y_str= str(Y)
	z_str= str(Z)
	while(len(x_str)<3):
		x_str="0"+x_str
	while(len(y_str)<3):
		y_str="0"+y_str
	while(len(y_str)<2):
		y_str="0"+y_str
	if (tocar):
		mensaje = "TX"+x_str+"Y"+y_str+"Z"+z_str
	else:
		mensaje = "FX"+x_str+"Y"+y_str+"Z"+z_str
	return mensaje

def ejecutarInst(lista):
	for i in range (len(lista)):
		inst= lista[i]
		if (inst=="TOUCHXY"):
			X= lista[i+1]
			Y= lista[i+2]
			touch_xy(X,Y)
			i=i+2
		if (inst=="TOUCHN"):
			tipoT= lista[i+1]
			numero= lista[i+2]
			touch_num(tipoT,numero)
			i=i+2
		elif (inst=="PUSH"):
			tiempo= lista[i+1]
			push_xy(21, 11, tiempo)
			i=i+1
		elif (inst=="DRAG"):
			X= lista[i+1]
			Y= lista[i+2]
			repeats= lista[i+3]
			drag_xy(X, Y, repeats)
			i=i+3
