# __author__ = 'admin'
# -*- coding: utf-8 -*-
import re
import string


def bleed(num):
    l = re.findall(r'[0-9]', str(num))
    a = l.pop()
    a = string.atoi(a)
    for i in l:
        l1 = l[:]
        l1.remove(i)
        for j in l1:
            l2 = l1[:]
            l2.remove(j)
            b = l2[0]

            x = string.atoi(b)
            y = string.atoi(i)
            z = string.atoi(j)

            if num == (a * 10 + x) * (y * 10 + z):
                print a, x, '*',
                print y, z, '=',
                print num
                return
            if num == (x * 10 + a) * (z * 10 + y):
                print x, a, '*',
                print z, y, '=',
                print num
                return


if __name__ == "__main__":
    for num in range(1000, 9999, 1):
        if num / 100 != 0:
            bleed(num)
