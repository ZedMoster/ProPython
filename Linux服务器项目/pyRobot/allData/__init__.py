#!/usr/bin/env python
# -*- coding: utf-8 -*-

import werobot
from aip import AipOcr

from .to_clientDB import *
from .datawxreplace import *
from .datadytt import *
from .data_flac import *
from .data_xmlFund import *
from .fund_id_image import *
from .fund_margin import *
from .fund_shell import *
from .dataRevitUser import *
from .datajd_parity import *
from .fund_login import *
from .fund_login_site import *

from werobot.replies import ImageReply
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse
import datetime
import requests
import pymongo
import json
import os
import re
import matplotlib.pyplot as plt
import matplotlib
import datetime

# 微信api接口数据
robot = werobot.WeRoBot(token='tokenlookthis')

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.config['APP_ID'] = 'wxd5590b08982ac9be'
robot.config['APP_SECRET'] = '502e0bf9c0a3ee872e7800c36abcb17e'

# 微信封装的部分api接口
# client = robot.client
client = robot.client

# baidu-api接口数据
APP_ID = '16954036'
API_KEY = 'zDs88WsG7Kl14uat0746aqFS'
SECRET_KEY = '9AMCFe1CyMCUT0PYF3lpXsEHjxaTi4oS'
client_Baidu = AipOcr(APP_ID, API_KEY, SECRET_KEY)
