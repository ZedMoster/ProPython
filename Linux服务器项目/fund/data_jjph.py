#!/usr/bin/env python
# -*- coding: utf-8 -*-

from client.to_client import BaseClient
from ast import literal_eval
import pandas as pd
import requests
import datetime
import pymongo
import random
import json


class ttjj_jjph(BaseClient):
    '''
    获取 基金排行
    '''
    title = 'ttjj_jjph'
    now = datetime.datetime.now()
    strToday = str(now.strftime('%Y-%m-%d %H:%M:%S'))
    
    # 连接到 天天基金 数据库
    db_TTJJ = to_client()
    # 连接到 天天基金_rate 集合
    myDB = db_TTJJ["fund_jjph"]
    
    # 001 数据获取
    def getMoneyData(self):
        # print('-- loading ....')
        url = "http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&sd=2000-01-01&ed={}&pi=1&pn=20000".format(
            self.strToday)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "Referer"   : "http://fund.eastmoney.com/data/fundranking.html",
            "Host"      : "fund.eastmoney.com",
        }
        # 获取数据
        response = requests.get(url, headers=headers).text
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
                    "_id" : li[0],
                    "基金代码": li[0],
                    "基金名称": li[1],
                    "今日日期": li[3],
                    "单位净值": li[4],
                    "累计净值": li[5],
                    "日增长率": li[6],
                    "最近1周": li[7],
                    "最近1月": li[8],
                    "最近3月": li[9],
                    "最近6月": li[10],
                    "最近1年": li[11],
                    "最近2年": li[12],
                    "最近3年": li[13],
                    "今年以来": li[14],
                    "成立至今": li[15],
                    "成立日期": li[16],
                    "手续费" : li[20],
                    "是否可购": li[17],
                }
                allDataList.append(result)
        else:
            print("** {} is wrong data".format(self.title))
        # 数据导出相应文件格式
        return allDataList
    
    # 003 数据插入mongoDB
    def insertData(self, data=None):
        # 清空数据
        self.myDB.drop()
        # 插入最新数据
        x = self.myDB.insert_many(data)
        # print(x.inserted_ids)
        
        return True
    
    # 主函数
    def main(self):
        try:
            step_01 = self.getMoneyData()
            step_02 = self.dataFormat(step_01)
            step_03 = self.insertData(step_02)
            
            if step_03:
                print("-- {} pull the job off at {}".format(self.title,
                                                            self.strToday))
            else:
                print(
                    "-- {} wrong step_03  {}".format(self.title, self.strToday))
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    start = ttjj_jjph()
    # 获取基金大盘数据分析表格
    start.main()
