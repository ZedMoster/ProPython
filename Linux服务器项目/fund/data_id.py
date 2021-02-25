#!/usr/bin/env python
# -*- coding: utf-8 -*-

from client.to_client import BaseClient
from ast import literal_eval
import pandas as pd
import requests
import datetime
import pymongo
import json


class FundId(BaseClient):
    '''基金代码'''
    
    def __init__(self):
        # col
        self._db = BaseClient.get_db(db_name="fund_data", col_name="fund_id")
        # 名称
        self._title = FundId.__name__
        # 时间戳
        self._time = BaseClient.get_time()
    
    def get_money_data(self):
        '''数据获取'''
        
        url = "http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&sd=2000-01-01&ed={}&pi=1&pn=20000&" \
            .format(self._time)
        headers = {
            "Referer": "http://fund.eastmoney.com/data/fundranking.html",
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        }
        # 获取数据
        response = requests.get(url, headers=headers)
        data = response.text \
            .split('{')[1].split('}')[0].split(',allRecords')[0].strip('datas:')
        new_list = literal_eval(data)
        return new_list
    
    def data_format(self, data=None):
        '''数据格式化'''
        all_data = []
        if data:
            for i in data:
                li = i.split(',')
                result = {
                    "基金代码": li[0],
                    "基金名称": li[1],
                }
                all_data.append(result)
        else:
            print("** {} is wrong data".format(self._title))
        # 数据导出相应文件格式
        return all_data
    
    def insert_data(self, data=None):
        '''数据插入mongoDB'''
        
        self._db.drop()
        x = self._db.insert_many(data)
        # print(x.inserted_ids)
        return True
    
    # 主函数
    def main(self):
        step_01 = self.get_money_data()
        step_02 = self.data_format(step_01)
        step_03 = self.insert_data(step_02)
        
        if step_03:
            print("-- {} pull the job off at {}"
                  .format(self._title, self._time))
        else:
            print("-- {} wrong step_03  {}"
                  .format(self._title, self._time))


if __name__ == '__main__':
    id = FundId()
    # 获取基金大盘数据分析表格
    id.main()
