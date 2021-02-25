#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
from .to_clientDB import to_clientDB

add = '+'
sub = '-'


def fund_login_txt(msg=None):
    if '*' in msg:
        rate = float(msg.split('*')[0])
        byword = msg.split('*')[1].strip('login')
    else:
        # 默认值 0.0
        rate = 0
        byword = msg.strip('login')
    
    if byword == '':
        return None, None, None, None
    else:
        if add in byword:
            user = byword.split(add)[0].strip()
            data = byword.split(add)[1].split()
            if "qq.com" in user:
                return user, data, add, rate
        elif sub in byword:
            user = byword.split(sub)[0].strip()
            data = byword.split(sub)[1].split()
            if "qq.com" in user:
                return user, data, sub, rate
        else:
            return None, None, None, None


def fund_login_to_data(data, rate):
    many_dic = []
    for d in data:
        result = {
            '_id' : d,
            'code': d,
            'rate': rate,
        }
        many_dic.append(result)
    
    return many_dic


def fund_login_data_db(col, many_dic, _is):
    word = ''
    if _is == add:
        for dic in many_dic:
            result = '基金代码：{}\n'.format(dic['code'])
            word += result
            col.update_one({'_id': dic['_id']}, {'$set': dic}, True)
        return True, word
    elif _is == sub:
        for dic in many_dic:
            result = '基金代码：{}\n'.format(dic['code'])
            word += result
            # 删除限值
            dic.pop("rate")
            delYes = col.delete_one(dic)
            print(delYes)
        return False, word


def fund_login(msg):
    try:
        user, data, _is, rate = fund_login_txt(msg)
        # 连接DB
        my_col = to_clientDB("fund_login", user)
        # 构造字典数据
        many_dic = fund_login_to_data(data, rate)
        # 添加记录
        of, word = fund_login_data_db(my_col, many_dic, _is)
        if of:
            return '用户：{}\n\n{}\n基金ID添加成功'.format(user, word)
        else:
            return '用户：{}\n\n{}\n基金ID删除成功'.format(user, word)
    except Exception as e:
        return '<a href={1}>{0}</a>'.format(
            '✨请查看功能介绍-login QQ邮箱地址+基金ID\n' + str(e),
            'https://mp.weixin.qq.com/s/dHP5Q3esmMhPvrPhicOYWQ')


if __name__ == '__main__':
    # msg = '0*login 957898780@qq.com+007818 162703 110011 007817 1235'
    # msg = 'login 957898780@qq.com-1235'
    msg = 'login1505636116@qq.com-000595'
    a = fund_login(msg)
    print(a)
