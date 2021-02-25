# coding:utf-8
from scrapy.cmdline import execute
import datetime

def crawl_rate():
    # 服务器端
    # execute(["scrapy", "crawl", "ttjj", "--nolog"])
    # # 本地端
    execute(["scrapy", "crawl", "ttjj"])

    # # 输出内容保存log
    # execute(["scrapy", "crawl", "ttjj", "-s", "LOG_FILE=log.log"])
    

if __name__ == '__main__':
    now = datetime.datetime.now()
    strToday = str(now.strftime('%Y-%m-%d %H:%M:%S'))
    
    print ("-- good job rate start at : " + strToday)
    crawl_rate()
    
    
