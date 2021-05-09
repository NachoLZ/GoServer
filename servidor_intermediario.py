import socket as skt
SERVERPORT = 55000
serverSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
serverSocket.bind(("",SERVERPORT))
serverSocket.listen()
print("Servidor TCP escuchando en: ",SERVERPORT)
condicion=True
numero_jugadas=0
while(condicion==True and numero_jugadas<=3):	
	clientsocket,clientaddr=serverSocket.accept()
	print("conectado con: "+ clientaddr[0])
	msg=clientsocket.recv(2048).decode()
	if(msg=="terminar"):
		condicion=False
		clientsocket.close()
		break;
	elif(msg=="disponible?"):
		respuesta="si" #Aqui verificar disponibilidad del servidor cachipun
		clientsocket.send(respuesta.encode())
	elif(msg=="papel"):
		respuesta="has jugado papel  y el bot ha jugado X"#Aqui poner la jugada del servidor cachipun, y enviar el resultado.
		clientsocket.send(respuesta.encode())
	elif(msg=="piedra"):
		respuesta=" has jugado piedra y etc"
		clientsocket.send(respuesta.encode())
	elif(msg=="tijera"):
		respuesta=" has jugado tijera y etc"
		clientsocket.send(respuesta.encode())
	else:
		respuesta=" Jugada no valida"
		clientsocket.send(respuesta.encode())

print("servidor cerrado")
serverSocket.close()