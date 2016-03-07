# __author__ = 'admin'
# -*- coding: utf-8 -*-

import time
import _thread


def timer(no, interval):
    cnt = 0
    while cnt < 5:
        print("Thread:(%d) Time:%s" % (no, time.ctime()))
        time.sleep(interval)
        cnt += 1
    _thread.exit_thread()


def test():
    _thread.start_new_thread(timer, (1, 1))
    _thread.start_new_thread(timer, (2, 2))
    _thread.start_new_thread(timer, (3, 3))


if __name__ == '__main__':
    test()




