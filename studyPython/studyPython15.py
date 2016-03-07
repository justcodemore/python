# __author__ = 'admin'
# -*- coding: utf-8 -*-
"""
from time import ctime
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now(x):
    print(ctime(), x)

now('abc')
print(now.__name__)
try:
    raise ValueError('abc')

except ValueError as e:
    print(e)
"""
"""
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
try:
    s.score = 9999
except ValueError as e:
    print(e)
"""

import randomname

L = ['张嘉辉', '阿黄', '胡胜龙', '阿达', '我']

x = randomname.choice(L)
print(x)
