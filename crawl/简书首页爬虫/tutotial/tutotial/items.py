# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class TutotialItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    author = Field()
    time = Field()
    '''
    url = Field()
    readNum = Field()
    commentNum = Field()
    likeNum = Field()
    '''
