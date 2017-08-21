import socket               # Import socket module
import time
import argparse
import sys

# Get arguments
#parser = argparse.ArgumentParser()
#args = parser.parse_args()

# Parse arguments


# Create data fragments as needed


alive = True



s = socket.socket()         # Create a socket object
#s.setblocking(False)
s.settimeout(5)
host = socket.gethostname() # Get local machine name
port = 10011               # Reserve a port for your service.
s.connect((host, port))
try:
    while alive:
        time.sleep(0.01)
        s.sendall(" ")
        temp = s.recv(4096)
        if temp != 'No Data! Goodbye.':
            sys.stdout.write(temp)
        else:
            alive = False
except StandardError as e:
    print e
    pass


finally:
    print"Closing socket connection."
    s.close()                     # Close the socket when done
