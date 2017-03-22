#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/22 15:16
# @Author  : mazicwong
# @File    : 675A.py
'''
给出a，b，c，求是否a加若干个c能得到b，是就输出YES，否就输出NO
解答： (b-a)%c==0
'''

a, b, c = map(int, input().split(' '))
if ((a != b and c == 0) or (b > a and c < 0)):
    print("NO")
elif ((a == b) or (b > a and c > 0 and ((b - a) % c == 0)) or (a > b and c < 0 and ((a - b) % c == 0))):
    print("YES")
else:
    print("NO")
