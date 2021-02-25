# -*- coding: UTF-8 -*-
import datetime
import pymongo
import pandas as pd
from .to_clientDB import to_clientDB, My_DB


# 连接mydb数据库
def fund_to_client_user(msg):
    byword = msg.strip('user').strip()
    if byword == '':
        return '检查邮箱是否正确,是否已关注相应基金'
    else:
        if byword == 'my':
            byword = '1505636116@qq.com'
        else:
            pass

        # 连接到 天天基金 数据库
        my_db = My_DB("fund_login")
        # 获取所有的数据库名称
        col_list = my_db.list_collection_names()

        if byword in col_list:
            my_col = my_db[byword]
            data = my_col.find({}, {'_id': 0, 'code': 1})
            key_word = fund_to_guzhi_user(list(data), byword)
            return key_word
        else:
            return 'no this email : %s' % byword


def fund_to_guzhi_user(site_list, site_name):
    key_word = '用户：{}\n关注了以下基金\n\n'.format(site_name)
    # 链接数据库 fund_jzgs
    my_col = to_clientDB("fund_data", "fund_jzgs")

    for word in site_list:
        my_query = {"基金代码": word['code']}
        try:
            data = my_col.find(my_query)[0]
            result = '基金名称：{}\n基金代码：{}\n净值估算：{}\n日增长率：{}\n\n'.format(data['基金名称'], word['code'], data['估增长率'],
                                                                     data['今日日增长率'])
            # rate = float(data['估增长率'].strip('%'))
            key_word += result
        except:
            key_word += '建议删除此基金代码: {}\n\n'.format(word['code'])
    return key_word.strip('\n\n')


if __name__ == '__main__':
    # key_word = fund_to_client_user('user 1505636116@qq.com')
    key_word = fund_to_client_user('user my')

    print(key_word)
