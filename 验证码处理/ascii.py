#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 17:13
# @Author  : mazicwong
# @File    : ascii.py


from PIL import Image

# 图片路径/名称
path = "char1.png"
# 字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# RGB值转字符的函数
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    im = Image.open(path)
    #WIDTH, HEIGHT = im.size
    WIDTH, HEIGHT = 80,80
    print(WIDTH, HEIGHT)
    im = im.resize((HEIGHT, WIDTH), Image.NEAREST)  # 使用最近滤波
    txt = ""
    for h in range(HEIGHT):
        for w in range(WIDTH):
            txt += get_char(*im.getpixel((w, h)))
        txt += '\n'
    print(txt)

    with open("output.txt", "w") as f:
        f.write(txt)
