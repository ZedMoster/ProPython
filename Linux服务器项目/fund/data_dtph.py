# coding:utf-8
from to_client import *
from ast import literal_eval
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
import requests
import datetime
import pymongo
import random
import re
import json


class ttjj_dtph():
    '''
    获取 定投排行
    '''
    title = 'ttjj_dtph'
    now = datetime.datetime.now()
    strToday = str(now.strftime('%Y-%m-%d %H:%M:%S'))

    #连接到 天天基金 数据库
    db_TTJJ = to_client()
    # 连接到数据库
    myCol = db_TTJJ["fund_dtph"]

    # 获取基金ID
    fund_id = get_id()

    #001 数据获取
    def getMoneyData(self, _id=None):
        # print('-- loading....')

        url = "http://fund.eastmoney.com/api/Dtshph.ashx?t=0&c=yndt&s=desc&issale=0&page=1&psize=20000"
        # url = "http://fund.eastmoney.com/api/Dtshph.ashx?t=0&c=yndt&s=desc&issale=0&page=1&psize=5"
        headers = {
        "Referer": "http://fund.eastmoney.com/fundguzhi.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Host": "fund.eastmoney.com",
        }

        #获取数据
        response = requests.get(url, headers=headers, timeout=10).text

        soup = etree.HTML(response)
        all_data = soup.xpath('//tbody/tr')

        return all_data

    # 002 数据格式化
    def dataFormat(self, data=None, _id=None):
        allDataList = []

        if data != None:
            for soup in data:
                li = soup.xpath("td//text()")
                dt = soup.xpath("td[14]/a")[0].get("title")
                if dt == None:
                    dt_num = '1'
                else:
                    dt_num = '0'
                today = str(self.now.strftime('%Y-')) + li[7]
                result = {
                    "_id": li[0],
                    "基金代码": li[1],
                    "基金名称": li[2],
                    "单位净值": li[6],
                    "今日日期": today,
                    "近1年定投收益": li[8],
                    "近2年定投收益": li[9],
                    "近3年定投收益": li[10],
                    "近5年定投收益": li[11],
                    "上海证券评级": li[12],
                    "手续费": li[13],
                    "是否可购": dt_num,
                }
                allDataList.append(result)
        else:
            print("** {} is wrong data".format(self.title))

        # 数据导出相应文件格式
        return allDataList

    #003 数据插入mongoDB
    def insertData(self, data=None):
        self.myCol.drop()
        x = self.myCol.insert_many(data)
        # print(x.inserted_ids)
        return True

    #主函数
    def main(self):

        step_01 = self.getMoneyData()
        step_02 = self.dataFormat(step_01)
        step_03 = self.insertData(step_02)

        if step_03:
            print("-- {} pull the job off at {}".format(self.title,self.strToday))
        else:
            print("-- {} wrong step_03  {}".format(self.title,self.strToday))

if __name__ == '__main__':
    start = ttjj_dtph()
    #获取基金大盘数据分析表格
    start.main()





