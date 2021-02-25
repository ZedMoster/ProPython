#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import datetime
import pymongo
import os


def convert(item):
    if isinstance(item, str):
        if ',' not in item:
            if item != '-':
                return float(item)
            else:
                return None
        s = ''
        tmp = item.strip().split(',')
        for i in range(len(tmp)):
            s += tmp[i]
        return float(s)
    else:
        return None


def to_excel(df_3=None, df_6=None):
    path = 'toFile'
    if not os.path.exists(path):
        os.makedirs(path)
    # 筛选过后的数据合并
    
    filename = 'toFile/xml_morningstar.xlsx'
    
    with pd.ExcelWriter(filename) as writer:
        # sheet name
        name_3 = '3-大盘成长'
        name_6 = '6-中盘成长'
        
        columns = "code,name,classify,base,total,front,setupday,openday,Mini,isBuy,rede".split(
            ',')
        
        # 保存数据
        df_3[columns].to_excel(writer, sheet_name=name_3, index=False)
        df_6[columns].to_excel(writer, sheet_name=name_6, index=False)
        print(' -- good job')


if __name__ == '__main__':
    # mongodb服务的地址和端口号
    myClient = pymongo.MongoClient('mongodb://root:root.1234@localhost:27017')
    # 连接到 数据库
    mydb = myClient["fund_晨星"]
    # 数据库下集合
    mycol = mydb['fund_base']
    
    data = mycol.find({}, {'_id': 0})
    
    df = pd.DataFrame(list(data))
    
    # # 数据类型转换 服务器不需要
    # df['total'] = df['total'].map(convert)
    # df['base'] = df['base'].map(convert)
    
    # 1-大盘价值 2-大盘平衡 3-大盘成长 4-中盘价值 5-中盘平衡 6-中盘成长 7-小盘价值 8-小盘平衡 9-小盘成长 0-无评级
    
    d3 = df[(df['base'] == 3.0) & (df['total'] >= 90) & (
                df['isBuy'] == '开放')].sort_values('total')
    d6 = df[(df['base'] == 6.0) & (df['total'] >= 30) & (
                df['isBuy'] == '开放')].sort_values('total')
    
    to_excel(d3, d6)
