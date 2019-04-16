import threading ,time

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global num
        print(self.name)
        lock.acquire()
        temp = num
        temp-=1
        time.sleep(.01)
        num=temp
        print(num)
        lock.release()


if __name__ == "__main__":
    num = 100
    a=[]
    lock = threading.Lock()
    for i in range(100):
        t = MyThread()
        t.start()
        # a.append(t)
    # for i in a:
    #     i.join()
        t.join()
