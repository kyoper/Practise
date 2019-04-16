import socket,os

sk = socket.socket()
sk.bind(("127.0.0.1",8012))
sk.listen(3)
while True:
    conn, address = sk.accept()
    save_path = os.path.join(os.path.dirname(__file__), "kyoper1.jpg")
    recv_info = conn.recv(1024)
    date_num = 0
    with open(save_path, "ab") as f_write:
        while date_num != int(str(recv_info,"utf8").split("|")[1]):
            print("1")
            data = conn.recv(1024)
            f_write.write(data)
            date_num += len(data)
