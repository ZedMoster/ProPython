# coding:utf-8
import pymongo

#获取基金ID
def get_id():

    db_TTJJ = to_client_TTJJ()
    # 连接到id集合
    my_ID = db_TTJJ["fund_id"]

    # 仅查找 基金代码
    data = my_ID.find({}, {"_id":0, "基金代码":1})

    # for i in data:
    #     print(i['基金代码'])

    # 返回数据库字典数据
    return data

# 连接TTJJ数据库
def to_client_TTJJ():

    # mongodb服务的地址和端口号
    myClient = pymongo.MongoClient('mongodb://root:root.1234@localhost:27017')
    # 连接到 数据库
    db_TTJJ = myClient["fund_data"]

    # 返回连接到TTJJ数据库
    return db_TTJJ


if __name__ == '__main__':
    get_id()
    to_client_TTJJ()
