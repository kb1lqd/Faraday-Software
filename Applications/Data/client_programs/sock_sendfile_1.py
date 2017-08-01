import socket
import sys
import time
import struct
import bytestuff
import Queue
import base64
import time



delay_interval_sec = 0.01
delay_tx_interval_sec = 0.1

temp_queue = Queue.Queue()
queue_get_size = int(delay_tx_interval_sec/delay_interval_sec)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

packetstruct = struct.Struct('%uB' % queue_get_size)
temp_msg = []

filepath = 'test.txt'


server_address = (socket.gethostname(), 10000)

def fragfile(filepath, fragment_size):

    with open(filepath, 'r') as f:
        read_data = f.read()
    print read_data


    test = bytestuff.fragmentmsg(read_data, fragment_size)
    return test

def main():
    """Main function."""

    print 'connecting to {0} port {1}'.format(server_address[0], server_address[1])
    sock.connect((server_address))
    message = ''
    count = 0

    #fragged_file = fragfile('test.txt', 10)

    #print fragged_file

    with open(filepath, 'r') as f:
        read_data = f.read()



    fragged_file = bytestuff.createmsgpackets('kb1lqd', 10, read_data)

    #print "fragged_file: ", fragged_file

    print "FRAGLEN ", len(fragged_file[0])

    # print temp_queue.qsize(), temp_list
    #msg = packetstruct.pack(*temp_list)
    for item in fragged_file:

        msg_stuffed = bytestuff.byte_escape_fixed_length(bytestuff.framing_startbyte, bytestuff.framing_stopbyte,
                                                         bytestuff.framing_escapebyte, item)
        print "Len ", len(item)
        msg_stuffed = bytestuff.create_fixed_length_packet(msg_stuffed, 32)
        print msg_stuffed, len(msg_stuffed)
        sock.sendall(msg_stuffed)
        time.sleep(0.05)

    sock.close()

if __name__ == '__main__':
    main()
