#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# # 三元运算符
# 三元运算符通常在Python里被称为条件表达式，这些表达式基于真(true)/假(not)的条件判断
# 逻辑：condition_is_true if condition else condition_is_false

is_fat = True
state = "fat" if is_fat else "not fat"
print(state)
# 它允许用简单的一行快速判断，而不是使用复杂的多行if语句。 这在大多数时候非常有用，而且可以使代码简单可维护。
