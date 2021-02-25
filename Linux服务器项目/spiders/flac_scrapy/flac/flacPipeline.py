# coding:utf-8
import scrapy
import pymongo
from to_clientDB import to_clientDB

class FlacPipeline(object):

    def __init__(self):
        '''
        数据库连接
        '''
        self.my_col = to_clientDB("weRobot_data","music_flac")

    def process_item(self, item, spider):
        # 自定义保存列
        data={
            '_id': item['_id'][0],
            'name': item['name'][0].strip('\n').strip('\t').strip(),
            'author': item['author'][0],
            'down': item['down'][0],
        }
        # 集合插入数据
        try:
            self.my_col.update({'_id': item['_id'][0]}, {'$set': data}, True)
            return item
        except Exception as e:
            print(e)