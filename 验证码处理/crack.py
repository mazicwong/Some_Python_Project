#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 16:21
# @Author  : mazicwong
# @File    : crack.py

from PIL import Image
im = Image.open("Code.png")
im = im.convert("P") #converting an “RGB” image to an 8-bit palette image
print (im.histogram()) #打印颜色直方图
#发现很多白点，每个点是256色，最后一个显示920，说明有920个白色像素
his = im.histogram()
values={}
for i in range(255):
    values[i] = his[i]

#排序得到有用的颜色，发现 211，741  这个就是我们要的验证码的红色部分了
for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:
    print(j,k)


#构造黑白二值图片
im2 = Image.new("P",im.size,255)

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix == 1 or pix ==2:
            im2.putpixel((y,x),0)

im2.show()

