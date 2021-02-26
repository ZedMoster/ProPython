#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# # 一行式的Python命令

# ## 简易Web Server
# 通过网络快速共享文件
# 进入到你要共享文件的目录下并在命令行中运行下面的代码：

'''
python - m SimpleHTTPServer  # Python 2
python - m http.server       # Python 3
'''

# ## 漂亮的打印
import itertools
from pprint import pprint

my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
print(my_dict)
pprint(my_dict)

# ## 脚本性能分析
# 备注：cProfile是一个比profile更快的实现，因为它是用c写的

'''
python -m cProfile my_script.py
'''

# ## CSV转换为json
# 确保更换csv_file.csv为你想要转换的csv文件

'''
python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"
'''

# ## 列表辗平 （拍平一次）
# 使用 itertools 包中的 itertools.chain.from_iterable 轻松快速的辗平一个列表。

a_list = [[1, 2], [3, 4], [5, 6], [[10]]]

print(list(itertools.chain.from_iterable(a_list)))
print(list(itertools.chain(*a_list)))


# Output:[1, 2, 3, 4, 5, 6, [10]]

# ## 一行式的构造器
# 避免类初始化时大量重复的赋值语句
class A(object):
    def __init__(self, a, b, c):
        self.a = a
        self.__dict__.update(
            {k: v for k, v in locals().items() if k != 'self'})
        # self.b = b
        # self.c = c


a = A(0, 1, 2)
print(a.a)
print(a.b)
print(a.c)
