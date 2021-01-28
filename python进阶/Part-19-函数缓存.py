#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-28
# @Author    : ZedMoster1@gmail.com

# # 函数缓存 (Function caching)
# 函数缓存允许我们将一个函数对于给定参数的返回值缓存起来。
# 使用 lru_cache 装饰器

from functools import lru_cache


# @lru_cache(maxsize=32)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
#
# print([fib(n) for n in range(100)])


@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y


print(add(1, 2))
print(add(1, 2))
print(add(2, 3))
print(add(2, 3))
print(add(2, 3))
print(add(3, 4))
print(add(3, 4))
print(add(4, 5))
print(add(4, 5))

# 查看缓存
cache = add.cache_info
# 清空缓存
clear = add.cache_clear
