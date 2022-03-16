import socket

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
    print(str(data))
    msg = bytes("input must be a number").encode("utf-8")
    server_socket.sendto(msg, addr)
