import socket
import sys
import signal
import time

# define signal handler function
def signal_handler(signal, frame):
    global not_stopped
    print('Exiting gracefully...')
    not_stopped = False
    sys.exit(0) # exit with code 0

# register signal handlers
signal.signal(signal.SIGQUIT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

# parse command line arguments
if len(sys.argv) < 2:
    sys.stderr.write("ERROR: Missing port number\n")
    sys.exit(1)

try:
    port = int(sys.argv[1])

except ValueError:
    sys.stderr.write("ERROR: Invalid port number\n")
    sys.exit(1)

if port > 65535:
    sys.stderr.write("ERROR: Invalid port number\n")
    sys.exit(1)

if port < 0:
    sys.stderr.write("ERROR: Invalid port number\n")
    sys.exit(1)

# create a socket object
server_socket = socket.socket(AF_INET, SOCK_STREAM)

# bind the socket to all interfaces and specified port number
try:
    server_socket.bind(('0.0.0.0', port))
except OSError:
    sys.stderr.write("ERROR: Could not bind to port {port}\n")
    sys.exit(1)

# set the server to listen for incoming connections, with a backlog of 10
server_socket.listen(10)

#print("Server is listening on port {port}...')

#not_stopped = True

# accept incoming connections
#while not_stopped:
#    try:
#        # wait for a client to connect
#        client_socket, address = server_socket.accept()
        #print("Accepted connection from {address}"")

        # set a timeout of 10 seconds for the connection
#        client_socket.settimeout(10)

        # send accio command to the client
#        client_socket.send(b'accio\r\n')

        # receive data from the client and count the amount of data received
#        total_len = 0
#        data = client_socket.recv(1024)
#        while data:
#            total_len += len(data)
#            data = client_socket.recv(1024)

        # print out the total amount of data received
        #print("Total amount of data received from {address}: {total_len} bytes")

        # close the connection
#        client_socket.close()
#    except KeyboardInterrupt:
        # exit gracefully if a keyboard interrupt is received
#3        not_stopped = False
#    except socket.timeout:
#        # if the client doesn't send any data for 10 seconds, abort the connection
#        client_socket.send(b'ERROR')
#        client_socket.close()
#    except ConnectionResetError:
        # if the client resets the connection, just print a message and continue
    #    print("Connection with {address} reset by client")

#server_socket.close()
