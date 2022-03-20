import socket
import sys

bufferSize = 4096

# to run client as standalone client, without using the main runner udpchallenge.py
# 1. uncomment the last line " startClient() "
# 2) and the two lines below that start with "serverIP"  and "msg"

# get ip of server and port number from command arguments
# serverIP = sys.argv[1]
# msg = sys.argv[2]


def startClient(serverIP, msg):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # set 5 second timeout on client socket
    client_socket.settimeout(5)

    # TODO  refactor to promt get Port and ServerIP and from user

    PORT = 12345

    # send message to server
    try:
        client_socket.sendto(msg.encode("utf-8"), (serverIP, PORT))

        # recieve message from server
        data, addr = client_socket.recvfrom(bufferSize)
        print("Server reponded with :")
        print(str(data.decode("utf-8")))
    except socket.timeout as e:
        print(e, ": Error did not recieving message from server: ")
        sys.exit(1)

    client_socket.close()


#startClient(serverIP, msg)
