import sys
import signal

import client
import server

# Handler function only works on Unix based systems


def handler(signum, frame):
    response = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if response == "y":
        exit(1)


# add keyboard interupt handler
signal.signal(signal.SIGINT, handler)


if sys.argv[0] == 'server':
    server.startServer()
elif sys.argv[0] == "client" and len(sys.argv) == 3:
    serverIP = sys.argv[1]
    num = sys.argv[2]
    #client.startClient(serverIP, num )
    client.startClient()
