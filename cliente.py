import socket as skt

SERVER = 'localhost'
PORT = 55000
#clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
#clientSocket.connect((SERVER, PORT))
terminate = False
clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
clientSocket.connect((SERVER, PORT))
mensaje=input("Pregunte por disponibilidad, escribiendo: 'ready?'\n")
clientSocket.send(mensaje.encode())
if(mensaje=="terminar"):
	clientSocket.send(mensaje.encode())
	clientSocket.close()
	print("Conexion terminada")
respuesta=clientSocket.recv(2048).decode()
print(respuesta+"\n")
if(respuesta=="OK"):
	while(terminate==False):
		clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
		clientSocket.connect((SERVER, PORT))
		jugada=input("Ingrese su jugada: \n")
		if(jugada=="terminar"):
			clientSocket.send(jugada.encode())
			print("Conexion terminada")
			break
		clientSocket.send(jugada.encode())

		resultadojugada=clientSocket.recv(2048).decode()

		if(resultadojugada=="Has ganado la partida!" or resultadojugada=="El Bot te ha derrotado!"):
			print("Servidor: "+ resultadojugada)
			print("Juego ha terminado")
			mensajeT="terminar"
			clientSocket.send(mensajeT.encode())
			clientSocket.close()
			print("Se ha cerrado el juego")
			break
		print("Servidor: "+ resultadojugada)	

elif(respuesta=="NO"):
	print("Servidor cachipun no disponible")
	print("Ejecute nuevamente el programa")
	jugada="terminar"
	clientSocket.send(jugada.encode())
	clientSocket.close()
