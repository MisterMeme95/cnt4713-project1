#!/usr/bin/env python3

import sys
import socket

#if __name__ == '__main__':
#    sys.stderr.write("client is not implemented yet\n")

#This is simply a way for us to run a test to see if
#We're passing the files correct


#These variables will be used for connectivity.
def makeConnection(connection, host, port):
    port = int(sys.argv[2])
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as err:
        sys.stderr.write("ERROR - Socket Creation failed!")
        return False

    try:
        host = socket.gethostbyname(sys.argv[1])

    except socket.gaierror:
        sys.stderr.write("ERROR - The host could not be reached!")
        return False


    try:
        connection.connect((host, port))
        data = connection.recv(1024)
        print("Received. . . {dater}".format(dater=data))

    except:
        sys.stderr.write("ERROR - A connection could not be established!")
        return False
        #data = s.recv(1024)
        #print('Received', repr(data))


domain_name = "blank"
port = 0
client_cpu = 0
makeConnection(client_cpu, domain_name, port)
