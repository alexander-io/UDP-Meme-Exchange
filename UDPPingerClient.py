from socket import *
import os, sys
import subprocess
import re

# build socket\
# FIXME - input the ip address of the server rather than local host
serverName = 'opensource.eco'
serverPort = 12000

# establish the udp socket
clientSocket = socket(AF_INET, SOCK_DGRAM)


proc = subprocess.Popen('ipconfig' , stdout=subprocess.PIPE)
output = proc.stdout.read()
output = output.decode('utf-8')

IPV4Line = output.split('\n')
IPV4 = IPV4Line[26].split(':')
IPV4 = IPV4[1].strip(' \t\n\r')

print(IPV4)
# IPV4toSend = IPV4.encode('utf-8')

for x in range(1,10): # do from 1 to 10
    try:

        # determine the meme message to send
        # message = 'meme@' + 'http://opensource.eco'
        message = 'meme@' + IPV4

        clientSocket.sendto(message.encode(), (serverName, serverPort))

        # After the message has been sent, set the timeout.
        clientSocket.settimeout(.01)  # sets a timeout of one second.
                                    # This will be caught in the
                                    # except block below.
        print("before recv")

        # determine the return message & receive it

        returned_message = clientSocket.recv(1024)


        # returned_message, serverAddress = (
        #     clientSocket.recv(1024)
        # )

        print("before decode")
        # # decode the return message from the server
        decoded_message = returned_message.decode('utf-8')
        print("here is the message",decoded_message)
        if 'ack' in decoded_message:
            print("got ack")
            break

        # decoded_message = decoded_message.split(' ')
        # print('return message : ', returned_message.decode(), ' server address : ', serverAddress)

    except:
        pass

clientSocket.close()



#
# Windows IP Configuration
#
#
# Ethernet adapter Ethernet:
#
#    Media State . . . . . . . . . . . : Media disconnected
#
#    Connection-specific DNS Suffix  . : pugetsound.edu
#
# Ethernet adapter VirtualBox Host-Only Network:
#
#    Connection-specific DNS Suffix  . :
#    Link-local IPv6 Address . . . . . : fe80::924:d5ca:32a5:7e19%14
#    IPv4 Address. . . . . . . . . . . : 192.168.56.1
#    Subnet Mask . . . . . . . . . . . : 255.255.255.0
#    Default Gateway . . . . . . . . . :
#
# Wireless LAN adapter Local Area Connection* 12:
#
#    Media State . . . . . . . . . . . : Media disconnected
#    Connection-specific DNS Suffix  . :
#
# Wireless LAN adapter Wi-Fi:
#
#    Connection-specific DNS Suffix  . : pugetsound.edu
#    Link-local IPv6 Address . . . . . : fe80::c9fd:fc22:8f64:5131%9
#    IPv4 Address. . . . . . . . . . . : 10.209.24.101
#    Subnet Mask . . . . . . . . . . . : 255.255.252.0
#    Default Gateway . . . . . . . . . : 10.209.24.1
