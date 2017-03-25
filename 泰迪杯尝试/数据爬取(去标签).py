#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/25 15:53
# @Author  : mazicwong
# @File    : 数据爬取(去标签).py

# 用正则表达式简单过滤html的标签
import re


def filter_tags(htmlstr):
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 处理换行
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('\n', s)  # 将br转换为换行
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  # 去掉HTML注释
    # 去掉多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    s = replaceCharEntity(s)  # 替换实体
    return s


##替换常用HTML字符实体.
# 使用正常的字符替换HTML中特殊的字符实体.
# 你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
# @param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                     'lt': '<', '60': '<',
                     'gt': '>', '62': '>',
                     'amp': '&', '38': '&',
                     'quot': '"''"', '34': '"', }

    re_charEntity = re.compile(r'&#?(?P<name>\w+);')
    sz = re_charEntity.search(htmlstr)
    while sz:
        entity = sz.group()  # entity全称，如>
        key = sz.group('name')  # 去除&;后entity,如>为gt
        try:
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
        except KeyError:
            # 以空串代替
            htmlstr = re_charEntity.sub('', htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
    return htmlstr


def repalce(s, re_exp, repl_string):
    return re_exp.sub(repl_string, s)


'''
def saveFile(news,cnt):
    path = r'E:\泰迪杯\C题样例数据\All_html 去标签\out%s.txt' % cnt
    file = open(path, 'w+')
    file.write(news)
    file.close()

if __name__ == '__main__':
    for cnt in range(1, 178):
        try:
            path1 = r'E:\泰迪杯\C题样例数据\All_html\out%s.txt' % cnt
            file = open(path1, 'r')
            text = file.read()
            news = filter_tags(text)
            saveFile(news,cnt)
            file.close()
        except:
            print("第%s文件不存在"%cnt)
'''


def saveFile(news, cnt):
    path = r'E:\泰迪杯\C题样例数据\All_html 相似url\66out%d.txt' % cnt
    file = open(path, 'w+')
    file.write(news)
    file.close()


#UnicodeDecodeError: 'gbk' codec can't decode byte 0xaf in position 641: illegal multibyte sequence
#上面在liaoxuefeng提到了，可以直接忽略他

if __name__ == '__main__':
    for cnt in [1,-1]:
        try:
            path1 = r'E:\泰迪杯\C题样例数据\All_html 相似url\out%s.txt' % cnt
            #读取一直错误。。改了半个小时终于改成功了
            #把下面mode = 'r' 改成 'rb', 因为r的时候读进来是gbk..但是也不知道为什么转换不了。。直接读二进制文件吧
            #明天再把编码问题好好看一看
            #第二个改动是decode('utf-8')
            file = open(path1, 'rb')
            text = file.read().decode('utf-8')
            news = filter_tags(text)
            saveFile(news, cnt)
            file.close()
        except:
            print("第%s文件不存在" % cnt)
