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
            #return False

        #host= socket.gethostbyname(sys.argv[1])
        try:

            connection.connect((self.domain_name, self.host_port))


            data = connection.recv(1024)
        #    print("Received #1 - {dater}".format(dater=data))

    #        f = open("file.txt", "rb")
            #for data in f:
                #print("Starting sending. . ")
            stuff = connection.send(b'confirm-accio\r\n')
            #print("Sent - {dater}".format(dater=stuff))

            data1=connection.recv(1024)
        #    print("Received #2 - {dater}".format(dater=data1))
            #print(stuff)
            connection.send(b'confirm-accio-again\r\n')
            #print("Sent - {dater}".format(dater=stuff1))
            stuff2 = connection.send(b'\r\n')
            #print("Sent - {dater}".format(dater=stuff2))


            sendfile = open(self.file_name, "rb")
            sendbytes = sendfile.read(1024)
        #    l = sendfile.read(1024)
            while (sendbytes):
                connection.send(sendbytes)
                sendbytes = sendfile.read(1024)

            #connection.send(sendfile)
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
            sys.stderr.write("ERROR: A connection could not be established!")
            #sys.exit(1)
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


#domain_name = "blank"
#port = 0
#file_name = "blank"
#client_cpu = 0
#domain_name = 0
#port = 0
#file_name = 0
host = client()

#argHandler(domain_name, port, file_name)
#print("Arg Handler Complete!")
#print("Domain Name: {domain}".format(domain=domain_name))
#print("Port: {porter}".format(porter=port))
#print("File Name: {filename}".format(filename=file_name))

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
host.makeConnection()
