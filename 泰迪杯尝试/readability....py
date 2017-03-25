#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/24 23:27
# @Author  : mazicwong
# @File    : readability....py

import requests
from readability import Document
response = requests.get('http://www.bbsmax.com/A/kmzLB4DX5G/')
doc = Document(response.text)
print (doc.title())
print (doc.summary())