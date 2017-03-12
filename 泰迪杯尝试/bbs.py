#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/12 16:55
# @Author  : mazicwong
# @File    : bbs.py
# datas = file('result_sample.txt').readlines()

from urllib import request
from bs4 import BeautifulSoup
import re

url = "http://x.heshuicun.com/forum.php?mod=viewthread&tid=80"
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
    'Referer': r'http://x.heshuicun.com/forum.php?mod=viewthread&tid=80',
}
req = request.Request(url, headers=headers)
page = request.urlopen(req).read()
# page = page.decode('utf-8')


# html = urlopen(url)
# page = html.read()
# bs0bj = BeautifulSoup(html, "html.parser")
# print(html)
# pattern = re.compile(r"^\d{4}(-\d\d){2} \d\d(:\d\d){2}")
# match = pattern.match('2015-05-22 17:43:50')
# mmm = re.match(r"^\d{4}(-\d\d){2} \d\d(:\d\d){2}",page)
# print (match.group())
