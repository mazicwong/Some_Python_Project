#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/25 12:44
# @Author  : mazicwong
# @File    : 数据爬取(未处理).py

import urllib.request

#按顺序放入txt
def saveFile(data, cnt):
    path = r'E:\泰迪杯\C题样例数据\All_html\out%s.txt' % cnt
    f = open(path, 'wb')
    f.write(data)
    f.close()


# 保存爬取不了的网页下来分析
def saveFail(url, cnt):
    path = r'E:\泰迪杯\C题样例数据\All_html\fail.txt'
    f = open(path, 'ab+')
    f.write(cnt + '  ' + url)
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
