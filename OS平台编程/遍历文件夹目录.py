#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

#打印所有文件的目录
path = input("输入一个需要打印的路径")
#os.walk 很常用,用来遍历一个目录,返回三元组  (路径,目录名,文件名)
for root, dirs, files in os.walk(path):
    for name in files:
        print(os.path.join(root, name)) #os.path.join可以将路径和名字结合起来形成绝对路径
