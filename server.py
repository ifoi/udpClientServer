import socket
import signal
import sys

# to run server withought using the main runner udpchallenge.py .
# 1. uncomment the last line " startServer() "


# Handler function seems to only works on Unix based systems
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


def sendReceiveData():

    while True:
        try:
            print("waiting for data from client...")
            data, addr = server_socket.recvfrom(bufferSize)
            print("recieved from client: " + str(data.decode("utf-8")))
            clientInput = str(data.decode("utf-8"))
            try:
                int(clientInput)  # checks if input is a number
                msg = str(int(clientInput) * 2)
            except ValueError:
                try:  # check if input is a float
                    float(clientInput)
                    msg = str(float(clientInput) * 2)
                except ValueError:
                    msg = "Error: input must be a number"
            server_socket.sendto(msg.encode("utf-8"), addr)
    # catches Ctr-c or keyboard interrrupt
        except KeyboardInterrupt:
            print()
            response = input(
                "Ctrl-c was pressed. Do you really want to exit? y/n ")
            if response == "y":
                server_socket.close()
                exit(1)


def startServer():
    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #  bind to all interfaces
    server_socket.bind((serverIP, localPort))

    print("  *** UDP server started ***  \n *********** \n use Ctrl-c to exit the program!! ")

    # recieved data from client and send back reply
    sendReceiveData()


# startServer()
