#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-01-27
# @Author    : ZedMoster1@gmail.com

# # 容器(Collections)
# Python附带一个模块 collections，它包含许多容器数据类型.
# * defaultdict
# * counter
# * deque
# * namedtuple
# * enum.Enum (包含在Python 3.4以上)

# * defaultdict
# defaultdict与 dict 类型不同，你不需要检查key是否存在，所以可以直接这样做：

import json
import collections
from collections import defaultdict
from collections import Counter
from collections import deque
from collections import namedtuple
from enum import Enum

colours = (
    ('Yas', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arh', 'Green'),
    ('Ali', 'Black'),
    ('Yas', 'Red'),
    ('Ahm', 'Silver'),
)

# 定义数据类型 defaultdict(<class 'list'>, {})
favourite_colours = defaultdict(list)
for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

# 当你在一个字典中对一个键进行嵌套赋值时，如果这个键不存在，会触发keyError异常。
# defaultdict允许我们用一个聪明的方式绕过这个问题。
# 首先我分享一个使用dict触发KeyError的例子，然后提供一个使用defaultdict的解决方案。

# some_dict = {}
# some_dict['colours']['favourite'] = "yellow"
# # KeyError: 'colours'

# 创建一个数据类型


def tree(): return collections.defaultdict(tree)


some_dict = tree()
print(some_dict)  # defaultdict(<function <lambda> at 0x0000029724BB6438>, {})
some_dict['colours']['favourite'] = "yellow"

print(json.dumps(some_dict))

# * counter
# Counter是一个计数器，它可以帮助我们针对某项数据进行计数。
# 比如它可以用来计算每个人喜欢多少种颜色：


colours = (
    ('Yas', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arh', 'Green'),
    ('Ali', 'Black'),
    ('Yas', 'Red'),
    ('Ahm', 'Silver'),
)

# 统计name的人喜欢 color 个数
name_colors = Counter(name for name, colour in colours)
print(name_colors)
# 统计喜欢 color 颜色的 name 人的个数
color_names = Counter(colour for name, colour in colours)
print(color_names)

# 计数 __iter__
line_count = Counter([1, 2, 3, 4, 5, 1])
print(line_count)

# * deque
# deque提供了一个双端队列，你可以从头/尾两端添加或删除元素

d = deque(range(5))
print(d)
print(d.popleft())
print(d)
print(d.pop())
print(d)

# 限制这个列表的大小，当超出你设定的限制时，数据会从对队列另一端被挤出去 popleft()。
d = deque(range(10), maxlen=5)
print(d)

# 你还可以从任一端扩展这个队列中的数据：
d = deque([1, 2, 3])
d.extendleft([0])
d.extend([4, 5])
print(d)


# * namedtuple
# 一个元组是一个不可变的列表，它和命名元组(namedtuple)非常像
# 你不必使用整数索引来访问一个 namedtuple 的数据。
# 你可以像字典(dict)一样访问 namedtuple ，但 namedtuple 是不可变的。

# ## 普通类，仅有属性的情况

class XYZ(object):
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z

    def __str__(self):
        return "XYZ(X={0},Y={1},Z={2})".format(self.X, self.Y, self.Z)


p0 = XYZ(0, 0, 1)
print(p0)

# ## 使用 namedtuple
Point = namedtuple("Point", ["X", "Y", "Z"])
p1 = Point(1, 0, 0)
print(p1)
print(p1._asdict())  # 将命名元组转换为字典


# * enum.Enum (Python 3.4+)
# 创建枚举
class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9


Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.dog)

print(perry.type == tom.type)
print("name:%s, age:%s, type:%s" % (charlie.name, charlie.age, charlie.type))
