#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-02-26
# @Author    : ZedMoster1@gmail.com


class PersonClass:
    '''定义Class 属性'''
    
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0 and value <= 120:
            self._age = value
        else:
            raise ValueError("输入年龄不正确：0-120")


if __name__ == '__main__':
    # 创建对象
    p = PersonClass(20)
    print(p.age)
    # 更新属性
    p.age = 22
    print(p.age)
    # 错误属性
    p.age = 220
    print(p.age)
