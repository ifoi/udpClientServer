### udpClientServer

To run this, first clone the repo.  
 (or just copy the 3 files.. udpchallenge.py server.py and client.py to the same directory )

To start the server run " `udpchallenge server` " and

" `udpchallenge.py 127.0.0.1 <text> ` " to start the client
( where `<text>` is the string you want to send to the server. <br /> If the sting is an int or float, the server will double it and send the results back to the client <br />
otherwise it returns a message indicating that the `input must be a number` )

TODO:

- ~~currently working on inttegrating them into udpClientServer.py so that both client and server can be started from that one file. ~~
- Implement tests
  ~~This text is struckthrough.~~
