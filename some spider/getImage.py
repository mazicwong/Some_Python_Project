#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
python正则表达式

用\d匹配数字
用.匹配任意字符
用\s匹配一个空格
用*表示任意个数字符
用+表示至少一个字符
http://www.jianshu.com/p/e0eb4635aa07
'''
import urllib.request
from urllib.request import urlopen
from urllib.request import urlretrieve
import re
import datetime
from bs4 import BeautifulSoup


def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla / 5.0(WindowsNT6.3;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 56.0.2924.87Safari / 537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh - CN, zh;q = 0.8',
        'Connection': 'close',
        'Referer': None  # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
    }
    req=urllib.request.Request(url,headers=headers)#为了伪装成浏览器
    page = urlopen(req)
    html = page.read()
    html = html.decode('UTF-8')  # 3.X的参数改了,read()这里要用decode,不然会出错
    return html


def getImg(html):
    splitReg = r'[\s\"]+'
    tempList = re.split(splitReg, html)  # 用正则表达式分割后获得一个list
    imgUrls = []

    x = 0
    for str in tempList:
        matchReg = r'http:.*.jpg'
        if re.match(matchReg, str):
            print('%s--' % x + str)
            imgUrls.append(str)
            x = x + 1
            urlretrieve(str, '%s %s.jpg' % (datetime.datetime.now().date(), x))  # 下载url的文件
        matchReg1 = r'http:.*.png'
        if re.match(matchReg1, str):
            print('%s--' % x + str)
            imgUrls.append(str)
            x = x + 1
            urlretrieve(str, '%s %s.jpg' % (datetime.datetime.now().date(), x))

    return imgUrls


url = "http://cn.bing.com/images/search?q=%E6%85%B5%E6%87%92%E5%B0%91%E5%A5%B3%E5%86%99%E7%9C%9F&FORM=ISTRTH&id=A87C17F9A484F4078C72BEB0FE1EC509BA1F59C8&cat=%E7%BE%8E%E5%A5%B3&lpversion="
# url = input("input the website you want to download: ")
html = getHtml(url)
print(html)
getImg(html)
