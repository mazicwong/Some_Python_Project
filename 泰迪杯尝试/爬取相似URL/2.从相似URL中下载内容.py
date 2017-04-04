#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/2 0:09
# @Author  : mazicwong
# @File    : 2.从相似URL中下载内容.py

import os
import urllib.request


def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    }
    try:
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req, timeout=2)
        html = response.read()
        return html
    except:
        print("there must be somthing wrong when crawing")


def main():
    for cnt in range(1, 171):
        with open("E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\out%s.txt" % cnt, "r") as file:
            List = file.readlines()
            if len(List) != 0:
                if not os.path.exists("E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\%s" % cnt):  # 创建一个文件夹
                    os.makedirs("E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\%s" % cnt)
                    for i in range(0, len(List)):
                        if i > 20:
                            break
                        with open(r"E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\%s\%s.txt" % (cnt, i), "wb") as f:
                            f.write(getHtml(List[i]))
                            print("第%s个小的url处理成功" % i)
                    print("第%s个URL处理成功" % cnt)


if __name__ == "__main__":
    main()
