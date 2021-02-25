#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .to_clientDB import to_clientDB
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import datetime
import pymongo
import requests
import os


def fund_describe_photo(msg):
    byword = msg.strip('fund').strip()
    # print(byword)
    if byword == '':
        return '✨fund 基金代码\n✨eg:fund 110011（基金代码）'
    else:
        words = byword.split()
        _id = words[0]
        try:
            _key = int(words[1])
            if _key < 30:
                _key = 30
            elif _key > 60:
                _key = 60
            else:
                pass
        except:
            _key = 30
        
        # 连接到 基金 数据库
        mycol = to_clientDB("fund_history", _id)
        df = pd.DataFrame(list(mycol.find({}, {'_id': 0}))).sort_values(
            by="净值日期", ascending=False)
        df[['日增长率', '单位净值', '累计净值']] = df[['日增长率', '单位净值', '累计净值']].apply(
            pd.to_numeric)
        df_30 = df.iloc[:_key].sort_values(['净值日期'], ascending=True)
        
        directory = os.path.join(os.getcwd(), 'grade')
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # describe
        _rate = round((df_30['日增长率'] > 0).sum() / df_30['日增长率'].count(), 2)
        _mean = df_30['日增长率'].describe().iloc[1].round(2)
        _std = df_30['日增长率'].describe().iloc[2].round(2)
        _min = df_30['日增长率'].describe().iloc[3].round(2)
        _max = df_30['日增长率'].describe().iloc[7].round(2)
        _25 = df_30['日增长率'].describe().iloc[4].round(2)
        _50 = df_30['日增长率'].describe().iloc[5].round(2)
        _75 = df_30['日增长率'].describe().iloc[6].round(2)
        
        # 默认字体  & '-'负号
        # matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        # matplotlib.rcParams['font.family'] = 'sans-serif'
        # matplotlib.rcParams['axes.unicode_minus'] = False
        
        ######################## 日增长率 ########################
        fig_rate = plt.figure(figsize=(_key / 2, _key / 5), dpi=150)
        
        # 近30天的数据
        plt.plot(df_30['净值日期'], df_30['日增长率'], color='b', linewidth=1.5,
                 label="rate")
        
        x = range(1, _key + 1, 1)
        plt.xticks(df_30['净值日期'], x)
        
        # 使用xlim()/ylim()调整坐标轴
        plt.xlabel('datetime', fontsize=_key / 4)
        plt.ylabel('rate', fontsize=_key / 4)
        
        # 添加标题
        title_1 = '{}_center{}_rate'.format(_id, _key)
        plt.title(title_1, fontsize=_key / 3)
        
        # 添加图例
        plt.legend(loc='upper left', fontsize=_key / 4)
        
        # 设置网格线
        plt.grid(True, ls=':', color='g', alpha=1)
        plt.axhline(y=0, c='r', ls='--', lw=3)
        
        # 散点图
        plt.scatter(df_30['净值日期'], df_30['日增长率'], c='0.3', label='scatters')
        # 去掉图形上边和右侧的边框
        for spine in plt.gca().spines.keys():
            if spine == 'top' or spine == 'right':
                plt.gca().spines[spine].set_color('none')
        
        # 添加文字说明
        plt.text(-1, _min + _std,
                 r'$\sigma={}$  mean={}  std={}  min={}  max={}  25%={}  50%={}  75%={}'.format(
                     _rate, _mean, _std,
                     _min,
                     _max, _25, _50, _75),
                 alpha=0.4)
        fileName = directory + '/{}.png'.format(title_1)
        fig_rate.savefig(fileName)
        
        media_id = get_media_ID(fileName)
        
        return media_id


# 获取token
def get_token():
    ''''''
    payload_access_token = {
        'grant_type': 'client_credential',
        'appid'     : 'wxd5590b08982ac9be',
        'secret'    : '502e0bf9c0a3ee872e7800c36abcb17e'
    }
    token_url = 'https://api.weixin.qq.com/cgi-bin/token'
    r = requests.get(token_url, params=payload_access_token)
    dict_result = (r.json())
    return dict_result['access_token']


def get_media_ID(path):
    img_url = 'https://api.weixin.qq.com/cgi-bin/material/add_material'
    payload_img = {
        'access_token': get_token(),
        'type'        : 'image'
    }
    data = {'media': open(path, 'rb')}
    r = requests.post(url=img_url, params=payload_img, files=data)
    dict = r.json()
    return dict['media_id']


if __name__ == '__main__':
    msg = 'fund 162703 30'
    media_id = fund_describe_photo(msg)
    print(media_id)
