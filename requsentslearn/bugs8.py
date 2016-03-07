# __author__ = 'admin'
# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import re


url = 'http://shop.freebuf.com/'
print "prepare&reading to read theweb"
data = urllib.urlopen(url).read()
# print data
print "parsing ... ... .. "
soup = BeautifulSoup(data)
# <div class="col-sm-6 col-md-4col-lg-4 mall-product-list">
itemlist = soup.findAll(name='div', attrs={'class': 'col-sm-6 col-md-4 col-lg-4 mall-product-list'})
for item in itemlist:
    print item.img["alt"] + " " + item.img["src"]

f = open("abc.txt", "w")
f.write(data)
f.close()
