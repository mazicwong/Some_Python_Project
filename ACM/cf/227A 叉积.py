#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/22 12:59
# @Author  : mazicwong
# @File    : 227A 叉积.py

'''
本题输入三个点坐标，考察叉积，若大于0则right，小于0则left，等于0则towards
'''

ax,ay = map(int,input().split(' '))
bx,by = map(int,input().split(' '))
cx,cy = map(int,input().split(' '))
x1=ax-bx
y1=cx-bx
x2=ay-by
y2=cy-by
ans=x1*y2-x2*y1
if ans>0:
    print("RIGHT")
elif ans<0:
    print("LEFT")
else:
    print("TOWARDS")