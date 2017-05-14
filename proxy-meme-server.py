import socket
import time

server_port = 12000
self_ip = '35.162.138.16'


serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind((self_ip, server_port))

# let's receive data from the above port
while True:
    message, address = serverSocket.recvfrom(1024)

    message = message.decode('utf-8')

    address = address.decode('utf-8')

    print(message, address)
