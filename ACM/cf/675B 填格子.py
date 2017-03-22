#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/22 15:29
# @Author  : mazicwong
# @File    : 675B 填格子.py

'''
有个3*3的九宫格，每个格子能填1~n中任意的数（n由输入给出）。要求其中任意2*2的格子中4个数的和与其他各个2*2格子都相等
解法： 对中间的数进行枚举
'''


def solve():
    n, a, b, c, d = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        t = i + a + b
        if t - a - c > 0 and t - a - c <= n and t - c - d > 0 and t - c - d <= n and t - b - d > 0 and t - b - d <= n:
            ans += 1
    return ans * n


print(solve())
