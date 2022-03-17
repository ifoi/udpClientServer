import socket
import signal
import sys


def handler(signum, frame):
    response = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if response == "y":
        exit(1)


# add keyboard interupt handler
signal.signal(signal.SIGINT, handler)

serverIP = "0.0.0.0"
localPort = 12345
bufferSize = 4096

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#  bind to all interfaces
server_socket.bind((serverIP, localPort))

print("UDP server started   ")

# recived data from client and send back reply
while True:
    data, addr = server_socket.recvfrom(bufferSize)
    print("recieved from client:  {str(data)} ")
    msg = bytes("input must be a number").encode("utf-8")
    server_socket.sendto(msg, addr)
