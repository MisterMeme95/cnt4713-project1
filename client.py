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
    #    for p in data:
    #        print(p)
        print("Received #1 - {dater}".format(dater=data))

        f = open("file.txt", "rb")
        #for data in f:
            #print("Starting sending. . ")
        stuff = connection.send(b'confirm-accio\r\n')
        print("Sent - {dater}".format(dater=stuff))

        data1=connection.recv(1024)
        print("Received #2 - {dater}".format(dater=data1))
            #print(stuff)
        stuff1 = connection.send(b'confirm-accio-again\r\n')
        print("Sent - {dater}".format(dater=stuff1))
        stuff2 = connection.send(b'\r\n')
        print("Sent - {dater}".format(dater=stuff2))
        #print("SENT - confirm-accio\r\n")

    #    data = connection.recv(1024)
    #    for p in data:
    #        print(p)
        #data = connection.recv(1024)
        #print("Received - {dater}".format(dater=data))

        #f = connection.send(1024)
        #connection.send("Twenty-five bytes to send")
        #data = connection.recv(1024)
        #print("Received:{dater}".format(dater=data))

    except:
        sys.stderr.write("ERROR - A connection could not be established!")
        return False



#def getArguments(arg1, arg2, arg3):
#    num = len(sys.argv)
#    iterate = 1
#    while iterate < num:
#        if iterate == 1:
#            arg1 = sys.argv[iterate]
#
#        elif iterate == 2:
#            if isinstance(sys.argv[2], int):
#                arg2 = int(sys.argv[iterate])
#
#            else:
#                sys.stderr.write("ERROR - In arguments!")
#
#        else:
#            arg3 = sys.argv[iterate]
#
#        iterate += 1


domain_name = "blank"
port = 0
file_name = "blank"
client_cpu = 0
domain_name = sys.argv[1]
port = int(sys.argv[2])
file_name = sys.argv[3]
#f = open(file_name, "rb")
#connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostbyname(sys.argv[1])
#connection.connect((host, port))

#data = connection.recv(1024)
#print("Received:{dater}".format(dater=data))

#with open(file_name, "rb") as file:
#    for data in file:
#        connection.send(data)

#data = connection.recv(1024)
#print("Received:{dater}".format(dater=data))
makeConnection(client_cpu, domain_name, port)
