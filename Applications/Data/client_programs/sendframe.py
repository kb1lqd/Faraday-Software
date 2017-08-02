import socket
import time
import struct
import bytestuff
import argparse

# Get arguments
parser = argparse.ArgumentParser()
parser.add_argument("fragsize", type=int, help="Fragment size in bytes of data", default=16)
parser.add_argument("data", help="Data string to be transmitted.")
args = parser.parse_args()

# Parse arguments
STRUCTSIZE = args.fragsize
data = args.data

# Create data fragments as needed
datafrag = bytestuff.fragmentmsg(data, STRUCTSIZE)

# Open socket connection to Faraday data server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 10000)
print 'connecting to {0} port {1}'.format(server_address[0], server_address[1])
sock.connect((server_address))

# Send data
for item in datafrag:
    msg_stuffed = bytestuff.byte_escape_fixed_length(bytestuff.framing_startbyte, bytestuff.framing_stopbyte, bytestuff.framing_escapebyte, item)
    sock.sendall(msg_stuffed)

# Close socket
sock.close()
