#!user/bin/env python3
# -*- coding: gbk -*-
'''
Created on 2017年1月25日

@author: mazicwong
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages=set()
random.seed(datetime.datetime.now())

#获取页面所有內链的列表
def getInternalLinks(bsObj,includeUrl):
    internalLinks=[]  #list,可变长
    #找到所有以'/'开头的连接
    for link in bsObj.findAll("a",href=re.compile("^(/|.*)"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

#获取页面所有外链的列表
def getExternalLinks(bsObj,excludeUrl):
    externalLinks=[]
    #找出所有以"http"或者"www"开头企鹅不含当前url的连接
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks
    
def splitAddress(address):
    addressParts=address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bsObj=BeautifulSoup(html,"html.parser")
    externalLinks=getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks=getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]
    
def followExternalOnly(startingSite):
    externalLink=getRandomExternalLink("http://oreilly.com")
    print("随机外链是: "+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")
    
    
    
    
    
    
    
    