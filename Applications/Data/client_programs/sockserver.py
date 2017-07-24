import socket
import sys
import time


server_address = ('localhost', 10000)

def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)
    count = 0

    while True:
        print "Bind Complete."
        sock.listen(1)
        count += 1
        print "Socket now listening.", count
        connected = True

        while connected == True:
            try:
                current_connection, address = sock.accept()

                while connected == True:
                    #time.sleep(0.5)
                    data = current_connection.recv(2048)

                    if len(data)>0:
                        if data == 'quit\r\n':
                            current_connection.shutdown(1)
                            current_connection.close()
                            break
                        else:
                            print 'RX Data({0}): {1}'.format(len(data), repr(data))
                    else:
                        pass
            except socket.error as e:
                print "Connection terminated forcibly."
                connected = False
                #current_connection.shutdown(1)
                current_connection.close()


if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
