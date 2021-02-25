# -*- coding: utf-8 -*-
import scrapy
from ..items import DyttItem
import re

class DySpider(scrapy.Spider):
    name = 'dy'
    start_urls = [
                  'https://www.dytt8.net/html/gndy/dyzz/index.html',
                  ]

    def parse(self, response):
        all_url = response.xpath('//table[@class="tbspan"]//a/@href').extract()
        for url in all_url:
            yield response.follow(url, callback=self.info)
        # 翻页
        pages_urls = response.xpath('//div[@class="x"]//@href').extract()
        for page in pages_urls:
            yield response.follow(page, callback = self.parse)
    def info(self,response):

        name = response.xpath('//div[@class="title_all"]/h1//text()').extract()[0]
        title = name.split('年')[-1].split('《')[-1].split('》')[0]
        code = name.split('年')[-1].split('《')[-1].split('》')[-1]
        #date = response.xpath('//div[@class="co_content8"]/ul/text()').extract()[0].strip().split('：')[-1]
        thunder = response.xpath('//div[@id="Zoom"]/span/a/@href').extract()

        nowUrl = response.request.url
        _id = re.findall("/(\d+).html", nowUrl)

        item = DyttItem()

        item['title'] = title
        item['code'] = code
        #item['date'] = date
        item['thunder'] = thunder
        item['_id'] = _id
        yield item
