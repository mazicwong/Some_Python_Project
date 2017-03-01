#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

path = input("输入一个路径")
for root, dirs, files in os.walk(path):
    for name in files:
        fname, fext = os.path.splitext(name)  # 用splitext分割文件名和扩展名
        os.rename(os.path.join(root, name), \
                  os.path.join(root, 'hdu ' + fname + fext))
