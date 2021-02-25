# -*- coding: utf-8 -*-
import scrapy
from ..items import FlacItem


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['sq688.com']
    start_urls = ['https://www.sq688.com/']

    def parse(self, response):
        if response != None:
            for i in range(30000):
            # for i in range(10):
                url = 'https://www.sq688.com/download/{}.html'.format(i)
                yield response.follow(url,callback=self.pandownload)

    def pandownload(self, response):
        # 唯一的ID值
        nowUrl = response.request.url.split('/')[-1]
        _id = []
        _id.append(nowUrl)
        # 初始化item方法
        item = FlacItem()
        # 提取需要的数据
        name = response.xpath('//div[@class="dcenter"]//h2/text()').extract()
        author = response.xpath('//a[@class="signame"]/text()').extract()
        down = response.xpath('//p[@class="downurl"]/text()').extract()
        # 传递数据到item
        item['name'] = name
        item['author'] = author
        item['_id'] = _id
        item['down'] = down
        # 循环
        yield item


