import socket
import sys

bufferSize = 4096

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get ip of server and port number from command argumentsr

# def client(server_ip, port):
serverIP = sys.argv[1]
PORT = int(sys.argv[2])

print("port number is %d" % PORT)

msg = serverIP  # extend to include port number


# send message to server

client_socket.sendto(msg.encode("utf-8"), (serverIP, PORT))

# recieve message from server
data, addr = client_socket.recvfrom(bufferSize)
print("Server reponds with")
print(str(data))

client_socket.close()
