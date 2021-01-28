#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# # reduce 计算结果
# 当需要对一个列表进行一些计算并返回结果时，Reduce 是个非常有用的函数。

from functools import reduce

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)

############################################################

# # Map
# Map会将一个函数映射到一个输入列表的所有元素上
# ** map(function_to_apply, list_of_inputs) **


# * 不使用
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i ** 2)

# * 使用
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))


# * 使用列表函数
def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

############################################################

# Filter
# filter过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表。
# filter类似于一个for循环，但它是一个内置函数，并且更快。

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
