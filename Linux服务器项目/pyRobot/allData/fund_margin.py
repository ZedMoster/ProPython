#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pymongo
import requests
import pymongo
import json
import math


def GetFundMoney(msg):
    '''
    星河湾4.0数据库
    :param msg:
    :return:
    '''
    name = msg.strip('margin').strip()
    if name == '':
        return '/:li 输入margin 金额 持有收益\n即可计算操作情况'
    else:
        data = name.split()
        # 全参数调用
        if len(data) == 4:
            return GetHowMoney(float(data[0]), float(data[1]), float(data[2]),
                               float(data[3]))
        elif len(data) == 3:
            if float(data[2]) < 0:
                return GetHowMoney(float(data[0]), float(data[1]),
                                   r=float(data[2]))
            else:
                return GetHowMoney(float(data[0]), float(data[1]),
                                   s=float(data[2]))
        # 默认参数 r s
        else:
            return GetHowMoney(float(data[0]), float(data[1]))


def GetHowMoney(money, lossMoney, r=-0.03, s=0.10):
    '''
    获取基金补仓金额
    :param money: 持仓金额
    :param lossMoney: 持有收益
    :param r: - 收益率
    :param s: + 收益率
    :return:
    '''
    # 总计
    _sum = money - lossMoney
    # 收益率
    _grade = lossMoney / (_sum)
    # 百分数表示
    grade = "%.2f%%" % (_grade * 100)
    _r = "%.2f%%" % (r * 100)
    _s = "%.2f%%" % (s * 100)
    result = "本金：{}\n持有收益率：{}\n负收益率限值：{}\n正收益率限值：{}\n{}\n".format(_sum, grade,
                                                                  _r, _s,
                                                                  "-" * 24)
    # 收益率位置 -0.03
    
    # 需要补仓
    if _grade <= r:
        tip = "-*-需要补仓-*-\n买入金额："
        # 计算补仓金额
        try:
            value = math.ceil(lossMoney / r - money)
        except:
            value = "负收益不能为0"
    # 不操作
    elif r < _grade <= s:
        tip = "-*-不需要操作！"
        value = grade
    # 卖出 收益
    elif s < _grade <= 2 * s:
        tip = "-*-建议卖出(1/3)-*-\n卖出金额："
        # 计算补仓金额
        value = math.ceil(_sum / 3)
    # 卖1/2
    elif 2 * s < _grade <= 3 * s:
        tip = "-*-建议卖出(1/2)-*-\n卖出金额："
        # 计算补仓金额
        value = math.ceil(_sum / 2)
    # 赚钱了
    else:
        tip = "-*-赚钱了！老铁！"
        value = grade
    # 输出结果
    result += "{}{}".format(tip, value)
    return result


if __name__ == '__main__':
    c = GetFundMoney('margin 900 -50 -0.01 1')
    print(c)
