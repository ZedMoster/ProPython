#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# # global

# result变量只能在创建它的函数内部才允许访问，除非它是全局的(global)。
# 现在我们运行相同的代码，不过是在将result变量设为global之后
def add(value1, value2):
    global result
    result = value1 + value2


add(2, 4)
print(result)


# # result 返回多个参数
# 返回一个包含多个值的tuple(元组)，list(列表)或者dict(字典),来解决这个问题。
def profile():
    name = "Danny"
    age = 18
    return name, age


res = profile()
print(type(res))
print(res)
