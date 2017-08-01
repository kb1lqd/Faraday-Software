import socket               # Import socket module
import random
import struct
import time
import sys
import base64

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 10011              # Reserve a port for your service.

RXDATASIZE = 42

s.connect((host, port))
print s


while True:
    try:
        while True:
            time.sleep(0.001)
            s.sendall(" ")
            temp = s.recv(4096)
            print "RX: ", temp, len(temp)#base64.b64decode(temp[:56])
            print "RX CLEAN: ", temp[:RXDATASIZE], '\n'
            #if not temp: break


        #time.sleep(0.1)

    except socket.error as e:
        print e
        sys.exit(1)
s.close                     # Close the socket when done
