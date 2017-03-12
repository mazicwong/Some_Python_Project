#!user/bin/env python3
# -*- coding: gbk -*-
'''
Created on 2017年1月20日

@author: mazicwong
'''

# ctrl+shift+F 可以用来格式化保存后的python代码

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs0bj = BeautifulSoup(html.read(),"edtvghtml.parser")
        title = bs0bj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("This could not be found")
else:
    print(title)
    