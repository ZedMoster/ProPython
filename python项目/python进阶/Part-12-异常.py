#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# 异常处理是一种艺术，一旦你掌握，会授予你无穷的力量。

# # try/except
# 可能触发异常的代码放到 try 语句块里，处理异常的代码在 except 语句块里。

try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))

# # 处理多个异常
# 我们可以使用三种方法来处理多个异常。
# * 把所有可能发生的异常放到一个元组里

try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))

# * 对每个单独的异常在单独的except语句块中处理

try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    # raise e
except IOError as e:
    print("An error occurred.")
    # raise e

# * 捕获所有异常

try:
    file = open('test.txt', 'rb')
except Exception as e:
    # 打印一些异常日志，如果你想要的话
    print("Exception")
    # raise e

# # finally语句
# 包裹到 finally 从句中的代码不管异常是否触发都将会被执行

try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

# # try/else语句
# else从句只会在没有异常的情况下执行，而且它会在finally语句之前执行。

try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # 这里的代码只会在try语句里没有触发异常时运行,
    # 但是这里的异常将 *不会* 被捕获
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')
