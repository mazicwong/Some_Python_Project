#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/2 0:56
# @Author  : mazicwong
# @File    : 3.所有小URL初步信息去标签.py

import re
import os

for i in range(0, 180):  #180个大URL
    if os.path.exists(r"E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\%s" % i):  #已经有爬取结果的
        for cnt in (0,30):  #对爬取好的相似URL选取不大于30个html代码来去标签
            if os.path.isfile(r"E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\%s\%s.txt" % (i, cnt)):
                if not os.path.exists("E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\去标签后的\%s" % cnt):  # 创建一个文件夹
                    os.makedirs("E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\去标签后的\%s" % cnt)
                    with open(r'E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\%s\%s.txt' % (i, cnt), 'r') as file:
                        str = file.read()
                        str = '\n'.join(re.split(' +', str))
                        str = '\n'.join(re.split('\t+', str))
                        str = '\n'.join(re.split('\r+', str))
                        str = '\n'.join(re.split('&nbsp', str))
                        str = '\n'.join(re.split('\n+', str))
                        print(str)
                    with open(r"E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\去标签后的\%s\%s去标签.txt" % (i, cnt),"wb") as file1:  # 一般用双引号，单引号会出问题
                        file1.write(str)
                        # with open(r"E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\去标签后的\%s\%s_去标签.txt" % (i, cnt), "w") as file1:
                        #     file1.write(str)

