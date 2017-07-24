import socket
import sys
import time
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

packetstruct = struct.Struct('B')

server_address = ('localhost', 10000)
print 'connecting to {0} port {1}'.format(server_address[0], server_address[1])
sock.connect(server_address)
message = ''
count = 0
while True:
    message = packetstruct.pack(count)
    sock.sendall(message)
    if count >= 255:
        count = 0
    else:
        count += 1

sock.close()
