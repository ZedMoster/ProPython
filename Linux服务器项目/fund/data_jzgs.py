# coding:utf-8
from to_client import to_client
import requests
import datetime
import pymongo
import random
import json


class ttjj_jzgs():
    '''
    获取 净值估算
    '''
    title = 'ttjj_jzgs'

    now = datetime.datetime.now()
    strToday = str(now.strftime('%Y-%m-%d %H:%M:%S'))

    # 连接到 天天基金 数据库
    _db = to_client()
    # 连接到数据库
    my_Col = _db["fund_jzgs"]

    #001 数据获取
    def getMoneyData(self):
        # print('-- loading ....')

        url = "http://api.fund.eastmoney.com/FundGuZhi/GetFundGZList?type=1&sort=3&orderType=desc&canbuy=0&pageIndex=1&pageSize=20000"
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Referer": "http://fund.eastmoney.com/data/fundranking.html",
        "Host": "fund.eastmoney.com",
        }

        #获取数据
        response = requests.get(url, headers=headers, timeout=8).text
        data_json = response.split('"Data":')[1].split(',"ErrCode":0')[0]

        # with open("a.json", "w+",encoding="utf-8") as f:
        #     f.writelines(a)

        data =json.loads(data_json)

        # print(data["list"][0])

        return data["list"]

    # 002 数据格式化
    def dataFormat(self, data=None):
        allDataList = []

        if data != None:
            for li in data:
                result = {
                    "_id": li['bzdm'],
                    "基金代码": li['bzdm'],
                    "基金名称": li['jjjc'],
                    "今日日期": li['gxrq'],
                    "今日估值": li['gsz'],
                    "估增长率": li['gszzl'],
                    "今日单位净值": li['gbdwjz'],
                    "今日日增长率": li['jzzzl'],
                    "估算偏差": li['gspc'],
                    "上一日日期": li['gzrq'],
                    "上一日单位净值": li['dwjz'],
                    "是否可购": li['isbuy'],
                    "限购大额": li['sgzt'],
                    "基金类型": li['FType'],
                    "Discount": li['Discount'],
                    "Rate": li['Rate'],
                    "feature": li['feature'],
                    "fundtype": li['fundtype'],
                }
                allDataList.append(result)
        else:
            print("** {} is wrong data".format(self.title))
        # 数据导出相应文件格式
        return allDataList

    #003 数据插入mongoDB
    def insertData(self, data=None):
        self.my_Col.drop()
        x = self.my_Col.insert_many(data)
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
    #函数实例化
    start = ttjj_jzgs()
    start.main()




