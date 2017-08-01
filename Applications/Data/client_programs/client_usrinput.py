import socket               # Import socket module
import random
import struct
import time
import sys

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 10000               # Reserve a port for your service.

data = ''
#data = str("A"*150)
#data = data.encode('base64','strict')
#print "bytes: ", bytes(data)
#data = 254

s.connect((host, port))

while True:
    try:
		data = raw_input("Enter Message: ")
		print 'sending...'
		s.sendall(data)
        #time.sleep(0.05)
        #print "RX: ", s.recv(4096)
    except socket.error as e:
        print e
        sys.exit(1)
s.close                     # Close the socket when done
