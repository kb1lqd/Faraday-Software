import socket
import time
import struct

import argparse
import sys
import os


def send(data):
	#data = ''

	# Get arguments
	#parser = argparse.ArgumentParser()
	#parser.add_argument("fragsize", type=int, help="Fragment size in bytes of data", default=16)
	#parser.add_argument("--data", help="Data string to be transmitted.")
	#args = parser.parse_args()

	# Parse arguments
	#STRUCTSIZE = args.fragsize
	#if args.data is not None:
	#    data = args.data
	#else:
	#    for line in sys.stdin:
	#	data = data + line  # Concatenate stdin lines to single string



	# Open socket connection to Faraday data server
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (socket.gethostname(), 10000)
	print 'connecting to {0} port {1}'.format(server_address[0], server_address[1])
	sock.connect((server_address))

	# Send data
	sock.sendall(data)

	# Close socket
	sock.close()
