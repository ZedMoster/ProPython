#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# # 推导式（又称解析式）
# 推导式是可以从一个数据序列构建另一个新的数据序列的结构体。Python的一种独有特性。
# 共有三种推导：
# * 列表(list)推导式
# * 字典(dict)推导式
# * 集合(set)推导式

# ## 列表推导式（list comprehensions）
# 规范：variable = [out_exp for out_exp in input_list if out_exp == 2]

multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)

# 用于创建列表
squared = [x ** 2 for x in range(10)]
print(squared)

# ## 字典推导式（dict comprehensions）

# 字典键转小写
case = {'a': 10, 'B': 34, 'A': 7}
case_frequency = {
    k.lower(): case.get(k.lower(), 0) + case.get(k.upper(), 0)
    for k in case.keys()}
print(case_frequency)

# 字典键值转换
print({v: k for k, v in case_frequency.items()})

# ## 集合推导式（set comprehensions）

squared = {x ** 2 for x in [1, 1, 2]}
print(squared)
