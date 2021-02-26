#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# # for/else循环的基本结构
# 找出2到10之间的数字的因子
for n in range(10, 15):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', int(n / x))
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
