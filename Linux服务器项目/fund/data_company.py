#!/usr/bin/env python
# -*- coding: utf-8 -*-

from client.to_client import BaseClient
import requests
import datetime
import pymongo


class FundCompany(BaseClient):
    '''基金公司'''
    
    def __init__(self):
        # col
        self._db = BaseClient.get_db(db_name="fund_data", col_name="fund_id")
        # 名称
        self._title = FundCompany.__name__
        # 时间戳
        self._time = BaseClient.get_time()
    
    # 001 数据获取
    def get_company(self):
        # print('-- loading ....')
        url = "http://fund.eastmoney.com/Data/FundRankScale.aspx"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "Referer": "http://fund.eastmoney.com/data/fundranking.html",
            "Host": "fund.eastmoney.com",
        }
        # 获取数据
        response = requests.get(url, headers=headers).text
        data = response.split('[[')[1].strip(']]}').split('],[')
        
        return data
    
    # 002 数据格式化
    def data_Format(self, data=None):
        allDataList = []
        if data != None:
            for company in data:
                li = company.split(',')
                try:
                    l777 = float(li[7].strip("'"))
                except:
                    l777 = 0.00
                
                result = {
                    "基金公司_id": li[0].strip("'"),
                    "基金公司": li[1].strip("'"),
                    "成立日期": li[2].strip("'"),
                    "基金数量": li[3].strip("'"),
                    "总经理": li[4].strip("'"),
                    "管理规模": l777,
                    "天相评级": li[8].strip("'"),
                    "数据日期": li[11].strip("'"),
                }
                allDataList.append(result)
        else:
            print("** {} is wrong data".format(self.title))
        # 数据导出相应文件格式
        return allDataList
    
    # 003 数据插入mongoDB
    def insert_Data(self, data=None):
        self.myCol.drop()
        x = self.myCol.insert_many(data)
        # print(x.inserted_ids)
        
        return True
    
    # 主函数
    def main(self):
        step_01 = self.get_company()
        step_02 = self.data_Format(step_01)
        step_03 = self.insert_Data(step_02)
        
        if step_03:
            print("-- {} pull the job off at {}"
                  .format(self._title, self._time))
        else:
            print("-- {} wrong step_03  {}"
                  .format(self._title, self._time))


if __name__ == '__main__':
    start = ttjj_company()
    # 获取基金大盘数据分析表格
    start.main()
