# __author__ = 'admin'
# -*- coding: utf-8 -*-

import threading
import time


class producer(threading.Thread):
    def __init__(self, t_name):
        threading.Thread.__init__(self, name=t_name)

    def run(self):
        global x
        con.acquire()
        if x > 0:
            con.wait()
        else:
            for i in range(5):
                x += 1
                print('producing...', str(x))
            con.notify()
        print(x)
        con.release()


class consumer(threading.Thread):
    def __init__(self, t_name):
        threading.Thread.__init__(self, name=t_name)

    def run(self):
        global x
        con.acquire()
        if x == 0:
            print('consumer wait!')
            con.wait()
        else:
            for i in range(5):
                x -= 1
                print('consuming...', str(x))
            con.notify()
        print(x)
        con.release()

con = threading.Condition()
x = 0
print('start consumer')
c = consumer('consumer')
print('start producer')
p = producer('producer')

p.start()
c.start()
p.join()
c.join()
print(x)
