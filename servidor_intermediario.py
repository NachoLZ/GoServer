import socket as skt
import _thread



def run_request(URL):
    header ='0'
    path = ''

    request_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    request_socket.settimeout(10)
    
    URL = URL.split("/", 1)
    host = URL[0]
    try:
        host_ip = skt.gethostbyname(host)
    except skt.gaierror:
        print("no existe el URL")
        return "0",0
    if len(URL)>1:
        path = URL[1]

    request = 'GET /{0} HTTP/1.1\r\nHost:{1}\r\n\r\n'.format(path, host)
    try:
        request_socket.connect((host_ip, 80))
        request_socket.send(request.encode())
        rec = request_socket.recv(4096).decode() #se pasa a string para sacar el header
        header = rec.split('\r\n\r\n')[0]
        header = header.encode()# de vuelta a bits
    except skt.error:
        print("Error. No se pudo conectar a URL")
        return "0", 0
    
    return header, 1

#def check_cache(URL):

def check_cache(cache, url): #recibe 2 strings.
    is_in = 0
    for registro in cache:
        if url == registro["url"]:
            is_in = 1
            registro["rank"] = registro["rank"] + 1
            index = registro["index"]        
    if is_in == 1:
        archivo = open("{0}.txt".format(index),"r") 
        contenido = archivo.read()
        update(cache)
        archivo.close()
        return cache , contenido.encode()
    else: 
        return cache, 0
            
def write_cache(cache, header, url): #recibe strings
    ocupados= []
    for reg in cache:#se buscan indices ocupados
        if reg["url"] != "":
            ocupados.append(reg["index"])
        
    desocupados = list(set(range(1,6))-set(ocupados)) #se encuentran los desocupados

    if len(desocupados)>0:
        index = desocupados[0]
        for i in cache:
            if i["index"] == index:
                i["url"] = url
    else:
        minimo = float("inf")
        for registro in cache:
            if registro["rank"] < minimo:
                minimo = registro["rank"]
                reemplazar = registro
        index = reemplazar["index"]
        reemplazar["url"] = url
        reemplazar["rank"] = 0

    cache = update(cache)
    with open("{0}.txt".format(str(index)),"w") as tequiste:
        tequiste.write(header)
    return cache
            
def update(cache):
    archivo_cache = open("lista_cache.txt","w") #update al txt del cache
    for registro in cache:
        archivo_cache.write("{0} {1} {2}\n".format(registro["url"],registro["index"],registro["rank"]))
    
    archivo_cache.close()
    return cache

def cliente_nuevo(newport, connectionSocket, addr, lista_cache):
    print("Conexion entrante de: "+str(addr))
    terminate = False
    while terminate == False:
        URL = connectionSocket.recv(2048)
        URL = URL.decode()
        print(URL)
        lista_cache, cache_lookup = check_cache(lista_cache,URL) #revisa cache
        if cache_lookup != 0:
            header,success = cache_lookup,1
        else:
            header,success = run_request(URL)
        if success == 1: #Success!
            serverSocketUDP=skt.socket(skt.AF_INET, skt.SOCK_DGRAM)  #puerto UDP

            OK_puerto= "OK-"+str(newport)
            serverSocketUDP.bind(('',newport))
            connectionSocket.send(OK_puerto.encode()) #Manda OK-n_puerto
            respuesta, direccion = serverSocketUDP.recvfrom(2048) #recibe OK
            print(respuesta)
            serverSocketUDP.sendto(header, direccion) #manda el header
            serverSocketUDP.close()
            if cache_lookup == 0:
                lista_cache = write_cache(lista_cache, header.decode(), URL)
        else:
            sentence = "ERR-0"
            connectionSocket.send(sentence.encode())
        if URL == "terminate":
            terminate = True
            connectionSocket.close()

fopen = open("lista_cache.txt","r")
LISTA_CACHE = []
for linea in fopen:
    linea_strip = linea.strip()
    url_cache, index,rank = linea_strip.split(" ")
    LISTA_CACHE.append({"url":url_cache,"index": int(index), "rank":int(rank)})
fopen.close()
n=1
while len(LISTA_CACHE)<5:
    LISTA_CACHE.append({"url":"","index": n, "rank":0})
    n+=1
NEWPORT=12002   #Puerto Z entregado por url
SERVERPORT = 12000
serverSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
serverSocket.bind(("",SERVERPORT))
serverSocket.listen()
print("Listo para recibir conexiones")

while True:
    CONNECTION_SOCKET, ADDR = serverSocket.accept()
    _thread.start_new_thread(cliente_nuevo, (NEWPORT, CONNECTION_SOCKET, ADDR, LISTA_CACHE))
serverSocket.close() 
