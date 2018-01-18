#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
kv = {'wd':'Python'}
q = requests.get("http://www.baidu.com/s",params = kv)

q.status_code
def get_URL(url):
    try:
        r=requests.get(url,timeout=30)
        print(r.encoding)
        r.raise_for_status()
        r.enconding=r.apparent_encoding
        return r.text[:1000]
    except:
        return "there must be a wrong"

if __name__=="__main__":
    url="https://detail.tmall.com/item.htm?spm=a223c.8145724.1110321729.1.Qz7Kic&acm=lb-zebra-175981-1643283.1003.4.1365015&id=537259409492&scm=1003.4.lb-zebra-175981-1643283.ITEM_537259409492_1365015"
    print(get_URL(url))
