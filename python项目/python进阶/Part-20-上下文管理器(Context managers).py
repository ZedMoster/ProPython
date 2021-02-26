#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-28
# @Author    : ZedMoster1@gmail.com

# # 上下文管理器
# 上下文管理器最广泛的案例就是with语句
# 上下文管理器的一个常见用例，是资源的加锁和解锁，以及关闭已打开的文件

# with语句
from contextlib import contextmanager
with open('some_file', 'w') as opened_file:
    opened_file.write('hello!')

# 等价
file = open('some_file', 'w')
try:
    file.write('hello!')
finally:
    file.close()


# ## 基于类的实现
# 一个上下文管理器的类，最起码要定义__enter__和__exit__方法。

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):  # __exit__函数接收三个参数
        self.file_obj.close()
        return True  # 处理异常


# 通过定义__enter__和__exit__方法，我们可以在with语句里使用它。

with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hello!')

# * with语句先暂存了 **File** 类的 **__exit__** 方法
# * 然后它调用 **File** 类的 **__enter__** 方法
# * **__enter__** 方法打开文件并返回给 **with语句**
# * 打开的文件句柄被传递给 **opened_file** 参数
# * 我们使用 **.write()** 来写文件
# * **with语句** 调用之前暂存的 **__exit__** 方法
# * **__exit__** 方法关闭了文件


# ### 处理异常
# __exit__方法的这三个参数：type, value和traceback
# 当异常发生时，with语句会采取哪些步骤。
# 1. 它把异常的type,value和traceback传递给__exit__方法
# 2. 它让__exit__方法来处理异常
# 3. 如果__exit__返回的是True，那么这个异常就被优雅地处理了。
# 4. 如果__exit__返回的是True以外的任何东西，那么这个异常将被with语句抛出。


# ## 基于生成器的实现
# ### contextlib模块


@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()


# 剖析:
# 1. Python解释器遇到了yield关键字。因为这个缘故它创建了一个生成器而不是一个普通的函数。
# 2. 因为这个装饰器，contextmanager会被调用并传入函数名（open_file）作为参数。
# 3. contextmanager函数返回一个以GeneratorContextManager对象封装过的生成器。
# 4. GeneratorContextManager被赋值给open_file函数，实际上在调用GeneratorContextManager对象。

with open_file('some_file') as f:
    f.write('hello!')
