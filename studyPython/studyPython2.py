__author__ = 'admin'
# -*- coding: utf-8 -*-


def multipliers():
	return [lambda x: i * x for i in range(4)]

print([m(2) for m in multipliers()])

# 输出结果为 [6, 6, 6, 6]
"""
原因是 Python 的闭包的后期绑定导致的 late binding，这意味着在闭包中的变量是在内部函数被调用的时候被查找。
所以结果是，当任何 multipliers() 返回的函数被调用，在那时，i 的值是在它被调用时的周围作用域中查找，到那时，
无论哪个返回的函数被调用，for 循环都已经完成了，i 最后的值是 3，因此，每个返回的函数 multiplies 的值都是 3。
因此一个等于 2 的值被传递进以上代码，它们将返回一个值 6 （比如： 3 x 2）
"""

# 修改如下
# 1.创建一个闭包，通过使用默认参数立即绑定它的参数。例如：


def multipliers():
	return [lambda x, i=i: i * x for i in range(4)]

print([m(2) for m in multipliers()])

# 2.使用 functools.partial 函数：

from functools import partial
from operator import mul


def multipliers():
	return [partial(mul, i) for i in range(4)]

print([m(2) for m in multipliers()])
