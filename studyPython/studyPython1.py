__author__ = 'admin'
# -*- coding: utf-8 -*-


def extendlist(val, lista=[]):
    lista.append(val)
    return lista

list1 = extendlist(10)
list2 = extendlist(123, [])
list3 = extendlist('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)
"""
# 输出结果为：
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
# 原因：新的默认列表仅仅只在函数被定义时创建一次。随后当 extendList 没有被指定的列表参数调用的时候，其使用的
是同一个列表。这就是为什么当函数被定义的时候，表达式是用默认参数被计算，而不是它被调用的时候。

"""

"""
#修改如下
def extendlist(val, lista=None):
    if lista is None:
        lista = []
    lista.append(val)
    return lista

list1 = extendlist(10)
list2 = extendlist(123)
list3 = extendlist('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)
"""