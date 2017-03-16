#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/16 19:35
# @Author  : mazicwong
# @File    : 百度提交关键词.py

import requests
kv = {'wd': 'python'}
r = requests.get("http://www.baidu.com/s", params=kv)
print(len(r.text))
