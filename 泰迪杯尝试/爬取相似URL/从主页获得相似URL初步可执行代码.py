#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/25 22:50
# @Author  : mazicwong
# @File    : 1.爬取相似url(最终).py

import urllib.request
import re
import os
from bs4 import BeautifulSoup


# 获得主页html
def get_root_html(url):
    # 在主页下面get新的html
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    }
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req, timeout=2)
    html = response.read()
    return html


def get_re(url):
    url = url[7:]  # 去除http://
    Len = len(url)
    p = "http://"
    i = 0
    while i < Len:
        if url[i] == '.':
            p += '.'
        elif 'a' <= url[i] <= 'z':  # 不能直接判isplpha，因为str[i]中全都是字符
            p += '[a-z]'
        elif '0' <= url[i] <= 'z':
            p += '\d'
        else:
            p += url[i]
        i += 1
    return p


# 获取该url数据，分为获取本身和相似url
def main():
    with open(r"E:\泰迪杯\C题样例数据\All_html 相似url\bbs_urls.txt", "r") as file:
        urlList = file.readlines()
        cnt = 1
        # path = r'E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果' #用来判断文件是否已经存在
        for url in urlList:
            # if os.path.isfile('out%s.txt'%cnt): #存在且不为空就退出
            #     if os.
            #         cnt +=1
            #         continue

            # 以下:get主页url   http://www.baidu.com/abc/cc  ==>>  www.baidu.com
            m = url.split('//')
            if len(m) == 2:
                root_url = m[1]
            else:
                root_url = m[0]
            tt = root_url.split('/')
            root_url = tt[0]
            root_url = r'http://' + root_url
            # getHtml(url, cnt)
            # print(root_url)
            root_html = get_root_html(root_url)  # 获得主页html
            p1 = get_re(url)  # 获取正则表达式
            # print(p1)
            # print(type(p1))
            p1 = p1.encode(encoding='utf-8')  # it can help transfer the "string" to "bytes"
            p1 = p1[:-1]  #去掉换行符
            # print(p1)
            # print(type(p1))
            pat = re.compile(p1)  # 编译正则表达式
            List = re.findall(pat, root_html)
            print(len(List))
            # for i in List:
            #     print(i)
            path = r"E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\out%s.txt" % cnt
            with open(path, "w") as f:
                for i in List:
                    i = i.decode()
                    i = str(i)
                    f.write(i)
                    f.write('\n')
            cnt += 1


if __name__ == "__main__":
    main()
