#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/25 13:12
# @Author  : mazicwong
# @File    : 1.py

import urllib.request


def saveFile(data, cnt):
    path = r'E:\泰迪杯\C题样例数据\All_html\out%s.txt' % cnt
    f = open(path, 'wb')
    f.write(data)
    f.close()


def getHtml(url, cnt):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    }
    # opener = urllib.request.build_opener()
    # opener.addheaders = [headers]
    # html = opener.open(url).read()

    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req, timeout=2)
    html = response.read()
    # print(html)
    saveFile(html, cnt)


def getUrl():
    file = open(r"E:\泰迪杯\C题样例数据\All_html\url.txt", "r")
    urlList = file.readlines()
    cnt = 1
    for url in urlList:
        getHtml(url, cnt)
        cnt += 1


def main():
    getUrl()


if __name__ == "__main__":
    main()
