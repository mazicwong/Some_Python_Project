#!user/bin/env python3
# -*- coding: gbk -*-

'''
Created on 2017年1月24日

@author: mazicwong
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()  # 用集合set可以去掉重复的URL

def getLinks(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org/" + pageUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    try:
        print(bsObj.h1.get_text())
        #print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("页面缺少一些属性! 不过不用担心...")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:  #在上面查找的链接中,但是不在已经有的链接中
                # 当遇到新的页面时
                newPage = link.attrs["href"]
                print("--------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")
