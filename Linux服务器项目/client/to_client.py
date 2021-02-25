#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

import pymongo


class BaseClient(object):
    ''' BaseClass 链接 MongoDB '''
    
    @staticmethod
    def get_db(host='mongodb://127.0.0.1:27017', db_name="fund_data",
               col_name=None):
        '''
        链接数据库 MongoDB
        
        :param host: mongodb 链接地址
        :param db_name: 数据库DB名称
        :param col_name: 数据页名称
        :return: 如果col名称存在返回数据页(col_db)
                 否则返回数据库(database_db)
        '''
        client = pymongo.MongoClient(host)
        return client[db_name][col_name] if col_name else \
            client[db_name]
    
    @staticmethod
    def get_time():
        '''格式化时间'''
        
        now = datetime.datetime.now()
        return str(now.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    db = BaseClient.get_db()
    print(db)
