import socket
import sys
import signal

bufferSize = 4096

serverIP = sys.argv[1]
msg = sys.argv[2]


def handler(signum, frame):
    response = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if response == "y":
        exit(1)


# add keyboard interupt handler for POSIX systems
signal.signal(signal.SIGINT, handler)


def startClient(serverIP, msg):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # set 5 second timeout on client socket
    client_socket.settimeout(5)

    # get ip of server and port number from command argumentsr

    # def client(server_ip, port):

    # serverIP = sys.argv[1]
    # msg = sys.argv[2]

    # TODO  refactor to get input from user

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


startClient(serverIP, msg)
