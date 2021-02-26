#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# # 枚举(enumerate)
# 枚举(enumerate)是Python内置函数

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):  # 可选参数允许我们定制从哪个数字开始枚举
    print((c, value))

# 创建包含索引的元组列表
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 100))
print(counter_list)
