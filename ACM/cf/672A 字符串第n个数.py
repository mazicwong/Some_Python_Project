#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/22 15:11
# @Author  : mazicwong
# @File    : 672A 字符串第n个数.py

'''
字符串1234....
打印字符串的第n个数
'''
k=int(input())
n=''
x=1
while len(n)<1000:
    n+=str(x)
    x+=1
print(n[k-1])