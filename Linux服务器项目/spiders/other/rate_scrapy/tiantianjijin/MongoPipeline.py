import scrapy
import pymongo
import re
from to_client import *

class MongoDBPipeline(object):

    def __init__(self):
        # 设置本地连接地址
        self.db = to_client()

    #空列表赋值，提取列表唯一值
    def get_valus(self,data=None):
        if len(data) == 0:
            return "--"
        else:
            return data[0]

    def process_item(self, item, spider):
        '''
            每个实现保存的类里面必须都要有这个方法，且名字固定，用来具体实现怎么保存
        '''
        if not item['基金代码']:
            return item

        table = self.db['fund_rate']
        _id = self.get_valus(item['基金代码'])

        jjgm = re.findall("：(.*?)亿元", self.get_valus(item['基金规模']))[0]

        # 自定义保存列
        data={
            '_id':  _id,
            '基金代码':  self.get_valus(item['基金代码']),
            '基金名称':  self.get_valus(item['基金名称']),
            '基金类型':  self.get_valus(item['基金类型']),
            '基金规模':  jjgm,
            '基金经理':  self.get_valus(item['基金经理']),
            '成立日期':  self.get_valus(item['成立日期']).strip('：'),
            '管理公司':  self.get_valus(item['管理公司']),
            '最近1周_k': self.get_valus(item['最近1周_k']),
            '最近1月_k': self.get_valus(item['最近1月_k']),
            '最近3月_k': self.get_valus(item['最近3月_k']),
            '最近6月_k': self.get_valus(item['最近6月_k']),
            '今年以来_k':self.get_valus(item['今年以来_k']),
            '最近1年_k': self.get_valus(item['最近1年_k']),
            '最近2年_k': self.get_valus(item['最近2年_k']),
            '最近3年_k': self.get_valus(item['最近3年_k']),
        }

        # 集合插入数据
        try:
            # mongodb在插入数据环节避免数据重复的方法
            table.update({'_id': _id}, {'$set': data}, True)

            return item
        except:
            pass
