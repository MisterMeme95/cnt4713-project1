#!/usr/bin/env python3

import time
import sys
import socket
import signal

if __name__ == '__main__':
    sys.stderr.write("server is not implemented yet\n")



def validatePort(port):
    if not isinstance(port, int):
        sys.stderr.write("ERROR: Port is not an integer!")
        sys.exit(1)

    if not 1 <= port <= 65535:
        sys.stderr.write("ERROR: Port is not valid range.")
        sys.exit(1)



class server:
    domain_name = 0
    host_port = 0

    def __init__(self):
        #self.domain_name = sys.argv[1]
        self.host_port = int(sys.argv[1])


    def makeConnection(self):
        server_socket = socket.socket()
        try:

            server_socket.listen(10)
            #server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except:
            sys.stderr.write('ERROR: Invalid port number\n')
            sys.exit(1)


        try:
            server_socket.listen(10)
            #server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except:
            sys.stderr.write('ERROR: Invalid port number\n')
            sys.exit(1)



        server_socket.settimeout(10)

        try:
            server_socket.listen(10)
            #server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except:
            sys.stderr.write('ERROR: Invalid port number\n')
            sys.exit(1)


        try:
            # read data from the client
            data = server_socket.recv(1024)
            total_len = len(data)
            while data:
                data = server_socket.recv(1024)
                total_len += len(data)
            # send the total length of the data received back to the client
            server_socket.send(str(total_len).encode())
        except socket.timeout:
            # if the client doesn't send any data for 10 seconds, abort the connection
            server_socket.send(b'ERROR')
            print(f'Connection with {addr} timed out')
            
        except ConnectionResetError:
            # if the client resets the connection, just print a message and continue
            print(f'Connection with {addr} reset by client')
        finally:
            # close the connection
            conn.close()





host = server()
host.makeConnection()
