#!/usr/bin/env python3

import time
import sys
import socket

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
        connection = 0
        try:
            server_socket.bind(('0.0.0.0', host_port))
            server_socket.listen(1)
            #server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except socket.error as err:
            sys.stderr.write("ERROR: Socket Creation failed!")
            sys.exit(1)
            return False

        try:
            self.domain_name = socket.gethostbyname(self.domain_name)

        except socket.gaierror:
            sys.stderr.write("ERROR: The host could not be reached!")
            sys.exit(1)


        try:
            validatePort(self.host_port)

        except socket.error as err:
            sys.stderr.write("ERROR: Port is not in valid rang4e!")
            sys.exit(1)

        try:

            sys.stderr.write("ERROR: ")
            server_socket.settimeout(10)
            server_socket.connect((self.domain_name, self.host_port))
            while True:
                data = server_socket.recv(1024)
                if data:
                    stuff = server_socket.send(b'confirm-accio\r\n')

                    while True:
                        data1=server_socket.recv(1024)
                        if data1:
                            stuff2 = server_socket.send(b'confirm-accio-again\r\n')
                            break
                    break

            stuff2 = server_socket.send(b'\r\n')

            sendfile = open(self.file_name, "rb")

            while True:
                sendbytes = sendfile.read(10000)
                if len(sendbytes) == 0:
                    break
                connection.send(sendbytes)



        except socket.error:
            print("ERROR: Connection failed!")
            sys.exit(1)
            return False






host = server()
host.makeConnection()
