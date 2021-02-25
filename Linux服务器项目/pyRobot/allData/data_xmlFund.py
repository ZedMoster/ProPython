import datetime
import pandas as pd
import os


def xmlFundEveryday(msg):
    '''
    获取每日基金推荐
    :param num: 出现次数大于num
    :return: 输出需要的内容
    '''
    num = msg.strip('xml').strip()

    # 获取当前时间日期
    now = datetime.datetime.today().strftime("%Y-%m-%d")
    try:
        word = now + "\n\n"
        # data = pd.read_excel(r"xml_outer.xlsx",dtype=str)
        data = pd.read_excel("/root/toFile/xml_outer.xlsx", dtype=str)
        data['date'] = data['基金代码'] + " -- " + data['基金名称'] + " -- " + data["出现次数"]

        if num == '':
            for i in range(len(data["出现次数"])):
                if int(data["出现次数"][i]) > 1:
                    word += str(data['date'][i]) + "\n"
        else:
            # 格式化内容输出
            for i in range(len(data["出现次数"])):
                if int(data["出现次数"][i]) == 1:
                    word += str(data['基金代码'][i] + " -- " + data['基金名称'][i]) + "\n"

        return word.strip("\n")
    except:
        return "数据读取错误...."


if __name__ == '__main__':
    li = xmlFundEveryday("xml")
    # print(li)
