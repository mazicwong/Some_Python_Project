#!user/bin/env python3
# -*- coding: gbk -*-
'''
Created on 2017年1月20日

@author: mazicwong
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, "html.parser")
images = soup.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
#一开始findall写成小写的,一直过不去....显示 TypeError: 'NoneType' object is not callable
for image in images:
    print(image["src"])




