import socket               # Import socket module
import time
import argparse
import sys
import dpkt


alive = True





while True:
    s = socket.socket()  # Create a socket object
    # s.setblocking(False)
    #s.settimeout(5)
    host = socket.gethostname()  # Get local machine name
    port = 10011  # Reserve a port for your service.
    s.connect((host, port))
    print "Connected"
    try:
        while alive:
            time.sleep(0.01)
            s.sendall(" ")
            temp = s.recv(2048)
            if temp != 'No Data! Goodbye.':
                #temp = dpkt.udp.UDP(temp)
                #temp = dpkt.ip.IP(temp)
                print repr(temp)
                #sys.stdout.write(temp)
            else:
                alive = False
    except StandardError as e:
        #print e
        pass
    except socket.timeout as e:
        pass


    finally:
        #print"Closing socket connection."
        s.close()                     # Close the socket when done
