import sys
import signal

import client
import server

# Handler function seems to only works on Unix based systems


def handler(signum, frame):
    response = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if response == "y":
        exit(1)


# add keyboard interupt handler
signal.signal(signal.SIGINT, handler)


def runner():
    if sys.argv[1] == 'server':
        print("about to start server******")
        server.startServer()
    elif sys.argv[1] == "client" and len(sys.argv) == 4:
        serverIP = sys.argv[2]
        num = sys.argv[3]
        client.startClient(serverIP, num)
    else:
        string = []
        if len(sys.argv) >= 2:
            string = sys.argv[1:]
        print(
            f'invalid arguments {string} \n ,Please enter "server" to start the server.  \n or "client <serverIP>  <string>" to start the client')


if __name__ == "__main__":
    runner()
