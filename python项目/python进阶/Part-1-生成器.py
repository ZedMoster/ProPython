#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-26
# @Author    : ZedMoster1@gmail.com

# # 生成器(Generators)
# ## yield

def fib(n):
    a = b = 1
    for i in range(n):
        yield a  # generator version
        a, b = b, a + b


fib = fib(20)
print(fib)
# <generator object fibon at 0x000002308781E7C8>


for x in fib:
    print(x)

# 生成器最佳应用场景是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。
