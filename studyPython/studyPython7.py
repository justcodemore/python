# __author__ = 'admin'
# -*- coding: utf-8 -*-

import _thread
import time

my_lock = _thread.allocate_lock()
num = 0


def add_num(name):
    global num
    while True:
        my_lock.acquire()

        print('Thread %s locked! num=%s' % (name, str(num)))
        if num >= 5:
            print('Thread %s released! num=%s' % (name, str(num)))
            my_lock.release()
            _thread.exit_thread()
        num += 1
        print('Thread %s released ! num=%s' % (name, str(num)))
        time.sleep(2)
        my_lock.release()


def test():
    _thread.start_new_thread(add_num, ('B',))
    _thread.start_new_thread(add_num, ('A',))
    _thread.start_new_thread(add_num, ('C',))

if __name__ == '__main__':
    test()
