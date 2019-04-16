import threading,time,random
class Producer(threading.Thread):
    def __init__(self):
        super(Producer,self).__init__()

    def run(self):
        global L
        while True:
            num = random.randint(0,100)
            print("生产者",self.name,"生产"+str(num),L)
            # time.sleep(0.0000000001)      # 线程之间是不断地切换的，这里只要加上休眠 这上面每个线程打印出来的是空列表
            con.acquire()                  # 而只要将那段代码注释掉 则 每个线程打印的列表都会更新
            L.append(num)                 # 所以猜想 原因是 每个线程执行此方法到释放锁那里的时间 要小于 CPU切换的时间
            con.notify()
            con.release()
            time.sleep(3)

class Customer(threading.Thread):
    def __init__(self):
        super(Customer, self).__init__()

    def run(self):
        global L
        while True:
            con.acquire()
            if len(L)==0:
                con.wait()
            print("消费者",self.name,"消费"+str(L[0]),L)
            del (L[0])
            con.release()
            time.sleep(1)

if __name__ == "__main__":
    con = threading.Condition()
    Threads =[]
    L = []
    Threads.append(Customer())
    for i in range(5):
        Threads.append(Producer())
    for t in Threads:
        t.start()
    for t in Threads:
        t.join()
