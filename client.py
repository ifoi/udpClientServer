import socket
import sys
import signal

bufferSize = 4096


def handler(signum, frame):
    response = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if response == "y":
        exit(1)


# add keyboard interupt handler
signal.signal(signal.SIGINT, handler)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get ip of server and port number from command argumentsr

# def client(server_ip, port):
serverIP = sys.argv[1]
PORT = int(sys.argv[2])

print("port number is %d" % PORT)

msg = "The server ip address is : " + \
    str(serverIP)  # extend to include port number


# send message to server

client_socket.sendto(msg.encode("utf-8"), (serverIP, PORT))

# recieve message from server
data, addr = client_socket.recvfrom(bufferSize)
print("Server reponds with :")
print(str(data.decode("utf-8")))

client_socket.close()
