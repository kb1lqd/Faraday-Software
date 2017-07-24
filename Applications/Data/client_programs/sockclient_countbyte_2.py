import socket
import sys
import time
import struct
import bytestuff
import Queue


delay_interval_sec = 0.01
delay_tx_interval_sec = 0.1

temp_queue = Queue.Queue()
queue_get_size = int(delay_tx_interval_sec/delay_interval_sec)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

packetstruct = struct.Struct('%uB' % queue_get_size)
temp_msg = []

server_address = ('localhost', 10000)
print 'connecting to {0} port {1}'.format(server_address[0], server_address[1])
#sock.connect(server_address)
message = ''
count = 0
start_time = time.time()
while True:
    #temp_msg.append(count)
    temp_queue.put(count)
    #message = packetstruct.pack(count)
    #sock.sendall(message)
    time.sleep(delay_interval_sec)
    if count >= 255:
        count = 0
    else:
        count += 1

    if time.time() - start_time >= delay_tx_interval_sec:
        temp_list = []
        for i in range(0, queue_get_size):
            temp_list.append(temp_queue.get())
        print temp_queue.qsize(), temp_list
        print packetstruct.pack(*temp_list)
        temp_msg = []
        start_time = time.time()

sock.close()
