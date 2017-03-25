#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/25 22:50
# @Author  : mazicwong
# @File    : 爬取相似url.py

import urllib.request


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


def getSimilarHtml(url, cnt):
    List = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    cnt *= -1
    # 处理url...先转到list，然后再转回去string..好像有点麻烦..if you really want to hah
    url = list(url)  # 转到list才可以处理(change the value)
    Len = len(url)
    for i in range(Len - 1, -1, -1):
        try:
            if ((url[i] in List) and (url[i + 1] in List)):
                url[i] = int(url[i])
                if (url[i] > 2):
                    url[i] -= 1
                else:
                    url[i] += 1
                url[i] = str(url[i])
                url = ''.join(url)  # 转回string
                getHtml(url, cnt)
                print("url查找成功")
                break
        except:
            print("url查找出错")


# 获取该url数据，分为获取本身和相似url
def getUrl():
    with open(r"E:\泰迪杯\C题样例数据\All_html 相似url\url.txt", "r") as file:
        urlList = file.readlines()
        cnt = 1
        for url in urlList:
            getHtml(url, cnt)
            getSimilarHtml(url, cnt)
            cnt += 1


def main():
    getUrl()


if __name__ == "__main__":
    main()
