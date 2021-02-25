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
        self.myClient = pymongo.MongoClient('mongodb://long:ailong.123@localhost:27017')
        self.db = self.myClient["股票"]



    def process_item(self, item, spider):
        '''
            每个实现保存的类里面必须都要有这个方法，且名字固定，用来具体实现怎么保存
        '''

        if not item['name']:
            return item

        code = item['code']

        table = self.db[code]

        # 自定义保存列
        data={
            '_id': item['date_time'],
            'name': item['name'],
            'code': item['code'],
            'market': item['market'],
            'dk_total': item['dk_total'],
            'jin_kai': item['jin_kai'],
            'zui_xin': item['zui_xin'],
            'zui_gao': item['zui_gao'],
            'zui_di': item['zui_di'],
            'turnover_L': item['turnover_L'],
            'turnover_E': item['turnover_E'],
            'amplitude': item['amplitude'],
        }

        # 集合插入数据
        try:
            # mongodb在插入数据环节避免数据重复的方法
            table.update({'_id': item['date_time']}, {'$set': data}, True)

            return item
        except:
            pass