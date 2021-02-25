# coding:utf-8
import pymongo

#获取基金ID
def get_id():
    _db = to_client()
    # 连接到id集合
    my_set = _db["fund_id"]
    # 仅查找 基金代码
    data = list(my_set.find({}, {"_id":0, "基金代码":1}))
    # 返回数据库字典数据
    return data

# 连接TTJJ数据库
def to_client():
    # mongodb服务的地址和端口号
    myClient = pymongo.MongoClient('mongodb://localhost:27017')

    myClient.admin.authenticate("root","root.1234",mechanism='SCRAM-SHA-1')
    # 连接到 数据库
    _db = myClient["fund_晨星"]
    # 返回连接到TTJJ数据库
    return _db

if __name__ == '__main__':
    a = get_id()
    print(a)
