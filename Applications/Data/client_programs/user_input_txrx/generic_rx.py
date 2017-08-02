import socket               # Import socket module
import random
import struct
import time
import sys






while True:
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 10011               # Reserve a port for your service.
    s.connect((host, port))
    try:
        while True:
            time.sleep(0.01)
            s.sendall(" ")
            temp = s.recv(4096)
            if temp != 'No Data! Goodbye.':
                print "RX: ", repr(temp)
            #if not temp: break


        #time.sleep(0.1)

    except socket.error as e:
        #print e
        s.close()
        #sys.exit(1)
    time.sleep(0.01)
s.close                     # Close the socket when done
