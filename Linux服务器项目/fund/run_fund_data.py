#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime


def run_py(fileName):
    try:
        os.system('python3 ' + fileName)
    except:
        os.system(fileName)


if __name__ == "__main__":
    # 指定含顺序文件夹列表
    filelist = ['data_id.py', 'data_company.py', 'data_dtph.py', 'data_jjjl.py',
                'data_jjph.py', 'data_jzgs.py', 'data_zqpj.py']
    # 获取当日时间
    now = datetime.datetime.now()
    strToday = str(now.strftime('%Y-%m-%d %H:%M:%S'))
    print("-- the job start at {}".format(strToday))
    
    good_job = []
    try:
        for file in filelist:
            run_py(file)
            good_job.append(file)
    except:
        pass
    print(good_job)
    
    # 获取路径下所有的py文件
    # path = r'D:\OneDrive - cqu.edu.cn\Linux\fund_everyday\other'
    # filelist = os.listdir(path)
    # for fileName in filelist:
    #     name, filetype = os.path.splitext(fileName)
    #     if '.py' == filetype and name not in ['to_client', 'run_fund_data']:
    #         run_py(fileName)
    #     else:
    #         pass
