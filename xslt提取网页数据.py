#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/12 16:39
# @Author  : mazicwong
# @File    : xslt提取网页数据.py
# https://zhuanlan.zhihu.com/p/20869884

'''
lxml是python的一个库，可以迅速、灵活地处理 XML。
提取集搜客官网旧版论坛的帖子标题和回复数，把整个列表提取出来，存成xml格式
'''
from urllib.request import urlopen
from lxml  import etree
url="http://www.gooseeker.com/cn/forum/7"
html = urlopen(url)
doc=etree.HTML(html.read())