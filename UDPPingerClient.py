from socket import *


# build socket\
# FIXME - input the ip address of the server rather than local host
serverName = 'localhost'
serverPort = 12000

# establish the udp socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

for x in range(1,10): # do from 1 to 10
    try:

        # determine the meme message to send
        message = 'meme:' + 'http://opensource.eco'

        clientSocket.sendto(message.encode(), (serverName, serverPort))

        # After the message has been sent, set the timeout.
        clientSocket.settimeout(1)  # sets a timeout of one second.
                                    # This will be caught in the
                                    # except block below.


        # determine the return message & receive it
        # returned_message, serverAddress = (
        #     clientSocket.recvfrom(2048)
        # )
        # # decode the return message from the server
        # decoded_message = returned_message.decode()
        # decoded_message = decoded_message.split(' ')
        # print('return message : ', returned_message.decode(), ' server address : ', serverAddress)

    except err:
        print('err')

clientSocket.close()
