# __author__ = 'admin'
# -*- coding: utf-8 -*-

import threading
my_lock = threading.RLock()
num = 0


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global num
        while True:
            my_lock.acquire()
            print('Thread(%s) locked, Number: %d' % (self.t_name, num))
            if num >= 4:
                my_lock.release()
                print('Thread(%s) released, Number: %d' % (self.t_name, num))
                break
            num += 1
            print('Thread(%s) released, Number: %d' % (self.t_name, num))
            my_lock.release()


def test():
    thread1 = myThread('A')
    thread2 = myThread('B')
    thread3 = myThread('C')
    thread1.start()
    thread2.start()
    thread3.start()

if __name__ == '__main__':
    test()
