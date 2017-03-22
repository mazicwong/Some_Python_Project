#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/22 15:00
# @Author  : mazicwong
# @File    : 227B.py

'''
n
a1,a2...an
q
b1,b2...bq
'''
n = int(input())
mylist = input().split(' ')
i = 0
zid = {}
for x in mylist:
    zid[x] = i
    i += 1
q = int(input())
m = input().split(' ')
ans1 = 0
ans2 = 0
for y in m:
    tmp = zid[y]
    ans1 += tmp + 1
    ans2 += n - tmp
print(ans1, ans2)
