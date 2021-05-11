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
		response = "STOP" #respuesta a UDP
		udpSocket.sendto(response.encode(), (udpserverAddr, UDPPORT))
		condicion=False
		print("Servidor cerrado")
		clientsocket.close()
		serverSocket.close()
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
				puntajeUDP+=1
				if (puntajeCliente == 3 or puntajeUDP == 3):

					if puntajeCliente == 3:
						respuesta = "Has ganado la partida!"
						print(respuesta)
						clientsocket.send(respuesta.encode())
					elif puntajeUDP == 3:
						respuesta = "El Bot te ha derrotado!"
						print(respuesta)
						clientsocket.send(respuesta.encode())
					break	
				respuesta = "El bot ha ganado un punto: Has jugado Papel y el bot ha jugado " + udpmessage + "\nTu puntuación es: " + str(puntajeCliente) + " y la del Bot: " + str(puntajeUDP)
				clientsocket.send(respuesta.encode())
				
			elif udpmessage == "Piedra":
				puntajeCliente+=1
				if (puntajeCliente == 3 or puntajeUDP == 3):

					if puntajeCliente == 3:
						respuesta = "Has ganado la partida!"
						print(respuesta)
						clientsocket.send(respuesta.encode())
					elif puntajeUDP == 3:
						respuesta = "El Bot te ha derrotado!"
						print(respuesta)
						clientsocket.send(respuesta.encode())
					break	
				respuesta = "Has ganado un punto: Has jugado Papel y el bot ha jugado " + udpmessage + "\nTu puntuación es: " + str(puntajeCliente) + " y la del Bot: " + str(puntajeUDP)
				clientsocket.send(respuesta.encode())
				
			else:
				respuesta = "Han empatado."
				clientsocket.send(respuesta.encode())
				continue

		elif(msg=="piedra"):
			print("Cliente ha jugado piedra y el bot ha jugado " + udpmessage) #Aqui poner la jugada del servidor cachipun, y enviar el resultado.

			

			if udpmessage == "Papel":
				puntajeUDP+=1
				if (puntajeCliente == 3 or puntajeUDP == 3):

					if puntajeCliente == 3:
						respuesta = "Has ganado la partida!"
						print(respuesta)
						clientsocket.send(respuesta.encode())
					elif puntajeUDP == 3:
						respuesta = "El Bot te ha derrotado!"
						print(respuesta)
						clientsocket.send(respuesta.encode())
					break	

				respuesta = "El bot ha ganado un punto: Has jugado Piedra y el bot ha jugado " + udpmessage + "\nTu puntuación es: " + str(puntajeCliente) + " y la del Bot: " + str(puntajeUDP)
				clientsocket.send(respuesta.encode())

			elif udpmessage == "Tijera":
				puntajeCliente+=1
				if (puntajeCliente == 3 or puntajeUDP == 3):

					if puntajeCliente == 3:
						respuesta = "Has ganado la partida!"
						print(respuesta)
						clientsocket.send(respuesta.encode())
					elif puntajeUDP == 3:
						respuesta = "El Bot te ha derrotado!"
						print(respuesta)
						clientsocket.send(respuesta.encode())
					break	
				respuesta = "Has ganado un punto: Has jugado Piedra y el bot ha jugado " + udpmessage + "\nTu puntuación es: " + str(puntajeCliente) + " y la del Bot: " + str(puntajeUDP)
				clientsocket.send(respuesta.encode())
				
			else:
				respuesta = "Han empatado."
				clientsocket.send(respuesta.encode())
				continue

		elif(msg=="tijera"):
			print("Cliente ha jugado tijera y el bot ha jugado " + udpmessage) #Aqui poner la jugada del servidor cachipun, y enviar el resultado.



			if udpmessage == "Piedra":
				puntajeUDP+=1
				if (puntajeCliente == 3 or puntajeUDP == 3):

					if puntajeCliente == 3:
						respuesta = "Has ganado la partida!"
						print(respuesta)
						clientsocket.send(respuesta.encode())
					elif puntajeUDP == 3:
						respuesta = "El Bot te ha derrotado!"
						print(respuesta)
						clientsocket.send(respuesta.encode())
					break	
				respuesta = "El bot ha ganado un punto: Has jugado Tijera y el bot ha jugado " + udpmessage + "\nTu puntuación es: " + str(puntajeCliente) + " y la del Bot: " + str(puntajeUDP)
				clientsocket.send(respuesta.encode())
				
			elif udpmessage == "Papel":
				puntajeCliente+=1
				if (puntajeCliente == 3 or puntajeUDP == 3):

					if puntajeCliente == 3:
						respuesta = "Has ganado la partida!"
						print(respuesta)
						clientsocket.send(respuesta.encode())
					elif puntajeUDP == 3:
						respuesta = "El Bot te ha derrotado!"
						print(respuesta)
						clientsocket.send(respuesta.encode())
					break	
				respuesta = "Has ganado un punto: Has jugado Tijera y el bot ha jugado " + udpmessage + "\nTu puntuación es: " + str(puntajeCliente) + " y la del Bot: " + str(puntajeUDP)
				clientsocket.send(respuesta.encode())
				
			else:
				respuesta = "Han empatado."
				clientsocket.send(respuesta.encode())
				continue
		
		else:
			respuesta = "Jugada no valida"
			clientsocket.send(respuesta.encode())

response = "STOP" #respuesta a UDP
udpSocket.sendto(response.encode(), (udpserverAddr, UDPPORT))

msg = clientsocket.recv(2048).decode()
if(msg == "terminar"):
	condicion = False
	clientsocket.close()
	print("Cerrando servidor...")
	serverSocket.close()


print("servidor cerrado")
serverSocket.close()