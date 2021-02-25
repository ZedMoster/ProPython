# coding:utf-8
import pymongo

#获取基金ID
def get_id():
    myClient = to_client()
    _db = myClient["fund_data"]
    # 连接到id集合
    my_set = _db["fund_id"]
    # 仅查找 基金代码
    data = list(my_set.find({}, {"_id":0, "基金代码":1}))
    # 返回数据库字典数据
    return data

# 连接TTJJ数据库
def to_client():
    # mongodb服务的地址和端口号
    myClient = pymongo.MongoClient('mongodb://long:ailong.123@111.229.98.184:27017')
    # 连接到  数据库
    return myClient

if __name__ == '__main__':
    a = get_id()
    print(a)
