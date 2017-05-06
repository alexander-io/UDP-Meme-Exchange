# import socket functionality
from socket import *
import subprocess as sub
import time
import os, sys
# port to listen on
serverPort = 12000
self_ip = '10.150.26.221'


time_between_memes = 15

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)


# FIXME - for the first parameter of bind, include the ip address of your local machine
# Assign IP address and port number to socket
serverSocket.bind((self_ip, serverPort))


got_meme = 0

while True:
    # receive bytes from the port that we're listening on
    message, address = serverSocket.recvfrom(1024)

    message = message.decode('utf-8')

    x = None
    url = None

    if 'meme' in message:
        x = message.split('@')
        url = x[1]
        print(x)


    # print the message
    print('message : ', message, ' from address : ', address)

    sub.run(["firefox", url])
    got_meme = 1

    if got_meme:
        time.sleep(time_between_memes)
        got_meme=0

    # os.system("firefox " + url)
    # respond to the client as the server
    # serverSocket.sendto('ack', address)
