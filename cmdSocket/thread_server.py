import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
       while True:
            conn =self.request
            addr=self.client_address
            data = conn.recv(1024)
            print(str(data,"utf8"))
            inp = input(">>>>>>")
            conn.send(bytes(inp,"utf8"))




if __name__ =="__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1",8055),MyServer)
    server.serve_forever()