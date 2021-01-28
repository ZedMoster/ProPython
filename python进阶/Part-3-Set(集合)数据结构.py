#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# # set(集合)数据结构
# set(集合)是一个非常有用的数据结构。它与列表(list)的行为类似，区别在于set不能包含重复的值。

# eg:获取集合中出现次数大于1的元素
# ** 通常情况 **
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

# ** 使用Set() **
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

###########################################################

# * 交集
# 对比两个集合的交集（两个集合中都有的数据）
valid = {'yellow', 'red', 'blue', 'green', 'black'}
input_set = {'red', 'brown'}
print(input_set.intersection(valid))
### 输出: set(['red'])


# * 差集
# 差集(difference)找出无效的数据
valid = {'yellow', 'red', 'blue', 'green', 'black'}
input_set = {'red', 'brown'}
print(input_set.difference(valid))

# * 并集
# union 合并两个集合中的所有数据
valid = {'a', 'b', 'c', 'd', 'e'}
input_set = {'e', 'f'}
print(valid.union(input_set))
