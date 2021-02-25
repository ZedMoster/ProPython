# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TiantianItem(scrapy.Item):
    基金代码 = scrapy.Field()

    净值日期 = scrapy.Field()
    单位净值 = scrapy.Field()
    累计净值 = scrapy.Field()
    日增长率 = scrapy.Field()
    申购状态 = scrapy.Field()
    赎回状态 = scrapy.Field()
    分红送配 = scrapy.Field()
