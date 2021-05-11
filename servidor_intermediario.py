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

puntajeCliente = 0
puntajeUDP = 0

while(condicion == True and puntajeCliente < 3 and puntajeUDP < 3):	

	clientsocket, clientaddr = serverSocket.accept()
	print("conectado con: "+ clientaddr[0])
	msg = clientsocket.recv(2048).decode()

	

	print(msg)

	if(msg == "terminar"):
		condicion=False
		clientsocket.close()
		break;

	elif(msg == "ready?" and flag == False):
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

	elif(flag == True):

		response = "jugada?" #respuesta a UDP
		udpSocket.sendto(response.encode(), (udpserverAddr, UDPPORT))
		udpmsg, addr = udpSocket.recvfrom(2048)
		udpmessage = udpmsg.decode()




		if(msg=="papel"):
			print("Cliente ha jugado papel y el bot ha jugado " + udpmessage) #Aqui poner la jugada del servidor cachipun, y enviar el resultado.

			if udpmessage == "Tijera":
				respuesta = "El bot ha ganado un punto."
				clientsocket.send(respuesta.encode())
				puntajeUDP+=1
			elif udpmessage == "Piedra":
				respuesta = "Has ganado un punto."
				clientsocket.send(respuesta.encode())
				puntajeCliente+=1
			else:
				respuesta = "Han empatado."
				clientsocket.send(respuesta.encode())
				continue

		elif(msg=="piedra"):
			print("Cliente ha jugado piedra y el bot ha jugado " + udpmessage) #Aqui poner la jugada del servidor cachipun, y enviar el resultado.

			if udpmessage == "Papel":
				respuesta = "El bot ha ganado un punto."
				clientsocket.send(respuesta.encode())
				puntajeUDP+=1
			elif udpmessage == "Tijera":
				respuesta = "Has ganado un punto."
				clientsocket.send(respuesta.encode())
				puntajeCliente+=1
			else:
				respuesta = "Han empatado."
				clientsocket.send(respuesta.encode())
				continue

		elif(msg=="tijera"):
			print("Cliente ha jugado tijera y el bot ha jugado " + udpmessage) #Aqui poner la jugada del servidor cachipun, y enviar el resultado.

			if udpmessage == "Piedra":
				respuesta = "El bot ha ganado un punto."
				clientsocket.send(respuesta.encode())
				puntajeUDP+=1
			elif udpmessage == "Papel":
				respuesta = "Has ganado un punto."
				clientsocket.send(respuesta.encode())
				puntajeCliente+=1
			else:
				respuesta = "Han empatado."
				clientsocket.send(respuesta.encode())
				continue
		
		else:
			respuesta = "Jugada no valida"
			clientsocket.send(respuesta.encode())


if puntajeCliente == 3:
	respuesta = "Has ganado la partida!"
	clientsocket.send(respuesta.encode())
elif puntajeUDP == 3:
	respuesta = "El Bot te ha derrotado!"
	clientsocket.send(respuesta.encode())


while(condicion == True):
	clientsocket, clientaddr = serverSocket.accept()
	msg = clientsocket.recv(2048).decode()
	if(msg == "terminar"):
		condicion = False
		clientsocket.close()
		break;

			

print("servidor cerrado")
serverSocket.close()