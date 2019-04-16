import socket,subprocess

sk = socket.socket()
addr = ("127.0.0.1",8000)
sk.connect(addr)

while True:
   inp = input(">>>>>>")
   if inp == "exit":
        break
   sk.send(bytes(inp,"utf8"))
   res_num = int(str(sk.recv(1024),"utf8"))
   data = bytes()
   while len(str(data,"gbk")) < res_num:
       data+=sk.recv(1024)
   print(str(data,"gbk"))


