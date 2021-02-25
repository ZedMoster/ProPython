# -*- coding: utf-8 -*-
from to_client import get_id
from ..items import TiantianjijinItem
import scrapy
import pymongo
import datetime
import pandas as pd
import re


class TtjjSpider(scrapy.Spider):
    #爬虫名称 - 基金评级
    name = 'ttjj'
    #创建访问的地址列表
    today = datetime.datetime.today()
    strToday = str(today.strftime('%Y-%m-%d'))

    # 连接到 天天基金 数据库
    _id = get_id()
    # 连接到数据库

    url_list = []
    # 创建地址
    for code in _id:
        url = "http://fund.eastmoney.com/{}.html".format(code["基金代码"])
        url_list.append(url)
    #初始化url
    start_urls = url_list

    def parse(self, response):
        # 传入items grade
        items = TiantianjijinItem()

        # 获取基金代码
        nowUrl = response.request.url
        code = re.findall("\d+", nowUrl)

        # 基本信息
        try:
            tips_0 = response.xpath('//*[@id="body"]//div[@style="float: left"]/text()').extract()
            tips_1 = response.xpath('//div[@class="infoOfFund"]//tr[1]/td[1]/a/text()').extract()
            tips_2 = response.xpath('//div[@class="infoOfFund"]//tr[1]/td[2]/text()').extract()
            tips_3 = response.xpath('//div[@class="infoOfFund"]//tr[1]/td[3]/a/text()').extract()
            tips_4 = response.xpath('//div[@class="infoOfFund"]//tr[2]/td[1]/text()').extract()
            tips_5 = response.xpath('//div[@class="infoOfFund"]//tr[2]/td[2]/a/text()').extract()
        except:
            print('**基本信息获取错误')

        # 四分位排名
        try:
            type1 = response.xpath('//*[@id="increaseAmount_stage"]//tr[6]/td[2]/h3/text()').extract()
            type2 = response.xpath('//*[@id="increaseAmount_stage"]//tr[6]/td[3]/h3/text()').extract()
            type3 = response.xpath('//*[@id="increaseAmount_stage"]//tr[6]/td[4]/h3/text()').extract()
            type4 = response.xpath('//*[@id="increaseAmount_stage"]//tr[6]/td[5]/h3/text()').extract()
            type5 = response.xpath('//*[@id="increaseAmount_stage"]//tr[6]/td[6]/h3/text()').extract()
            type6 = response.xpath('//*[@id="increaseAmount_stage"]//tr[6]/td[7]/h3/text()').extract()
            type7 = response.xpath('//*[@id="increaseAmount_stage"]//tr[6]/td[8]/h3/text()').extract()
            type8 = response.xpath('//*[@id="increaseAmount_stage"]//tr[6]/td[9]/h3/text()').extract()
        except:
            print('**四维等级获取错误')

        items["基金代码"] = code
        items["基金名称"] = tips_0

        items["基金类型"] = tips_1
        items["基金规模"] = tips_2
        items["基金经理"] = tips_3
        items["成立日期"] = tips_4
        items["管理公司"] = tips_5

        items["最近1周_k"] = type1
        items["最近1月_k"] = type2
        items["最近3月_k"] = type3
        items["最近6月_k"] = type4
        items["最近1年_k"] = type6
        items["最近2年_k"] = type7
        items["最近3年_k"] = type8
        items["今年以来_k"] = type5

        yield items