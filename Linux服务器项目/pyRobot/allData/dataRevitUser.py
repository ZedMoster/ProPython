#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pymongo
import requests
import json
import time
import datetime
from .to_clientDB import to_clientDB


def getCaptcha(msg):
    '''
    注册Revit插件
    :param msg:
    :return:
    '''
    name = msg.strip('注册插件').strip()
    if name == '':
        return '/:li需要在后面加一个用户名:\n注册插件 UserName'
    else:
        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        timeStr = str(time.time())
        captcha = timeStr[-4:]
        
        my_col = to_clientDB("RevitUser", "userInfo")
        dateIn = list(my_col.find({}, {"_id": 0, "name": 1}))
        for i in dateIn:
            inName = i["name"]
            if inName == name:
                return "用户名已存在"
        # 用户数据：max 最大登录次数 2
        data = {
            # '_id': timeStr,
            'name'    : name,
            'password': None,
            'captcha' : captcha,
            'time'    : now_time,
            'max'     : 2,
        }
        try:
            my_col.update_one({'name': name}, {'$set': data}, True)
            # my_col.insert_one(data)
            c = "验证码：" + captcha
            return c
        except:
            return "验证码获取失败！"


if __name__ == '__main__':
    c = getCaptcha("注册插件 admin12")
    print(c)
