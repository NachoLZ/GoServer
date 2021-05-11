import socket as skt

SERVERPORT = 55000
UDPPORT = 50001
udpSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
udpSocket.bind(('', SERVERPORT))
serverSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
serverSocket.bind(("",SERVERPORT))
serverSocket.listen()
print("Servidor TCP escuchando en: ", SERVERPORT)
print("Servidor UDP escuchando en: ", UDPPORT)
condicion=True
numero_jugadas=0

while(condicion == True and numero_jugadas <= 3):	

	clientsocket, clientaddr = serverSocket.accept()
	print("conectado con: "+ clientaddr[0])
	msg = clientsocket.recv(2048).decode()

	udpmsg, udpclientAddr = udpSocket.recvfrom(2048)
	udpmessage = udpmsg.decode()
	print("Se recibe desde UDP: ", udpmessage)
	response = "" #respuesta a UDP
	udpSocket.sendto(response.encode(), udpclientAddr)



	if(msg=="terminar"):
		condicion=False
		clientsocket.close()
		break;
	elif(msg=="ready?"):
		respuesta="OK" #Aqui verificar disponibilidad del servidor cachipun
		clientsocket.send(respuesta.encode())
	elif(msg=="Papel"):
		respuesta="has jugado papel  y el bot ha jugado X"#Aqui poner la jugada del servidor cachipun, y enviar el resultado.
		clientsocket.send(respuesta.encode())
	elif(msg=="Piedra"):
		respuesta=" has jugado piedra y etc"
		clientsocket.send(respuesta.encode())
	elif(msg=="Tijera"):
		respuesta=" has jugado tijera y etc"
		clientsocket.send(respuesta.encode())
	else:
		respuesta=" Jugada no valida"
		clientsocket.send(respuesta.encode())

print("servidor cerrado")
serverSocket.close()