import randomname
__author__ = 'admin'
# -*- coding: utf-8 -*-

# 排序集合

# 地精排序：最简单的排序 最坏情况下为O(n2)  最好情况为O(n)  平均情况为O(n2)  空间复杂度为O(1)

"""
def gnome_sort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1

seq = random.sample(range(0, 300), 10)
print("Origin: ", seq)
gnome_sort(seq)
print("After sort:", seq)
"""

# 冒泡排序：下沉排序  最坏情况下为O(n2)  最好情况为O(n)  平均情况为O(n2)  空间复杂度为O(1)

"""
def bubble_sort(seq):
    for i in range(0, len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] >= seq[j]:
                seq[i], seq[j] = seq[j], seq[i]

seq = random.sample(range(0, 300), 10)
print("Origin: ", seq)
bubble_sort(seq)
print("After sort:", seq)
"""

# 插入排序 最坏情况下为O(n2)  最好情况为O(n)  平均情况为O(n2)  空间复杂度为O(1)

"""
def insert_sort(seq):
    for i in range(1, len(seq)):
        tmp = seq[i]
        j = i
        while j > 0 and tmp < seq[j-1]:     # 这里不能用range  否则会一直循环到j为0  或者使用break
            seq[j] = seq[j-1]
            j -= 1
        seq[j] = tmp

seq = random.sample(range(0, 300), 10)
print("Origin: ", seq)
insert_sort(seq)
print("After sort:", seq)
"""

# 选择排序 最坏情况下为O(n2)  最好情况为O(n2)  平均情况为O(n2)  空间复杂度为O(1)

"""
def select_sort(seq):
    for i in range(0,len(seq)):
        tmp = i
        for j in range(i+1, len(seq)):
            if seq[tmp] > seq[j]:
                tmp = j
        seq[tmp], seq[i] = seq[i], seq[tmp]

seq = random.sample(range(0, 300), 10)
print("Origin: ", seq)
select_sort(seq)
print("After sort:", seq)
"""

# 快速排序 最坏情况下为O(n2)  最好情况为O(n log n)  平均情况为O(n log n)  空间复杂度为O(log n)

"""
def sub_sort(seq, low, high):
    key = seq[low]
    while low < high:
        while low < high and seq[high] >= key:
            high -= 1
        while low < high and seq[high] < key:
            seq[low] = seq[high]
            low += 1
            seq[high] = seq[low]
    seq[low] = key
    return low


def quick_sort(seq, low, high):
    if low < high:
        key_index = sub_sort(seq, low, high)
        quick_sort(seq, low, key_index)
        quick_sort(seq, key_index + 1, high)

seq = random.sample(range(0, 300), 10)
print("Origin: ", seq)
quick_sort(seq, 0, len(seq) - 1)
print("After sort:", seq)
"""

# shell 排序


def shell_sort(seq):
    length = len(seq)
    inc = 0
    while inc <= length / 3:
        inc = inc * 3 + 1
    while inc >= 1:
        for i in range(inc, length):
            tmp = seq[i]
            for j in range(i, 0, -inc):
                if tmp < seq[j - inc]:
                    seq[j] = seq[j - inc]
                else:
                    j += inc
                    break
            seq[j - inc] = tmp
        inc //= 3

seq = randomname.sample(range(0, 300), 10)
print("Origin: ", seq)
shell_sort(seq)
print("After sort:", seq)

