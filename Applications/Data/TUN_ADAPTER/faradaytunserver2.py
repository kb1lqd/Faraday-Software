import fcntl
import os
import select
import struct
from subprocess import call
import time
import sys
import faraday_send_tun
import socket

TUNSETIFF = 0x400454ca
TUNSETOWNER = TUNSETIFF + 2
IFF_TUN = 0x0001
IFF_TAP = 0x0002
IFF_NO_PI = 0x1000

# Open file corresponding to the TUN device.
tun = open('/dev/net/tun', 'r+b')
ifr = struct.pack('16sH', 'tun1', IFF_TUN | IFF_NO_PI)
fcntl.ioctl(tun, TUNSETIFF, ifr)
fcntl.ioctl(tun, TUNSETOWNER, 1000)

# Create TUN adapter
os.system('ip addr add 192.178.90.1/32 dev tun1')
#Set MTU
os.system('ip link set dev tun1 mtu 128')
# Bring UP Tun adapter
os.system('ip link set dev tun1 up')
# Add routing rule to avoid linux optimization and ensure data goes through adapter.
os.system('ip route add 192.178.90.2/32 dev tun1')


#raw_input("press enter to continue")

tun_fd = tun.fileno()



while True:

    try:
        s = socket.socket()  # Create a socket object
        # s.setblocking(False)
        # s.settimeout(5)
        host = socket.gethostname()  # Get local machine name
        port = 10011  # Reserve a port for your service.
        s.connect((host, port))

        read, write, exc = select.select([tun_fd, ], [tun_fd, ], [])

        #for s in read:
        #    rxdata = os.read(s, 1500)
        #    print '\n'
        #    print "RX Data (LEN = {0})".format(len(rxdata))
        #    print "ORIG: {0}".format(rxdata)
        #    print "RAW: {0}".format(repr(rxdata))
            # faraday_send_tun.send(rxdata)
        # call(['echo "Test" | python sendframe.py'])

        time.sleep(0.01)
        s.sendall(" ")
        temp = s.recv(2048)
        if temp != 'No Data! Goodbye.':
            #temp = dpkt.udp.UDP(temp)
            #temp = dpkt.ip.IP(temp)
            print repr(temp)
            os.write(s, rxdata)
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
        s.close()




                     # Close the socket when done
