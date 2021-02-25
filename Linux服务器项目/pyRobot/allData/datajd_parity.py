#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import datetime
import json
import time
import re


def to_time(timeStamp):
    '''
    格式化时间戳
    
    :param timeStamp: 时间戳
    :return: %Y-%m-%d
    '''
    timeStr = re.findall('\d{10}', timeStamp)[0]
    timeArray = time.localtime(int(timeStr))
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime


def jd_response(msg):
    '''
    京东数据比价
    :param msg:
    :return:
    '''
    byword = msg.strip('比价').strip().split("?")[0]
    if byword == '':
        return '✨商品地址【https://item.jd.com/6212482.html】\n' \
               '✨只需输入:比价 https://item.jd.com/6212482.html'
    else:
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; google Pixel 2 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 mmbWebBrowse',
        }
        url = 'http://api.lanrenbijia.com/ChromeWidgetServices/WidgetServices.ashx?methodName=getBiJiaInfo_weixin&jsoncallback=&p_url={}'.format(
                byword)
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            data = json.loads(r.text)
            spName = data['title']
            currentPriceStatus = data['currentPriceStatus']
            lowerPrice = data['lowerPrice']
            lowerDate = to_time(data['lowerDate'])
            now = datetime.datetime.now()
            strToday = str(now.strftime('%Y-%m-%d'))
            
            word = '商品名称:{}\n商品地址:{}\n' \
                   '--------------------------------------------\n' \
                   '时间:{} 价格分析:{}\n' \
                   '时间:{} 最低金额:{}(元)\n' \
                   '--------------------------------------------'.format(
                    spName, byword, strToday, currentPriceStatus, lowerDate,
                    lowerPrice, )
            return word
        else:
            return "数据获取失败....稍后重试！"


if __name__ == '__main__':
    li = jd_response(
            '比价 https://item.m.jd.com/product/100009074814.html?wxa_abtest=a&utm_user=plusmember&gx=RnFmxGVRbzWKwtQUqoRyW2PTGnN2pZU&ad_od=share&utm_source=androidapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL')
    print(li)
