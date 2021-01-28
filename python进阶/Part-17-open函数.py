#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-28
# @Author    : ZedMoster1@gmail.com

# # open函数
# open 函数可以打开一个文件。

# * r:读取文件
# * r+:读取并写入文件
# * w:覆盖写入文件
# * a:追加写入

import io

with open('photo.jpg', 'rb') as inf:
    jpgData = inf.read()

if jpgData.startswith(b'\xff\xd8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(text % len(jpgData))
