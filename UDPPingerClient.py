# Alex Harris
# Network Programming
# Spring 2017
# Homework 5: A UDP Pinger

from socket import *
import time

# define a class to hold meaningful info about the ping session
class ping_summary(object):
    def __init__(self):
        self.minimum_time = 0
        self.maximum_time = 0
        self.average_time = 0
        self.num_returned_msg = 0
        self.aggregated_ping_time = 0
        self.num_packets_lost = 0
        self.packet_loss_rate = 0.0

# build socket
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

p_summary = ping_summary()
for seqno in range(1,10): # do from 1 to 10
    try:
        # Here's where you're going to send the ping message
        # You've already got the sequence number. You can
        # use the time module imported above to get a timestamp
        # with time.time(). Remember that to cast numbers to
        # strings you can use the str() function.

        message = 'Ping ' +  str(seqno) +' '+ str(time.time())
        clientSocket.sendto(message.encode(), (serverName, serverPort))

        # After the message has been sent, set the timeout.
        clientSocket.settimeout(1)  # sets a timeout of one second.
                                    # This will be caught in the
                                    # except block below.

        # Next, you're going to receive the message from
        # the server (assuming the timeout doesn't go off).
        # You should then grab another timestamp and check how
        # much time has elapsed, in order that you can keep track


        returned_message, serverAddress = (
            clientSocket.recvfrom(2048)
        )
        decoded_message = returned_message.decode()
        decoded_message = decoded_message.split(' ')
        print('return message : ', returned_message.decode(), ' server address : ', serverAddress)

        # cast the time stamp to a float for math
        message_time_stamp = float(decoded_message[2])

        elapsedTime = time.time()-message_time_stamp
        # print('elapsed time : ', elapsedTime)

        # find the max
        if (elapsedTime > p_summary.maximum_time):
            p_summary.maximum_time = elapsedTime

        # find the min
        if (p_summary.minimum_time == 0):
            p_summary.minimum_time = elapsedTime
        elif (elapsedTime < p_summary.minimum_time):
            p_summary.minimum_time = elapsedTime

        # increment the number of messages received
        p_summary.num_returned_msg+=1

        # increment the aggregated time of successful pings
        p_summary.aggregated_ping_time+=elapsedTime

        # Here we print out the data for each ping response.
        # Note the way Python's number formatting works. The
        # format function yields a float of precision 3, which
        # then must be explicitly converted to string with str().
        print(
            "from " + str(serverAddress[0]) + ": time=" + str(format(elapsedTime*1000, '.3f'))
            )
    except timeout:
        # increment the number of packets lost
        p_summary.num_packets_lost += 1
        # And we print the message to the terminal:
        print(
            str(seqno) + ": Timed out"
            )
p_summary.average_time = p_summary.aggregated_ping_time/p_summary.num_returned_msg
p_summary.packet_loss_rate = p_summary.num_packets_lost/(p_summary.num_returned_msg+p_summary.num_packets_lost)
print(
    # Print out the report with minimum, maximum, and average time between packets.
    '\naverage time for packet transmission : ', str(format(p_summary.average_time*1000, '.3f')),
    '\nmaximum time for packet transmission : ', str(format(p_summary.maximum_time*1000, '.3f')),
    '\nmaximum time for packet transmission : ', str(format(p_summary.minimum_time*1000, '.3f'))
    )
print(
    # Report the packet loss rate as a percentage of packets sent.
    # Check the screenshots in the assignment description for what
    # the output should look like.
    '\nnumber of successful packet transmissions : ', p_summary.num_returned_msg,
    '\nnumber of lost packet transmissions : ', p_summary.num_packets_lost,
    '\npacket loss rate : ', "{0:.0f}%".format(p_summary.packet_loss_rate*100),
    )
clientSocket.close()
