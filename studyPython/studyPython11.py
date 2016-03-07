# __author__ = 'admin'
# -*- coding: utf-8 -*-

import threading
import time

exitFlag = 0


class myThread (threading.Thread):   # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        # threading.Thread.__init__(self)
        super(myThread, self).__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):                   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        threadLock.release()
        print("Exiting " + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

thread1.join()

print("Exiting Main Thread")
