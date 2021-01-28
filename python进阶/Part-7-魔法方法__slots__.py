#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# # __slots__
# 使用 __slots__ 来告诉 Python 不要使用字典，而且只给一个固定集合的属性分配空间。
# 内存占用率几乎40%~50%的减少。


class MyClass(object):
    __slots__ = ['name', 'age']

    def __init__(self, name, identifier):
        self.name = name
        self.age = identifier


m = MyClass("Tom", 20)

print(m.name)
print(m.age)
