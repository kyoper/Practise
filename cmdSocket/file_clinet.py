import socket,os

sk = socket.socket()
sk.connect(("127.0.0.1", 8012))

image_path = os.path.join(os.path.dirname(__file__), "kyoper.jpg")
with open(image_path, "rb") as f:
    image_len = len(f.read())
send_info = bytes(("%s|%s" % (os.path.basename(image_path), image_len)), "utf8")
sk.send(send_info)
data_num = 0
with open(image_path,"rb") as f_read:    # 此处需要重新打开文件 f_read读取 因为上面拿文件长度 f 已经一次性读取完成了
    while data_num != image_len:         #也可以通过 os.stat(path).st_size 读取文件长度
        data = f_read.read(1024)
        sk.send(data)
        data_num += len(data)
    print("成功")