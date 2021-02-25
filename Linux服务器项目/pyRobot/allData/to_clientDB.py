# coding : utf-8
import pymongo


def My_DB(dbName):
    '''
    链接MongoDB _db 数据库
    :param dbName:
    :return: 返回 my_db 链接
    '''
    my_Client = pymongo.MongoClient('mongodb://root:root.1234@111.229.98.184:27017')
    my_db = my_Client[dbName]
    return my_db


def to_clientDB(dbName, colName):
    '''
    链接MongoDB _col 数据库
    :param dbName: 数据库db名称
    :param colName: 数据库col名称
    :return: 指定col数据库的链接
    '''
    my_Client = pymongo.MongoClient('mongodb://root:root.1234@111.229.98.184:27017')
    # my_Client = pymongo.MongoClient('mongodb://long:ailong.123@111.229.98.184:27017')
    my_db = my_Client[dbName]
    my_col = my_db[colName]
    return my_col


if __name__ == "__main__":
    to_clientDB("db", "col")
