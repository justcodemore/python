# __author__ = 'admin'
# -*- coding: utf-8 -*-

import urllib
import re
import os
import time
from bs4 import BeautifulSoup


def getHtml(url):
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page.read())
    htmllist = soup.findAll(name='a', attrs={'href': re.compile("^https?://")})
    for url in htmllist:
        print url['href']
    getImg(soup)


def getImg(html):
    imglist = html.findAll(name='img', attrs={'src': re.compile("(\.jpg)$")})
    x, y = 0, 0
    print "downloading"
    for imgurl in imglist:
        name = re.split('/', imgurl['src'])[-1]
        isexist = 'f:/picture/' + name
        if name.__len__() > 90:
            continue
        if os.path.exists(isexist):
            print "%s is done before" % name
            y += 1
        else:
            print "%s is done" % name
            urllib.urlretrieve(imgurl['src'], 'f:/picture/%s' % name)
            x += 1
            if x % 100 == 0:
                time.sleep(1)
                print "%d has done" % x
                continue
    print "Total :%d items is done ; %d itmes done before" % (x, y)


getHtml("http://tieba.baidu.com/p/2460150866")
data = None
headers = {
'content-type': 'application/json',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}


