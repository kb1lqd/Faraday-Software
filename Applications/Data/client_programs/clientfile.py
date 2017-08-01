import socket               # Import socket module
import random
import struct
import time
import sys
import base64

import bytestuff

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 10011              # Reserve a port for your service.

RXDATASIZE = 42

s.connect((host, port))
print s

msgrx = bytestuff.rxparse()


while True:
    try:
        while True:
            time.sleep(0.001)
            s.sendall(" ")
            temp = s.recv(4096)
            #print "RX CLEAN: ", repr(temp[:RXDATASIZE])
            #if not temp: break
            print "DATA RX SOCKET", len(temp), repr(temp)
            final_data = ''
            for byte in temp:
                #print repr(byte)
                rxdata = msgrx.parseframe(byte, bytestuff.framing_startbyte, bytestuff.framing_stopbyte, bytestuff.framing_escapebyte)
                if(rxdata is not None):
                    print "RXDATA: ", rxdata
                    final_data = final_data + rxdata
                    #test = msgrx.parsepacketfromdatagram(temp[:RXDATASIZE])
            #if test is not None:
            #    print "RECEIVED: ", test



        #time.sleep(0.1)

    except socket.error as e:
        print e
        sys.exit(1)
    finally:
        print "FINAL: ", final_data
s.close                     # Close the socket when done

print "DONE"