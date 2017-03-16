#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 0:22
# @Author  : mazicwong
# @File    : re过滤html标签.py



from html.parser import HTMLParser
from bs4 import BeautifulSoup
from urllib import request
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

url = "http://x.heshuicun.com/forum.php?mod=viewthread&tid=80"
html = request.urlopen(url)
bsObj = BeautifulSoup(html)
strip_tags(bsObj)