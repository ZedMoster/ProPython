#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pymongo
import json
from .to_clientDB import to_clientDB


# 接口来源:https://github.com/MZCretin/RollToolsApi
def music_flac(msg):
    '''
    数据库中的音乐链接
    :param msg: 指定消息内容
    :return: 数据库检索msg歌曲链接
    '''
    name = msg.strip('music').strip()
    if name == '':
        return '/:li需要输入:music 歌名'
    else:
        my_col = to_clientDB("weRobot_data", "music_flac")
        query = {"name": name}
        date = list(my_col.find(query))
        if len(date) == 0:
            return '歌名是否正确或者未包含此歌曲\n\n'
        else:
            word = '歌名【{}】总计 {} 首\n\n'.format(name, len(date))
            for i in date:
                keyword = '歌名:{}\n歌手:{}\n下载:{}\n\n'.format(i['name'],
                                                           i['author'],
                                                           i['down'])
                word += keyword
            return word.strip('\n\n')


if __name__ == '__main__':
    c = music_flac('music 模特')
    print(c)
