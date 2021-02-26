#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# # 装饰器
# 简单地说：修改其他函数的功能的函数。

# python自带装饰器复制函数注释及说明信息
from functools import wraps


# ### 装饰器类
# 类也可以用来构建装饰器。那我们现在以一个类而不是一个函数的方式，来重新构建 log_it。

class log_it(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            self.save(func.__name__ + " is Running")
            self.notification()
            return func(*args, **kwargs)

        return wrapped_function

    def save(self, log_string):
        print("保存日志：{0}\n日志内容：{1}".format(self.logfile, log_string))

    @staticmethod
    def notification():
        print("通知消息：已保存")


@log_it()
def add(a, b):
    return a + b


print(add(1, 2))

# class email_log_it(log_it):
#     def __init__(self, email='admin@myproject.com', *args, **kwargs):
#         self.email = email
#         super(log_it, self).__init__(*args, **kwargs)
#
#     def notify(self):
#         print("send email to:" + self.email)
#
#
# @email_log_it()
# def my_func2():
#     pass

# ###################################################################
# # * 一切皆对象
# # 首先我们来理解下Python中的函数
# def hi(name="Tom"):
#     return "hi " + name
#
#
# print(hi())
#
# # 我们甚至可以将一个函数赋值给一个变量，比如
# greet = hi
# # 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# # 而是在将它放在greet变量里头。我们尝试运行下这个
#
# print(greet())
#
# # 如果我们删掉旧的hi函数，看看会发生什么！
# del hi
# print("del hi")
# # print(hi())
#
# print(greet())
#
#
# # ** 将一个函数赋值给一个变量 **
#
# ###################################################################
#
# # * 在函数中定义函数
# def hi2(name="Tom"):
#     print("now you are inside the hi() function")
#
#     def greet():
#         return "now you are in the greet() function"
#
#     def welcome():
#         return "now you are in the welcome() function"
#
#     print(greet())
#     print(welcome())
#     print("now you are back in the hi() function")
#
#
# hi2()
#
#
# # 上面展示了无论何时你调用hi(), greet()和welcome()将会同时被调用。
#
# # 然后greet()和welcome()函数在hi()函数之外是不能访问的
# # 比如：greet()  outputs: NameError: name 'greet' is not defined
#
# ###################################################################
#
# # * 从函数中返回函数
# # 其实并不需要在一个函数里去执行另一个函数，我们也可以将其作为输出返回出来：
# def hi3(name="Tom"):
#     def greet():
#         return "now you are in the greet() function"
#
#     def welcome():
#         return "now you are in the welcome() function"
#
#     if name == "Tom":
#         return greet
#     else:
#         return welcome
#
#
# a = hi3()
# print(a)
#
# # 上面清晰地展示了`a`现在指向到 hi3() 函数中的greet()函数
# # 现在试试这个
#
# print(a())
#
#
# # 在if/else语句中我们返回greet和welcome，而不是greet()和welcome()。
# # 为什么那样？这是因为当你把一对小括号放在后面，这个函数就会执行；
# # 然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它。
#
# # 当我们写下a = hi3()，hi3()会被执行，而由于 name 参数默认是 Tom，所以函数 ** greet ** 被返回了。
# # 如果我们把语句改为a = hi3(name = "ali")，那么welcome函数将被返回。
# # 我们还可以打印出 ** hi3()() **，这会输出now you are in the welcome() function。
#
# ###################################################################
#
# # * 将函数作为参数传给另一个函数
# def hi4():
#     return "hi Tom!"
#
#
# def doSomethingBeforeHi4(func):
#     print("I am doing some boring work before executing hi4()")
#     print(func())
#
#
# doSomethingBeforeHi4(hi4)
#
# # 装饰器让你在一个函数的前后去执行代码。
#
# ###################################################################
#
#
#
# # # 你的第一个装饰器
# def a_new_decorator(a_func):
#     '''
#     定义装饰器函数
#     :param a_func: 函数名
#     :return: 装饰器函数名
#     '''
#
#     @wraps(a_func)
#     def wrapTheFunction():
#         # 装饰器函数 start
#         print("\nI am doing some boring work before executing a_func()")
#         # 传入函数
#         a_func()
#         # 装饰器函数 end
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction
#
#
# # @ 给 a_function_requiring_decoration 添加装饰器 a_new_decorator
# @a_new_decorator
# def a_function_requiring_decoration():
#     """Hey you! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell")
#
#
# a_function_requiring_decoration()
# print(a_function_requiring_decoration.__name__)
#
# ###################################################################
#
# # ## 规范写法
#
#
# def decorator_name(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         if not can_run:
#             return "Function will not run"
#         return f(*args, **kwargs)
#
#     return decorated
#
#
# @decorator_name
# def func():
#     return ("Function is running")
#
#
# can_run = True
# print(func())
#
# # 注意：@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。
# # 这可以让我们在装饰器里面访问在装饰之前的函数的属性。
#
# ###################################################################
#
# # # 使用场景
# # ## 授权(Authorization)
#
# # 装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。它们被大量使用于Flask和Django web框架中。
# # 这里是一个例子来使用基于装饰器的授权：
#
#
#
# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         #  验证用户名是否存在
#         if auth:
#             print("no username")
#         return f(*args, **kwargs)
#
#     return decorated
#
#
# auth = []
#
# # ## 日志(Logging)
# # 日志是装饰器运用的另一个亮点。
# # 这是个例子：
#
#
# def log_it(func):
#     @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__ + " was called")
#         return func(*args, **kwargs)
#
#     return with_logging
#
#
# @log_it
# def addition_func(x):
#     """Do some math."""
#     return x + x
#
#
# result = addition_func(4)
#
# # ### 在函数中嵌入装饰器
#
#
# def log_it(logfile='out.log'):
#     def logging_decorator(func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + " was called"
#             print("文件名称：{}\n文件内容：{}".format(logfile, log_string))
#
#             # # 打开logfile，并写入内容
#             # with open(logfile, 'a') as opened_file:
#             #     # 现在将日志打到指定的logfile
#             #     opened_file.write(log_string + '\n')
#
#             return func(*args, **kwargs)
#
#         return wrapped_function
#
#     return logging_decorator
#
#
# @log_it()
# def my_func1():
#     pass
#
#
# @log_it(logfile='func2.log')
# def my_func2():
#     pass
#
#
# my_func1()
# my_func2()
