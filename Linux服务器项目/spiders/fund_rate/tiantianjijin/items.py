# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TiantianjijinItem(scrapy.Item):
    基金代码 = scrapy.Field()
    基金名称 = scrapy.Field()

    基金类型 = scrapy.Field()
    基金规模 = scrapy.Field()
    基金经理 = scrapy.Field()
    成立日期 = scrapy.Field()
    管理公司 = scrapy.Field()

    最近1周_k = scrapy.Field()  # 最近一周
    最近1月_k = scrapy.Field() # 最近一月
    最近3月_k = scrapy.Field() # 最近三月
    最近6月_k = scrapy.Field() # 最近六月
    最近1年_k = scrapy.Field()  # 最近一年
    最近2年_k = scrapy.Field()  # 最近二年
    最近3年_k = scrapy.Field()  # 最近三年
    今年以来_k = scrapy.Field() # 今年以来

    #持仓数据
    股票持仓 = scrapy.Field()
    股票名称 = scrapy.Field()
    持仓比例 = scrapy.Field()
    涨跌幅度 = scrapy.Field()
    前十持仓比例 = scrapy.Field()
    持仓截止日期 = scrapy.Field()

    # 债券持仓 = scrapy.Field()
    # 债券名称 = scrapy.Field()
    # 持仓占比_q = scrapy.Field()
    # 涨跌幅度_q = scrapy.Field()
