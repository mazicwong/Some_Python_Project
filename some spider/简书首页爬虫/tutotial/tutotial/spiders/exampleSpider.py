# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from tutotial.items import TutotialItem


class Example(scrapy.Spider):
    name = 'example'
    start_urls=['http://www.jianshu.com']
    url = 'http://www.jianshu.com'

    def parse(self, response):  # response即网页数据
        item = TutotialItem()
        selector = Selector(response)
        articles = selector.xpath('//*[@id="list-container"]/ul/li')
        print("huangzhiqihuangzhiqi-----")

        for article in articles:
            title = article.xpath('div/a/text()').extract()
            author = article.xpath('div/div[1]/div/a[1]/text()').extract()
            time = article.xpath('div/div[1]/div/span/@data-shared-at').extract()
            print('--------------------------------------------------------')
            print(author)

            item['title'] = title
            item['author'] = author
            item['time'] = time

            yield item

