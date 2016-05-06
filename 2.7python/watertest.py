# __author__ = 'admin'
# -*- coding: utf-8 -*-


def calculate(testcase):
    p_l = 0
    p_r = len(testcase) - 1
    max_l = testcase[p_l]
    max_r = testcase[p_r]

    volume = 0
    list_r = []
    while p_r > p_l:
        if max_l < max_r:
            p_l += 1
            if testcase[p_l] >= max_l:
                max_l = testcase[p_l]
                list_r.append(volume)
                volume = 0
            else:
                volume = volume + (max_l - testcase[p_l])
        else:
            p_r -= 1
            if testcase[p_r] >= max_r:
                max_r = testcase[p_r]
                list_r.append(volume)
                volume = 0
            else:
                volume = volume + (max_r - testcase[p_r])
    list_r.sort()
    print list_r
    return list_r[-1]


case = [2, 5, 1, 6, 1, 2, 1, 7, 5, 6]
l = calculate(case)
print l
