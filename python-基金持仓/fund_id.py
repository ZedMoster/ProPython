#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fund_client_mongoDB import to_client
from ast import literal_eval
import pandas as pd
import requests
import datetime
import pymongo
import json


class ttjj_id():
    '''
    获取 基金代码
    '''
    title = 'ttjj_id'
    now = datetime.datetime.now()
    strToday = str(now.strftime('%Y-%m-%d %H:%M:%S'))
    
    # 连接到 天天基金 数据库
    _db = to_client()
    # 连接到数据库
    my_Col = _db["fund_id"]
    
    # 001 数据获取
    def getMoneyData(self):
        # print('-- loading ....')
        url = "http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&sd=2000-01-01&ed={}&pi=1&pn=20000&".format(
            self.strToday)
        headers = {
            "Referer"   : "http://fund.eastmoney.com/data/fundranking.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        }
        # 获取数据
        response = requests.get(url, headers=headers, ).text
        data = response.split('{')[1].split('}')[0].split(',allRecords')[
            0].strip('datas:')
        new_list = literal_eval(data)
        return new_list
    
    # 002 数据格式化
    def dataFormat(self, data=None):
        allDataList = []
        if data != None:
            for i in data:
                li = i.split(',')
                result = {
                    "基金代码": li[0],
                    "基金名称": li[1],
                }
                allDataList.append(result)
        else:
            print("** {} is wrong data".format(self.title))
        # 数据导出相应文件格式
        return allDataList
    
    # 003 数据插入mongoDB
    def insertData(self, data=None):
        # 清空数据
        self.my_Col.drop()
        # 插入最新数据
        x = self.my_Col.insert_many(data)
        # print(x.inserted_ids)
        return True
    
    # 主函数
    def main(self):
        step_01 = self.getMoneyData()
        step_02 = self.dataFormat(step_01)
        step_03 = self.insertData(step_02)
        
        if step_03:
            print("-- {} pull the job off at {}".format(self.title,
                                                        self.strToday))
        else:
            print("-- {} wrong step_03  {}".format(self.title, self.strToday))


if __name__ == '__main__':
    start = ttjj_id()
    # 获取基金大盘数据分析表格
    start.main()
