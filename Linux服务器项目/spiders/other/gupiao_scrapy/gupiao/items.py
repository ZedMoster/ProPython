# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GupiaoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    code = scrapy.Field()
    market = scrapy.Field()
    dk_total = scrapy.Field()

    date_time = scrapy.Field()
    jin_kai = scrapy.Field()
    zui_xin = scrapy.Field()
    zui_gao = scrapy.Field()
    zui_di = scrapy.Field()
    turnover_L = scrapy.Field()
    turnover_E = scrapy.Field()
    amplitude = scrapy.Field()




