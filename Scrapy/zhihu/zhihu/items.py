# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class ZhihuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    KeyWord = Field()
    Topic_name = Field()
    Topic_id = Field()
    Question_id = Field()
    Question_content = Field()
    Content = Field()  #内容

