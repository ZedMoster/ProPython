import scrapy
import pymongo
import re
from to_client import *

class MongoDBPipeline(object):
    '''
    scrapy startproject project [项目名称]
    '''

    def __init__(self):
        # 设置本地连接地址
        client = to_client()
        self.table = client['fund_base']

    def get_valus(self,data=None):
        '''
        #空列表赋值，提取列表唯一值
        :param data: list
        :return: list[0]
        '''
        if data == '-':
            return 0
        else:
            return float(data.strip(','))

    def process_item(self, item, spider):
        '''
            每个实现保存的类里面必须都要有这个方法，且名字固定，用来具体实现怎么保存
        '''
        if not item['code']:
            return item

        # base total替换空值
        code = item['code'][0].split()[0]
        name = item['code'][0].split()[1]
        base = self.get_valus(item['base'][0].split('_')[1].split('.')[0].strip('new'))
        classify = item['classify'][0]
        setupday = item['setupday'][0]
        openday = item['openday'][0]
        isBuy = item['isBuy'][0]
        rede = item['rede'][0]
        total = self.get_valus(item['total'][0])
        Mini = item['Mini'][0]
        front = item['front'][0]

        # 自定义保存列
        data={
            '_id': code,
            'code': code,
            'name': name,
            'base': base,
            'classify': classify,
            'setupday': setupday,
            'openday': openday,
            'isBuy': isBuy,
            'rede': rede,
            'total': total,
            'Mini': Mini,
            'front': front,
        }

        # 集合插入数据
        try:
            self.table.update({'_id': data['_id']}, {'$set': data}, True)
            return item
        except:
            pass

