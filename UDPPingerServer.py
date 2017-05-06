# import socket functionality
from socket import *

# port to listen on
serverPort = 12000

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)


# FIXME - for the first parameter of bind, include the ip address of your local machine
# Assign IP address and port number to socket
serverSocket.bind(('', serverPort))

while True:
    # receive bytes from the port that we're listening on
    message, address = serverSocket.recvfrom(1024)

    # print the message
    print('message : ', message, ' from address : ', address)

    # respond to the client as the server
    serverSocket.sendto(message, address)
