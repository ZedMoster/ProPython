# coding:utf-8
from to_clientDB import to_clientDB
import scrapy
import pymongo
import re

class DyttPipeline(object):

    def __init__(self):
        '''
        数据库连接
        '''
        self.my_db = to_clientDB("weRobot_data","dytt8")

    def get_valus(self,data=None):
        '''
        #空列表赋值，提取列表唯一值
        :param data: list
        :return: list[0]
        '''
        if len(data) == 0:
            return "--"
        else:
            return data[0]

    def process_item(self, item, spider):
        '''
            每个实现保存的类里面必须都要有这个方法，且名字固定，用来具体实现怎么保存
        '''
        if not item['_id']:
            return item

        # 自定义保存列
        data={
            '_id': self.get_valus(item['_id']),
            'title': item['title'],
            'code': item['code'],
            'date': item['date'],
            'thunder': self.get_valus(item['thunder']),
        }

        # 集合插入数据
        try:
            self.my_db.update({'_id': self.get_valus(item['_id'])}, {'$set': data}, True)
            return item
        except:
            pass
