# __author__ = 'admin'
# -*- coding: utf-8 -*-
"""
from time import ctime, sleep


def test(name, num):
    print('%s begin %s' % (name, ctime()))
    sleep(num)
    print('%s end %s' % (name, ctime()))
    return name


thread = ['th1', 'th2', 'th3', 'th4', 'th5']
num_list = range(1, 5)
results = map(test, thread, num_list)
for i in results:
    print('-->', i)
"""

import randomname
from time import time, sleep
from multiprocessing.dummy import Pool as ThreadPool
import threading
lock = threading.Lock()
cnt = []


def test(url):
    x = randomname.randint(1, 10)
    print(url, x)
    # lock.acquire()
    sleep(x)
    global cnt
    cnt.append(x)
    # lock.release()

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    # etc..
    ]

for i, j in enumerate(urls):
    print(i, j)

t = time()

# Make the Pool of workers
pool = ThreadPool(5)
# Open the urls in their own threads
# and return the results
results = pool.map(test, urls)
# close the pool and wait for the work to finish
pool.close()
pool.join()

t = time() - t
print(t)
print(cnt, sum(cnt))
