#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import pymongo
import pandas as pd
from .to_clientDB import to_clientDB


# 连接mydb数据库
def fund_to_shell(msg):
    '''
    获取可卖出的份额
    :param msg:
    :return:
    '''
    byword = msg.strip('shell').strip()
    if byword == '':
        return 'shell 基金ID+收益\n自动计算份需卖出的份额'
    else:
        res = byword.split("+")
        grade = fund_to_grade_now(byword.split("+")[0])
        return "基金id:{0}\n收益:{1}\n估值:{2}\n\n可卖出份额:{3}".format(res[0], res[1],
                                                              grade,
                                                              round(float(res[
                                                                              1]) / float(
                                                                  grade)))


def fund_to_grade_now(Id):
    '''
    获取基金最新估值
    :param Id:
    :return:
    '''
    my_col = to_clientDB("fund_data", "fund_jzgs")
    my_query = {"基金代码": Id}
    data = my_col.find(my_query)[0]
    rate = data['今日估值']
    return rate


if __name__ == '__main__':
    key_word = fund_to_shell('shell 110011+600')
    print(key_word)
