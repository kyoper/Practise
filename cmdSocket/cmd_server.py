import socket,subprocess

sk = socket.socket()
addr = ("127.0.0.1",8000)
sk.bind(addr)
sk.listen(3)


while True:
    conn, adr = sk.accept()
    while True:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        if not data:
            break
        obj = subprocess.Popen(data.decode("utf8"),shell=True,stdout=subprocess.PIPE)
        res = obj.stdout.read()
        conn.send(bytes(str(len(str(res,"gbk"))),"utf8"))
        conn.sendall(res)