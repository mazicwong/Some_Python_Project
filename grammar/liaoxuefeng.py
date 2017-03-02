#!/usr/bin/env python
# _*_ coding:utf-8 _*_

print('this is', 'a learning', 'process')
name = input("input your name : ")
a = input("input your age : ")
age = int(a)
print('hello: %s , %d ' % (name, age))  # 用%中间不用逗号...it is not C

# ****常用数据类型****#
# list [] 数组 append(),insert(1,'ma'),pop(),
classmates = ['mazic']
classmates.append('cpp')
print(classmates[-1])
classmates.pop()
L = list(range(100)) #共0~99
L = L[3:10:2] #第三到第十个数,每两个取一次(这种切片操作可用于list,tuple,str)
# tuple () 定长数组 =>就是比较安全而已

for name in classmates:  # for name in range(101)
    print(name)
for i,value in enumerate(['A','B','C']):
    print(i,value)

# dict 字典(即map),一组key+value
d = {'mazic': 100, 'java': 6, 'cpp': 99}
# set 一组key,但是没有重复的key #add(3),remove(4)
s = set([1, 2, 3])
ss

#from 库 import 函数