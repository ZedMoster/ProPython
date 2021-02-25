# coding:utf-8
from scrapy.cmdline import execute
import datetime

def crawl_lsjz():
    # 服务器端
    # execute(["scrapy", "crawl", "rate"])
    execute(["scrapy", "crawl", "lsjz", "--nolog"])

if __name__ == '__main__':
    now = datetime.datetime.now()
    strToday = str(now.strftime('%Y-%m-%d %H:%M:%S'))
    
    print ("-- good job lsjz start at : " + strToday)
    crawl_lsjz()
    
