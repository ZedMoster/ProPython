# coding:utf-8
from ast import literal_eval
from to_client import to_client
import pandas as pd
import requests
import datetime
import pymongo
import random
import json


class ttjj_jjjl():
    '''
    获取 基金经理
    '''
    title = 'ttjj_jjjl'
    now = datetime.datetime.now()
    strToday = str(now.strftime('%Y-%m-%d %H:%M:%S'))

    # 连接到 天天基金 数据库
    db_TTJJ = to_client()
    # 连接到数据库
    myCol = db_TTJJ["fund_jjjl"]

    #001 数据获取
    def getMoneyData(self):
        # print('-- loading ....')
        #dx = 1 可购买
        url = "http://fund.eastmoney.com/Data/FundDataPortfolio_Interface.aspx?dt=14&mc=returnjson&ft=all&pn=3000&pi=1&sc=abbname&st=asc"
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Referer": "http://fund.eastmoney.com/data/fundranking.html",
        "Host": "fund.eastmoney.com",
        }
        #获取数据
        response = requests.get(url, headers=headers).text
        data = response.split('{')[1].split('}')[0].split(',record')[0].strip('datas:')
        new_list = literal_eval(data)
        return new_list

    # 002 数据格式化
    def dataFormat(self, data=None):
        allDataList = []
        if data != None:
            for li in data:
                if li[10].strip('亿元') == '--':
                    l100 = 0.0
                else:
                    l100 = float(li[10].strip('亿元'))
                if li[7].strip('%') == '--':
                    l777 = 0.0
                else:
                    l777 = float(li[7].strip('%'))

                result = {
                    "基金经理_id": li[0],
                    "基金经理": li[1],
                    "基金公司_id": li[2],
                    "所属公司": li[3],
                    "管理基金_id": li[4],
                    "现任基金": li[5],
                    "从业时间": int(li[6]),
                    "现任基金最佳回报": l777,
                    "基金代码": li[8],
                    "基金名称": li[9],
                    "现任基金总规模": l100,
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
    jijinjingli = ttjj_jjjl()
    #获取基金大盘数据分析表格
    jijinjingli.main()

