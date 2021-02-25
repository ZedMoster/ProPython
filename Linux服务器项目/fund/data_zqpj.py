# coding:utf-8
from to_client import to_client
from ast import literal_eval
from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime
import pymongo
import re
import json


class ttjj_zqpj():
    '''
    获取 证券排行
    '''
    title = 'ttjj_zqpj'
    now = datetime.datetime.now()
    strToday = str(now.strftime('%Y-%m-%d %H:%M:%S'))

    # 连接到 天天基金 数据库
    db_TTJJ = to_client()
    # 连接到数据库
    myCol = db_TTJJ["fund_zqpj"]

    #001 数据获取
    def getMoneyData(self):
        # print('-- loading ....')
        url = "http://fund.eastmoney.com/data/fundrating.html"
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Referer": "http://fund.eastmoney.com/data/fundranking.html",
        "Host": "fund.eastmoney.com",
        }

        #获取数据
        response = requests.get(url, headers=headers, timeout=10).text
        soup =BeautifulSoup(response, features="lxml")
        data = soup.find_all(id="fundinfo")
        # print(type(data[0]))
        # print(data[0])
        txt = re.findall('fundinfos = "(.*?)"; var JG_1_pjrq', str(data[0]))[0]

        return txt

    # 002 数据格式化
    def dataFormat(self, data=None):
        allDataList = []
        if data != None:
            dateList = data.split("_")
            for li in dateList:
                li = li.split("|")
                result = {
                    "基金代码": li[0],
                    "基金名称": li[1],
                    "基金类型": li[2],
                    "基金经理": li[3],
                    "基金经理_id": li[4],
                    "公司简称": li[5],
                    "基金公司_id": li[6],
                    "5星评价": li[7],
                    "上海证券": li[12],
                    "招商证券": li[14],
                    "济安金信": li[16],
                    "手续费": li[18],
                    "是否可购": li[20],

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
            print("-- {} pull the job off at {}".format(self.title, self.strToday))
        else:
            print("-- {} wrong step_03  {}".format(self.title, self.strToday))

if __name__ == '__main__':
    start = ttjj_zqpj()
    #获取基金大盘数据分析表格
    start.main()





