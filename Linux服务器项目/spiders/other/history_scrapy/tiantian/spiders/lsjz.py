# -*- coding: utf-8 -*-
import scrapy
from ..items import TiantianItem
from to_client import get_id
import pymongo
import json
import re


class LsjzSpider(scrapy.Spider):
    name = 'lsjz'

    # 连接到 天天基金 数据库
    _id = get_id()
    # 连接到数据库

    url_list = []
    # 创建地址
    for code in _id:
        # url = "http://api.fund.eastmoney.com/f10/lsjz?callback=&fundCode={}&pageIndex=1&pageSize=20000".format(code["基金代码"])

        # 第一次运行上面的地址数据
        # 后面你每天定时运行只需获取最近的十条数据即可
        url ="http://api.fund.eastmoney.com/f10/lsjz?callback=&fundCode={}&pageIndex=1&pageSize=100".format(code["基金代码"])
        url_list.append(url)

    #初始化url
    start_urls = url_list

    def parse(self, response):
        # 获取基金代码
        nowUrl = response.request.url
        code = re.findall("fundCode=(\d+)", nowUrl)

        dic = json.loads(response.text)
        data = dic['Data']['LSJZList']

        items = TiantianItem()

        if data != None:
            for li in data:
                items['基金代码'] = code

                items['净值日期'] = li['FSRQ']
                items['单位净值'] = li['DWJZ']
                items['累计净值'] = li['LJJZ']
                items['日增长率'] = li['JZZZL']
                items['申购状态'] = li['SGZT']
                items['赎回状态'] = li['SHZT']
                items['分红送配'] = li['FHSP']

                yield items
