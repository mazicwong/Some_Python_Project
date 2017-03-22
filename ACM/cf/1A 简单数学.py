#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/22 0:53
# @Author  : mazicwong
# @File    : 1A 简单数学.py

'''
give : n,m,a     a retangle with n*m and use how many square with a*a to patch up with it
(can be overlap)
http://blog.csdn.net/chenguolinblog/article/details/12190689
'''

myList = input().split()
n=int(myList[0])
m=int(myList[1])
a=int(myList[2])

print((n//a+(n%a>0))*(m//a+(m%a>0)))