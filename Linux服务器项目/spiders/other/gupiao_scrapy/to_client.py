# coding:utf-8
import pymongo


# 连接TTJJ数据库
def to_client_gp():

    # mongodb服务的地址和端口号
    myClient = pymongo.MongoClient('mongodb://localhost:27017')
    # 连接到 天天基金 数据库
    db_TTJJ = myClient["股票代码"]

    # 返回连接到TTJJ数据库
    return db_TTJJ


if __name__ == '__main__':
    to_client_gp()
