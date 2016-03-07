# __author__ = 'admin'
# -*- coding: utf-8 -*-
"""
from threading import Thread, Lock

# define a global variable
some_var = 0
lock = Lock()


class IncrementThread(Thread):
    def run(self):
        # we want to read a global variable
        # and then increment it
        global some_var
        lock.acquire()
        read_value = some_var
        print("some_var in %s is %d" % (self.name, read_value))
        some_var = read_value + 1
        print("some_var in %s after increment is %d" % (self.name, some_var))
        lock.release()


def use_increment_thread():
    threads = []
    for i in range(50):
        t = IncrementThread()
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("After 50 modifications, some_var should have become 50")
    print("After 50 modifications, some_var is %d" % (some_var,))

use_increment_thread()
"""
"""
from threading import Thread
import time


class CreateListThread(Thread):
    def __init__(self):
        super(CreateListThread, self).__init__()
        self.entries = []

    def run(self):
        for i in range(10):
            time.sleep(0.1)
            self.entries.append(i)
        print(self.entries)


def use_create_list_thread():
    for i in range(3):
        t = CreateListThread()
        t.start()

use_create_list_thread()
"""
