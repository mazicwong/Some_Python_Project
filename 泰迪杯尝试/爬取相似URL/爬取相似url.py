#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/25 22:50
# @Author  : mazicwong
# @File    : 爬取相似url.py

import urllib.request
import re
import os
from bs4 import BeautifulSoup


# 按顺序放入txt
def saveFile(data, cnt):
    path = r'E:\泰迪杯\C题样例数据\All_html 相似url\out%s.txt' % cnt
    f = open(path, 'wb')
    f.write(data)
    f.close()


# 保存爬取不了的网页下来分析
def saveFail(url, cnt):
    path = r'E:\泰迪杯\C题样例数据\All_html 相似url\fail.txt'
    f = open(path, 'a+')
    f.write('%d   %s' % (cnt, url))
    f.close()


def getHtml(url, cnt):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    }
    req = urllib.request.Request(url=url, headers=headers)
    try:
        response = urllib.request.urlopen(req, timeout=2)
        html = response.read()
        print('第%s个论坛爬取成功' % cnt)
        saveFile(html, cnt)
    except:
        print('sorry! 第%s个论坛爬取失败' % cnt)
        saveFail(url, cnt)


# 以下:获得主页url   http://www.baidu.com/abc/cc  ==>>  www.baidu.com
def get_root_url(url):
    m = url.split('//')
    if len(m) == 2:
        root_url = m[1]
    else:
        root_url = m[0]
    tt = root_url.split('/')
    root_url = tt[0]
    root_url = r'http://' + root_url
    return root_url


# 获得主页html
def get_root_html(url):
    # 以下:get主页url   http://www.baidu.com/abc/cc  ==>>  www.baidu.com
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    }
    try:
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req, timeout=4)
        html = response.read()
        return html
    except:
        print("出错了")


# 传入url，返回匹配的re
def get_re(url):
    url = url[7:]  # 去除http://
    Len = len(url)
    p = "http://"  # 这里不能用r,因为在下面str->bytes的时候\d会变成\\d
    i = 0
    while i < Len:
        if url[i] == '.':
            p += '.'
        elif 'a' <= url[i] <= 'z':  # 不能直接判isplpha，因为str[i]中全都是字符
            p += '[a-z]'
        elif 'A' <= url[i] <= 'Z':  #http://www.shdxlt.cn/ShowPost.asp?ThreadID=144952
            p += '[A-Z]'
        elif '0' <= url[i] <= 'z':
            p += '\d'
        else:
            p += url[i]
        i += 1
    return p


# def getSimilarHtml(url, cnt):
#     List = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     cnt *= -1
#     # 处理url...先转到list，然后再转回去string..好像有点麻烦..if you really want to hah
#     url = list(url)  # 转到list才可以处理(change the value)
#     Len = len(url)
#     for i in range(Len - 1, -1, -1):
#         try:
#             if ((url[i] in List) and (url[i + 1] in List)):
#                 url[i] = int(url[i])
#                 if (url[i] > 2):
#                     url[i] -= 1
#                 else:
#                     url[i] += 1
#                 url[i] = str(url[i])
#                 url = ''.join(url)  # 转回string
#                 getHtml(url, cnt)
#                 print("url查找成功")
#                 break
#         except:
#             print("url查找出错")


# 获取该url数据，分为获取本身和相似url
def getUrl():
    with open(r"E:\泰迪杯\C题样例数据\All_html 相似url\bbs_urls.txt", "r") as file:
        urlList = file.readlines()
        cnt = 1
        for url in urlList:
            path = r'E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\out%s.txt' % cnt  # 用来判断文件是否已经存在
            if os.path.isfile(path):  # 存在且不为空就退出
                # if os.stat("out%s.txt" % cnt).st_size == 0
                cnt += 1
            else:
                root_url = get_root_url(url)  # 获得主页URL
                root_html = get_root_html(root_url)  # 获得主页html
                p1 = get_re(url)  # 获取正则表达式
                p1 = p1.encode(encoding='utf-8')  # str => bites (for the use of re.compile)
                p1 = p1[:-1]  # 去掉换行符
                pat = re.compile(p1)  # 编译正则表达式
                List = re.findall(pat, root_html)
                print("第%s个:%s个结果" % (cnt, len(List)))
                path = r"E:\泰迪杯\C题样例数据\All_html 相似url\爬取结果\out%s.txt" % cnt
                with open(path, "w") as f:
                    for i in List:
                        i = i.decode()  # 把b''decode掉，bytes=>string
                        i = str(i)
                        f.write(i)
                        f.write('\n')
                cnt += 1


def main():
    getUrl()


if __name__ == "__main__":
    main()
