#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import pandas as pd
from .to_clientDB import to_clientDB


##from to_clientDB import to_clientDB


def dytt(msg):
    '''
    电影天堂 - 电影数据
    :param msg:
    :return:
    '''
    byword = msg.strip('电影').strip()
    if byword == '':
        return '✨输入电影下载及电影名称\n✨获取迅雷下载地址\n--------\n✨eg:电影 电影名称'
    else:
        my_col = to_clientDB("weRobot_data", "dytt8")
        
        query = {"title": {"$regex": byword}}
        news = list(my_col.find(query))
        
        # news = list(my_col.find({}))
        
        df = pd.DataFrame(news)
        words = '-*-数据来源网络仅供交流使用-*-\n检索【{}】名称得到以下列表：\n\n'.format(byword)
        i = 0
        movieName = df['title'].values
        for name in movieName:
            if byword in name:
                title = name
                date = list(df[df['title'] == name]['date'])[0]
                thunder = list(df[df['title'] == name]['thunder'])[0]
                word = '✨电影名称：{}\n✨更新时间：{}\n✨迅雷下载：\n\n{}\n\n'.format(title,
                                                                     date,
                                                                     thunder)
                if thunder not in words:
                    words += word
                    i += 1
        
        if i != 0 and len(words) <= 460:
            return words
        else:
            return "输入详细名称检索到太多的内容...."


if __name__ == '__main__':
    a = dytt('电影 同门')
    if a != None:
        print(a)
