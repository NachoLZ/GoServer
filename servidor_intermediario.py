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
flag = False
udpserverAddr = 'localhost'

while(condicion == True and numero_jugadas <= 3):	

	clientsocket, clientaddr = serverSocket.accept()
	print("conectado con: "+ clientaddr[0])
	msg = clientsocket.recv(2048).decode()

	

	print(msg)

	if(msg == "terminar"):
		condicion=False
		clientsocket.close()
		break;

	elif(msg == "ready?"):
		#udpSocket.send(msg.enconde())

		response = "ready?" #respuesta a UDP
		udpSocket.sendto(response.encode(), (udpserverAddr, UDPPORT))
		udpmsg, addr = udpSocket.recvfrom(2048)
		udpmessage = udpmsg.decode()
		print("Se recibe desde UDP: ", udpmessage)


		if udpmessage == "OK":
			clientsocket.send(udpmessage.encode())
			flag = True
		else:
			clientsocket.send(udpmessage.encode())
			flag = False



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