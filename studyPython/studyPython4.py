__author__ = 'admin'
# -*- coding: utf-8 -*-


old_str = "friend"
new_str = "f"

f = open("E:/python/abc", 'r+')
"""
while True:
    line = f.readline()

    if old_str in line:
        line_pos = f.tell() - len(line) - 1
        f.seek(line_pos)
        new_line = line.replace(old_str, new_str)
        f.writelines(new_line)
        break
"""

for line in f.readlines():
    print(line, end='')
f.close()
