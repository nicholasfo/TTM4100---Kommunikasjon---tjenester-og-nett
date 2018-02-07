# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
from socket import *

# Get the server hostname and port as command line arguments
host = "10.0.0.69";
port = 9999;
timeout = 1 # in seconds

# Create UDP client socket
# FILL IN START

# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

clientSocket = socket(AF_INET, SOCK_DGRAM);

# Set socket timeout as 1 second
clientSocket.settimeout(1);

# FILL IN END

# Sequence number of the ping message
ptime = 0

# Ping for 10 times
while ptime < 10:
    ptime += 1
    # Format the message to be sent as in the Lab description
    data = "Ping "+str(ptime)+" "+ str(time.strftime("%H:%M:%S"));
    
    try:
        # Record the "sent time"
        sendTime = time.time();
        # Send the UDP packet with the ping message
        clientSocket.sendto(data, (host, 9999));
        # Receive the server response
        data2, server = clientSocket.recvfrom(1024);
        # Record the "received time"
        recordTime = time.time();
        rtt = recordTime - sendTime;
        # Display the server response as an output
        print "Message received ", data;
        print "Round Trip Time", rtt;
        print
        # FILL IN END
    except:
        # Server does not response
	# Assume the packet is lost
        print("Request timed out.")
        continue
    
# Close the client socket
#clientsocket.close()
