#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/28 0:15
# @Author  : mazicwong
# @File    : 去除换行+空格.py

'''
源码编码判断用chardet，取出换行和空格用strip
'''

import re

# s = "as, \n asdas   \n       \n   \n  \n\nasda"
# print(s)
# print(".............")
# s = ''.join(re.split(' +', s))
# s = '\n'.join(re.split('\n+', s))
# print(s)
# print ('\n'.join(re.split(' +',s)))


with open(r'C:\Users\ASUS\Desktop\66out-1.txt', 'r') as file:
    str = file.read()
    str = '\n'.join(re.split(' +', str))
    str = '\n'.join(re.split('\t+', str))
    str = '\n'.join(re.split('\r+', str))
    str = '\n'.join(re.split('&nbsp', str))
    str = '\n'.join(re.split('\n+', str))
    print(str)

file1 = open(r'C:\Users\ASUS\Desktop\666-1.txt', 'w')
file1.write(str)
file1.close()
