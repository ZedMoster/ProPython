#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# # lambda表达式（匿名函数）
# 语法：lambda 参数:操作(参数)

def add(x, y): return x + y


print(add(3, 5))

# * 列表排序
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)
