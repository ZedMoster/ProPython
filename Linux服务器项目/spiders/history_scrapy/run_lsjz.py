# coding:utf-8
from scrapy.cmdline import execute
import datetime

def crawl_lsjz():
    # 服务器端
    # execute(["scrapy", "crawl", "lsjz"])
    execute(["scrapy", "crawl", "lsjz", "-s", "LOG_FILE=log.log"])

if __name__ == '__main__':
    now = datetime.datetime.now()
    strToday = str(now.strftime('%Y-%m-%d %H:%M:%S'))
    
    print ("-- good job lsjz start at:" + strToday)
    crawl_lsjz()
    
