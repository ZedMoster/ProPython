import scrapy
import pymongo
import re

class MongoDBPipeline(object):
    '''
    scrapy startproject project [项目名称]
    文件放置位置project/目录下
    setting 中设置

    ITEM_PIPELINES = {
        'project.MongoPipeline.MongoDBPipeline': 1
    }

    '''

    def __init__(self):
        '''
        数据库连接
        '''
        self.myClient = pymongo.MongoClient('mongodb://root:root.1234@localhost:27017')


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
        if not item['基金代码']:
            return item

        self.db = self.myClient["fund_history"]
        page = str(self.get_valus(item['基金代码']))
        table = self.db[page]
        _id = item['净值日期']
        # 自定义保存列
        data={
            '_id': _id,
            '基金代码': self.get_valus(item['基金代码']),
            '净值日期': item['净值日期'],
            '单位净值': item['单位净值'],
            '累计净值': item['累计净值'],
            '日增长率': item['日增长率'],
            '赎回状态': item['赎回状态'],
            '分红送配': item['分红送配'],
        }

        # 集合插入数据
        try:
            # mongodb在插入数据环节避免数据重复的方法
            table.update({'_id': _id}, {'$set': data}, True)

            return item
        except:
            pass
