# __author__ = 'admin'
# -*- coding: utf-8 -*-
# import webbrowser as wb
import os
import platform
import subprocess


def open_file(path):
    if platform.system() == "Windows":
        subprocess.call(r'explorer \\192.168.64.89', shell=True)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

# wb.open(r'\\192.168.64.89\周报\2015年\第49周')

open_file(1)
