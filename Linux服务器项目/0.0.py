#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-02-25
# @Author    : ZedMoster1@gmail.com

import requests

r = requests.get("http://fund.jrj.com.cn/action/fhs/list.jspa")
print(r.status_code)
print(r.text)