# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import GupiaoItem

class GpSpider(scrapy.Spider):
    name = 'gp'
    allowed_domains = ['eastmoney.com']

    url_list = []
    for i in range(50):
    # for i in range(2):
        url = 'http://90.push2.eastmoney.com/api/qt/clist/get?&pn={}&pz=100&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f12,f13'.format(str(i))
        url_list.append(url)
    start_urls = url_list

    def parse(self, response):
        data = json.loads(response.text)
        try:
            diff = data['data']['diff']

            for i in range(100):
            # for i in range(1):
                i = str(i)
                code = diff[i]['f12']
                market = diff[i]['f13']

                url = 'http://3.push2his.eastmoney.com/api/qt/stock/kline/get?&secid={}.{}&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&klt=101&fqt=0&end=20500101&lmt=20000'.format(market,code)

                yield response.follow(url, callback=self.evety_gp)

        except Exception as e:
            print(e)

    def evety_gp(self,response):
        item = GupiaoItem()
        data = json.loads(response.text)

        name = data['data']['name']
        code = data['data']['code']
        market = data['data']['market']
        dk_total = data['data']['dktotal']

        klines = data['data']['klines']
        for k in klines:

            every = k.split(',')
            date_time = every[0]
            jin_kai = float(every[1])
            zui_xin = float(every[2])
            zui_gao = float(every[3])
            zui_di = float(every[4])
            turnover_L = float(every[5])
            turnover_E = float(every[6])
            amplitude = float(every[7])

            item['name'] = name
            item['code'] = code
            item['market'] = market
            item['dk_total'] = dk_total
            item['date_time'] = date_time
            item['jin_kai'] = jin_kai
            item['zui_xin'] = zui_xin
            item['zui_gao'] = zui_gao
            item['zui_di'] = zui_di
            item['turnover_L'] = turnover_L
            item['turnover_E'] = turnover_E
            item['amplitude'] = amplitude

            yield item