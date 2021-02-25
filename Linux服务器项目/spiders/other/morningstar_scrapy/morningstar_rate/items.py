# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MorningstarRateItem(scrapy.Item):
    # 代码 名称
    code = scrapy.Field()
    # 分类
    classify = scrapy.Field()
    # 成立日期
    setupday = scrapy.Field()
    # 开放日期
    openday = scrapy.Field()
    # 申购状态
    isBuy = scrapy.Field()
    # 赎回状态
    rede = scrapy.Field()
    # 投资风格
    base = scrapy.Field()
    # 总净资产
    total = scrapy.Field()
    # 最低投资
    Mini = scrapy.Field()
    # 前端收费
    front = scrapy.Field()

