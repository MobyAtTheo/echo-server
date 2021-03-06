#!/usr/bin/env python3

import socket
import sys

"""
# demo client:
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
client_socket.connect(("127.0.0.1", 20000))

my_message = input("> ")
client_socket.sendall(my_message.encode('utf-8'))

received_message = client_socket.recv(4096)
print("Server says: {}".format(received_message.decode()))

client_socket.close()
"""

import datetime
time_now = datetime.datetime.timestamp(datetime.datetime.now())
time_start = datetime.datetime.timestamp(datetime.datetime.now())


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 12000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    # sock = None
    #### markob
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)

    #### markob

    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    # TODO: connect your socket to the server here.
    sock.connect((server_address[0], server_address[1]))

    # you can use this variable to accumulate the entire message received back
    # from the server
    received_message = ''

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        # TODO: send your message to the server here.
        #my_message = input("> ")
        #sock.sendall(my_message.encode('utf-8'))
        sock.sendall(msg.encode('utf-8'))


        # TODO: the server should be sending you back your message as a series
        #       of 16-byte chunks. Accumulate the chunks you get to build the
        #       entire reply from the server. Make sure that you have received
        #       the entire message and then you can break the loop.
        #
        #       Log each chunk you receive.  Use the print statement below to
        #       do it. This will help in debugging problems
        # chunk = ''
        while True:
            chunk = sock.recv(4096)

            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)

            received_message = received_message + chunk  #check if complalin str/byte

            if str(received_message) == str(msg):
                print ("[*] exiting loop")
                break

            if len(received_message) > 2:
                #raise "Too many bytes, exiting."
                print("[-] Too many bytes, exiting.")
                break


    finally:
        # TODO: after you break out of the loop receiving echoed chunks from
        #       the server you will want to close your client socket.
        print('closing socket', file=log_buffer)

        # TODO: when all is said and done, you should return the entire reply
        # you received from the server as the return value of this function.


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
