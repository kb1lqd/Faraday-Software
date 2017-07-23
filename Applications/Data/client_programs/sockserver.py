import socket
import sys
import time

server_address = ('localhost', 10000)

def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)

    print "Bind Complete."
    sock.listen(1)
    print "Socket now listening."

    while True:
        current_connection, address = sock.accept()
        while True:
            #time.sleep(0.5)
            data = current_connection.recv(2048)

            if len(data)>0:
                if data == 'quit\r\n':
                    current_connection.shutdown(1)
                    current_connection.close()
                    break
                else:
                    print repr(data), len(data), type(data)
                    print data
            else:
                pass


if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
