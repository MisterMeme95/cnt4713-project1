#!/usr/bin/env python3

import time
import sys
import socket

#if __name__ == '__main__':
#    sys.stderr.write("client is not implemented yet\n")

#This is simply a way for us to run a test to see if
#We're passing the files correct


#These variables will be used for connectivity.
def validatePort(port):
    if not isinstance(port, int):
        sys.stderr.write("ERROR: Port is not an integer!")
        sys.exit(1)
    #    print("Port is an int!")
    #   Last check

    if not 1 <= port <= 65535:
        sys.stderr.write("ERROR: Port is not valid range.")
        sys.exit(1)



class client:
    domain_name = 0
    host_port = 0
    file_name = 0

    def __init__(self):
        #self.argHandler(self.domain_name, self.host_port, self.file_name)
        self.domain_name = sys.argv[1]
        self.host_port = int(sys.argv[2])
        #print("Arg2 = {arger2}".format(arger2=sys.argv[2]))
        self.file_name = sys.argv[3]
        #print("Arg3 = {arger3}".format(arger3=sys.argv[3]))
        #self.year = year


    #def makeConnection(connection, host, port):
        #port = int(sys.argv[2])


    def makeConnection(self):
        connection = 0
        try:
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #print("Connection made successfully!")
        except socket.error as err:
            sys.stderr.write("ERROR: Socket Creation failed!")
            sys.exit(1)
            return False

        try:
            self.domain_name = socket.gethostbyname(self.domain_name)

        except socket.gaierror:
            sys.stderr.write("ERROR: The host could not be reached!")
            sys.exit(1)
            #return False


        try:
            validatePort(self.host_port)

        except socket.error as err:
            sys.stderr.write("ERROR: Port is not in valid rang4e!")
            sys.exit(1)

        try:

            connection.connect((self.domain_name, self.host_port))

            data = connection.recv(1024)
            stuff = connection.send(b'confirm-accio\r\n')


            data1=connection.recv(1024)
            connection.send(b'confirm-accio-again\r\n')
            stuff2 = connection.send(b'\r\n')

            sendfile = open(self.file_name, "rb")
            sendbytes = sendfile.read(1024)

            while (sendbytes):
                connection.send(sendbytes)
                sendbytes = sendfile.read(1024)
                if len(sendbytes) == 0: break




        except socket.gaierror:
            sys.stderr = print("ERROR: A connection could not be established!")
            return False
            sys.exit(1)






host = client()
host.makeConnection()
