import socket as skt

SERVER = 'localhost'
PORT = 12000

clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

clientSocket.connect((SERVER, PORT))
terminate = False
while terminate == False:
    URL = input("URL: ")

    clientSocket.send(URL.encode()) #bytes
    response = clientSocket.recv(2048).decode().split("-")
    if response[0]=="OK":
        clientSocketUDP= skt.socket(skt.AF_INET,skt.SOCK_DGRAM)
        clientSocketUDP.sendto("OK".encode() ,(SERVER,int(response[1])))
        header,addr = clientSocketUDP.recvfrom(2048)

        with open('{0}.txt'.format(URL), 'w') as tequiste:  # el with cierra el archivo al terminar
            tequiste.write(header.decode())
        clientSocketUDP.close()
    else:
        print(response)
    
    if URL == "terminate":
        terminate = True
clientSocket.close()
