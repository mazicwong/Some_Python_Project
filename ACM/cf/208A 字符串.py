#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 22:44
# @Author  : mazicwong
# @File    : 208A 字符串.py
# 将原字符串中的“WUB”子串去掉
'''
input()输入string，如果要读一个数字的话，要用int（）转为数字 int(input())
a = str.split(sss) 将原串按sss进行分割，然后存到的到子串存到一个集合当中
eg: str ="a$b$c"  a = str.split('$') a=[a,'',b,'',c]
'''


print (input().replace('WUB', ' '))

'''
str = input()
str.encode('UTF-8')
a = []
a = str.split('WUB')
for t in a:
    if t != '':
        print(t, end=' ')#print默认\n结尾，给换成空格就好
'''

