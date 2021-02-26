#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

import inspect

# # dir
# 列出了一个对象所拥有的属性和方法

my_list = [1, 2, 3]
print(dir(my_list))

# # type和id

print(type(''))
print(type([]))
print(type({}))
print(type(dict))
print(type(3))

name = "tom"
# print(dir(name))
print(id(name))

# # inspect模块
# inspect模块也提供了许多有用的函数，来获取活跃对象的信息。
# 比方说，你可以查看一个对象的成员

print(inspect.getmodule(str))
