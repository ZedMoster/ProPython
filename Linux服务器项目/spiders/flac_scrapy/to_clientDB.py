import pymongo

def to_clientDB(dbName, colName):

    my_Client = pymongo.MongoClient('mongodb://root:root.1234@localhost:27017')
    # my_Client = pymongo.MongoClient('mongodb://long:ailong.123@111.229.98.184:27017')
    # 连接到 天天基金 数据库
    my_db = my_Client[dbName]
    # 修改数据库名称
    my_col = my_db[colName]

    return my_col

if __name__ == "__main__":
    to_clientDB("db","col")

