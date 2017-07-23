import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print 'connecting to {0} port {1}'.format(server_address[0], server_address[1])
sock.connect(server_address)
message = ''
while message is not 'quit':
    message = raw_input("Enter Message:")
    sock.sendall(message)
sock.close()
