#!/usr/bin/env python
# coding=utf-8

import scrapy
from scrapy.selector import Selector
from jnuxshc.items import JnuxshcItem
from scrapy.http import Request


class xzhc(scrapy.Spider):
    name = 'xzhc'  #最后要调用的名字
    start_urls=['https://news.jnu.edu.cn/xshc/ll/']
    url = 'https://jnu.edu.cn'

    def parse(self, response):  # response即网页数据
        item = JnuxshcItem()
        selector = Selector(response)
        articles = selector.xpath('//*[@id="content"]/div[1]/ul/li') 
        print("huangzhiqihuangzhiqi-----")

        for article in articles:
            #if article.xpath('@class/text()').extract()
            title = article.xpath('div[2]/div[1]/a/text()').extract()
            time = article.xpath('div[2]/div[3]/text()').extract()
            intro = article.xpath('div[2]/div[2]/text()').extract()
            print('--------------------------------------------------------')
            print(title)

            item['title'] = title
            item['time'] = time
            item['intro'] = intro

            yield item
        
        #因为有很多页,所以要递归调用
        tmp_url = 'https://news.jnu.edu.cn/'
        next_link = selector.xpath('//*[@class="pager"]/a[@class="next"]/@href').extract()
        if next_link[0] != '/xshc/ll/List_1.html':
            next_link = tmp_url+next_link[0]
            yield Request(next_link,callback=self.parse) #回调函数为self.parse

