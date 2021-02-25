import scrapy


class EastmoneySpider(scrapy.Spider):
    name = 'eastmoney'
    allowed_domains = ['fund.eastmoney.com']
    start_urls = ['http://fund.eastmoney.com/']

    def parse(self, response):
        pass
