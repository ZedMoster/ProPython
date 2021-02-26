#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-26
# @Author    : ZedMoster1@gmail.com

# # *args **kwargs 魔法变量
# ## *args 的用法
# 定义函数时，未知输入变量的个数

def clac(*args):  # *args:表示元组 可迭代
    '''计算器'''
    count = 0
    for i in args:
        count += i
    return count


print(clac(1, 2, 3, 4))


# ## **kwargs 的用法
# 传入键值参数

def person(**kwargs):
    for key, value in kwargs.items():
        print("{0}: {1}".format(key, value))


person(name="tom", age=20)

# ## 使用 *args 和 **kwargs 来调用函数
# 标准参数与*args、**kwargs在使用时的顺序
# 那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的：
# func(args, *args, **kwargs)
