# -*- coding: UTF-8 -*-
import pandas as pd
import pymongo
import os


def to_excel(data=None,code=None):
    path = 'grade'
    if not os.path.exists(path):
        os.makedirs(path)
    # 筛选过后的数据合并
    filename = 'grade/xml_{}.xlsx'.format(code)
    try:
        with pd.ExcelWriter(filename) as writer:
            # sheet name
            name = '基金历史净值均值'
            data.to_excel(writer, sheet_name=name)
            # print("-- good job with ID {}".format(code))
    except:
        pass

def fund_describe(code=None):
    if code == '':
        return '** NO code'
    else:
        # mongodb服务的地址和端口号
        myClient = pymongo.MongoClient("127.0.0.1", 27017)
        # 连接到 天天基金 数据库
        mydb = myClient["scrapy_TTJJ_LSJZ"]
        # print('-- complete\n')
        mycol = mydb[code]

        df = pd.DataFrame(list(mycol.find({}, {'_id': 0})))
        df[['日增长率', '单位净值', '累计净值']] = df[['日增长率', '单位净值', '累计净值']].apply(pd.to_numeric)

        word = df.describe(percentiles=[.33, .5, .75])
        df = pd.DataFrame(word)

        to_excel(df, code)


def mainID(code):
    fund_describe(code)
    

if __name__ == '__main__':
    mainID('162703')
