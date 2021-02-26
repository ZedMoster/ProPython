#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-28
# @Author    : ZedMoster1@gmail.com

# # 协程
# Python中的协程和生成器很相似但又稍有不同。
# 主要区别在于：生成器是数据的生产者,协程则是数据的消费者.

# 创建生成器
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# 创建协程
def grep(pattern):
    print("Searching for", pattern)
    print("=" * 30)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


# 创建协程
search = grep('love')
# 启动协程
next(search)

# send()方法向它传值
search.send("No keyword no send")
# 包含内容
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutine instead!")

# 关闭一个协程
search.close()
