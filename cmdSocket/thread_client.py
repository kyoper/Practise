import socket

sk =socket.socket()
sk.connect(("127.0.0.1",8055))
while True:
    inp = input(">>>>>")
    sk.send(bytes(inp,"utf8"))
    data=sk.recv(1024)
    print(str(data,"utf8"))