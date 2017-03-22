#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/22 15:35
# @Author  : mazicwong
# @File    : 675E DP+greedy.py

'''
英文： buy only tickets to stations from i+1 to ai inclusive (inclusive 表示包含在这个路段内的)

题意：有一个一条直线的地铁线路。给出a数组，在每个站点i只能买到去往[i+1, a[i]]内的票。
设p(i,j)为从i到j所需要的最少票数，求对所有ij的p(i,j)的和。（1=<i<j<=n）

思路：dp[i] 是从i到后面所有站点的最小票数和
当从一个站点i到不了所有点时，会到它能到的点中a[i]最大的点x。这时就能用到dp[x]。
其中自己能走i+1~x-1点，用x-i票
x能到x+1~n，用b[x]票
x能走的那些中，x+1 ~ a[i]是i自己能走的，把x走的当做自己走的，更远的要自己买票走到x，要n - a[i]张票
得到：dp[i] = x-i + dp[x] + n - a[i]
x能走的肯定比a[i]远，因为a[a[i]]肯定要大于a[i]
这样，我们要做的就是每次找出区间[i+1, a[i]]中a[x]最大的x
这可以用各种RMQ方法,不能用单调区间O(1)求，因为这个区间不是纯粹向左移动的，左界是一个个往左，右界是会来回动的。
所以可以维护一个只进不出的单调下降队列，然后用二分找。O(nlogn)

give:
n
a1,a2...an-1

使用：deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
说明http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431953239820157155d21c494e5786fce303f3018c86000
'''

from collections import deque


def argmax(que, z): #二分求[i+1, a[i]]中a[x]最大的x
    l = 0
    r = len(que) - 1
    while (l <= r):
        mid = int((l + r) / 2)
        x = que[mid]['i']
        if (x <= z):
            r = mid - 1
        else:
            l = mid + 1
    return que[l]['i']


def solve(n, A):
    a = [0] * (n + 1)
    a[1:] = A
    dp = [0] * (n + 1)
    dp[n - 1] = 1
    que = deque()
    que.append({'i': n - 1, 'a': a[n - 1]})
    for i in range(n - 2, 0, -1):
        if (a[i] >= n):
            dp[i] = n - i
        else:
            x = argmax(que, a[i])
            dp[i] = x - i + dp[x] + n - a[i]
        while (len(que) > 0 and que[-1]['a'] < a[i]):
            que.pop()
        que.append({'i': i, 'a': a[i]})
    return sum(dp)


n = int(input())
a = map(int, input().split(' '))
print(solve(n, a))
