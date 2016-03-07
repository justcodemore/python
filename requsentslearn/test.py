# __author__ = 'admin'
# -*- coding: utf-8 -*-
score = raw_input('please write your score:')
score = int(score)
if score >= 90:
    print 'excellent'
elif score >= 80:
    print 'good'
elif score >= 60:
    print 'passed'
else:
    print 'failed'

f = lambda a: a+2
print f(2)

