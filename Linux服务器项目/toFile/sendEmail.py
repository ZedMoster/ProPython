# -*- coding: UTF-8 -*-
import smtplib
import datetime
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
import pymongo
import pandas as pd
import time

# 日期
now = datetime.datetime.now()
strTime = str(now.strftime('%Y-%m-%d'))
strToday = str(now.strftime('%Y-%m-%d %H:%M:%S'))

def sendEmail(key_word, grade, to_user):
    # 发件人邮箱账号
    my_sender = '1505636116@qq.com'
    # 发件人邮箱密码
    my_pass = 'iozvbqauvbkebaha'

    # 邮件标题
    subject = strTime + '-以下已关注基金跌超预期值'
    # subject = "bug 测试修复中"
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("好用不火", 'utf-8')
    title_email = "已关注的基金今日跌超{}%".format(str(grade))
    message['To'] = Header(title_email, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText(key_word, 'plain', 'utf-8'))

    # 发送邮件
    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, to_user, message.as_string())
        print("{} ---- good job send Email".format(strToday))
        return True
    except smtplib.SMTPException:
        print("{} **** error send Email".format(strToday))
        return False


# 连接mydb数据库
def fund_to_client(mycol):
    data = mycol.find({},{'_id':0})
    return list(data)

def fund_to_guzhi(byword):
    global grade
    key_word = ''
    send_key = False
    # mongodb服务的地址和端口号
    my_Client = pymongo.MongoClient('mongodb://root:root.1234@111.229.98.184:27017')
    # my_Client = pymongo.MongoClient('mongodb://long:ailong.123@111.229.98.184:27017')
    # 连接到 天天基金 数据库
    my_db = my_Client['fund_data']
    # 修改数据库名称
    my_col = my_db['fund_jzgs']
    for word in byword:
        myquery = {"基金代码": word['code']}
        try:
            grade = word['rate']
        except:
            grade = 0
        try:
            data = my_col.find(myquery)[0]
            result = '基金代码：{}\n基金名称：{}\n净值估算：{}\n\n'.format(word['code'],data['基金名称'],data['估增长率'])
            rate = float(data['估增长率'].strip('%'))

            if rate <= grade:
                send_key = True
                key_word += result
            else:
                pass
        except:
            key_word += '建议删除此基金代码: {}\n\n'.format(word['code'])
    return key_word.strip('\n\n'), send_key

if __name__ == '__main__':
    # mongodb服务的地址和端口号
    my_Client = pymongo.MongoClient('mongodb://root:root.1234@111.229.98.184:27017')
    # my_Client = pymongo.MongoClient('mongodb://long:ailong.123@111.229.98.184:27017')
    # 连接到 基金用户 数据库
    my_db = my_Client["fund_login"]
    # 返回连接到db数据库
    col_list = my_db.list_collection_names()
    for login in col_list:
        print(login)
        # 收件人邮箱账号
        to_user = []
        # 必须列表形式
        to_user.append(login)

        mycol = my_db[login]
        code_list = fund_to_client(mycol)
        key_word,send_key = fund_to_guzhi(code_list)
        
        # print(key_word)
        if send_key:
            sendEmail(key_word, grade, to_user)
        else:
            print('it is OK ~ no plan at {}'.format(strToday))
