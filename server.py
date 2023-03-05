import socket
import sys
import signal
import time

# define signal handler function
def signal_handler(signal, frame):
    global not_stopped
    print('Exiting gracefully...')
    not_stopped = False

# register signal handlers
signal.signal(signal.SIGQUIT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

# parse command line arguments
if len(sys.argv) < 3:
    sys.stderr.write('ERROR: Missing arguments\n')
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

# create a socket object
client_socket = socket.socket()

# connect to the server
client_socket.connect((host, port))

# send accio command to the server
client_socket.send(b'accio\r\n')

# receive data from the server
total_len = 0
data = client_socket.recv(1024)
while data:
    total_len += len(data)
    data = client_socket.recv(1024)

# print out the total amount of data received
print(f'Total amount of data received: {total_len} bytes')

# close the connection
client_socket.close()

# set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen(1)

not_stopped = True

# accept incoming connections
while not_stopped:
    try:
        # wait for a client to connect
        client_socket, address = server_socket.accept()
        print(f'Accepted connection from {address}')

        # receive data from the client
        total_len = 0
        data = client_socket.recv(1024)
        while data:
            total_len += len(data)
            data = client_socket.recv(1024)

        # print out the total amount of data received
        print(f'Total amount of data received from {address}: {total_len} bytes')

        # close the connection
        client_socket.close()
    except KeyboardInterrupt:
        # exit gracefully if a keyboard interrupt is received
        not_stopped = False

server_socket.close()
