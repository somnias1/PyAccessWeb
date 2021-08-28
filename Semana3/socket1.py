import socket

#Crea el socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Prepara comunicación HTTP
mysock.connect(('data.pr4e.org', 80))
#Petición
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#Petición enviada
mysock.send(cmd)

while True:
    #Se recibirán 512 caracteres cada petición
    data = mysock.recv(512)
    #Si es el fin del documento, finalice petición
    if len(data) < 1:
        break
    #Información recibida
    print(data.decode(),end='')

#Finaliza la conexión
mysock.close()