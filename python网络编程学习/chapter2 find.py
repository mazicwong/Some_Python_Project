#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/12 16:13
# @Author  : mazicwong
# @File    : chapter2 find.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html, "html.parser")
# use findall to get a 'list' containing those only appeared in <span class="green"></span>
nameList = bs0bj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())
