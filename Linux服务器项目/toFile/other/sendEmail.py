# -*- coding: UTF-8 -*-
import smtplib
import datetime
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

# 日期
now = datetime.datetime.now()
strtime = str(now.strftime('%Y-%m-%d'))
strToday = str(now.strftime('%Y-%m-%d %H:%M:%S'))

# 发件人邮箱账号
my_sender = '1505636116@qq.com'
# 发件人邮箱密码
my_pass = 'aeodudlokpzlbafd'
# 收件人邮箱账号，我这边发送给自己
to_user = '1505636116@qq.com '.split()
# to_user = '1505636116@qq.com maxiaoyushi007@qq.com 522507683@qq.com'.split()


# 邮件标题
subject = strtime + '基金数据已归档整理'
# 邮件正文内容
msg = '''强烈注意!!\n过往业绩不预示其未来表现，市场有风险，投资需谨慎。'''
# 设置附件文件名称
path = '/root/toFile/grade/'
files = os.listdir(path)


def withFile(files):
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("From_xml", 'utf-8')
    message['To'] = Header("关注基金今日情况", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText(msg, 'plain', 'utf-8'))


    # 构造附件1，传送当前目录下的 test.txt 文件
    for file in files:
        try:
            att = readFile(file)
            message.attach(att)
        except:
            pass

    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, to_user, message.as_string())
        print("-- good job send Email at {}".format(strToday))
        return True
    except smtplib.SMTPException:
        print("** error send Email at {}".format(strToday))



def readFile(file):
    # 构造附件1，传送当前目录
    filepath = path + file
    att = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att["Content-Disposition"] = 'attachment; filename={}'.format(file)

    return att

if __name__ == '__main__':

    if len(files) != 0:
        t = withFile(files)
        if t:
            for file in files:
                filepath = path + file
                os.remove(filepath)
