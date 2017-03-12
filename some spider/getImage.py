#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
import os

root = "D://pics//"
url = "http://imgsize.ph.126.net/?enlarge=true&imgurl=http://edu-image.nosdn.127.net/73946898DEFC4EEE8B934F5DA131B905.jpg?imageView&amp;thumbnail=426y240&amp;quality=100_230x130x1x95.png"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        # 图片是二进制格式,把图片保存为文件
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("successfully saving")
    else:
        print ("The file is already existing")
except:
    print("a faulty operation ")