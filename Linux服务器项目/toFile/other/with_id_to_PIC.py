import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import datetime
import pymongo


def to_client(_key, _id):
    # mongodb服务的地址和端口号
    myClient = pymongo.MongoClient("127.0.0.1", 27017)
    # 连接到 天天基金 数据库
    mydb = myClient["fund_history"]
    mycol = mydb[_id]
    df = pd.DataFrame(list(mycol.find({},{'_id':0}))).sort_values(by="净值日期" , ascending=False)
    df[['日增长率','单位净值','累计净值']] = df[['日增长率','单位净值','累计净值']].apply(pd.to_numeric)
    df_30 = df.iloc[:_key].sort_values(['净值日期'], ascending=True)

    return df_30

def toplt_fig(_key, _id):
    df_30 = to_client(_key, _id)
    # describe
    _rate = round((df_30['日增长率'] > 0).sum() / df_30['日增长率'].count(), 2)
    _mean = df_30['日增长率'].describe().iloc[1].round(2)
    _std = df_30['日增长率'].describe().iloc[2].round(2)
    _min = df_30['日增长率'].describe().iloc[3].round(2)
    _max = df_30['日增长率'].describe().iloc[7].round(2)
    _25 = df_30['日增长率'].describe().iloc[4].round(2)
    _50 = df_30['日增长率'].describe().iloc[5].round(2)
    _75 = df_30['日增长率'].describe().iloc[6].round(2)

    # 默认字体  & '-'负号
    #matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    #matplotlib.rcParams['font.family'] = 'sans-serif'
    #matplotlib.rcParams['axes.unicode_minus'] = False

    # 日增长率
    fig_rate = plt.figure(figsize=(14, 5), dpi=150)

    # 近30天的数据
    plt.plot(df_30['净值日期'], df_30['日增长率'], color='b', linewidth=1.5, label="rate")

    x = range(1, _key + 1, 1)
    plt.xticks(df_30['净值日期'], x)

    # 使用xlim()/ylim()调整坐标轴
    plt.xlabel('datetime', fontsize=14)
    plt.ylabel('rate', fontsize=14)

    # 添加标题
    title_1 = '{}_center{}_rate'.format(_id,_key)
    plt.title(title_1, fontsize=16)

    # 添加图例
    plt.legend(loc='upper left', fontsize=12)

    # 设置网格线
    plt.grid(True, ls=':', color='g', alpha=1)
    plt.axhline(y=0, c='r', ls='--', lw=3)



    # 散点图
    plt.scatter(df_30['净值日期'], df_30['日增长率'], c='0.3', label='scatters')
    # 去掉图形上边和右侧的边框
    for spine in plt.gca().spines.keys():
        if spine == 'top' or spine == 'right':
            plt.gca().spines[spine].set_color('none')

    # 添加文字说明
    plt.text(-1, _min + _std,
             r'$\sigma={}$  mean={}  std={}  min={}  max{}  25%={}  50%={}  75%={}'.format(_rate, _mean, _std, _min,
                                                                                           _max, _25, _50, _75), alpha=0.4)

    # 单位净值
    fig_jz = plt.figure(figsize=(13, 5), dpi=150)

    # 近30天的数据
    plt.plot(df_30['净值日期'], df_30['单位净值'], color='r', linewidth=1.5, label="lsjz")
    x = range(1, _key + 1, 1)
    plt.xticks(df_30['净值日期'], x)

    # 使用xlim()/ylim()调整坐标轴
    plt.xlabel('datetime', fontsize=14)
    plt.ylabel('rate', fontsize=14)

    # 添加标题
    title_2 = '{}_center{}_lsjz'.format(_id,_key)
    plt.title(title_2, fontsize=16)

    # 添加图例
    plt.legend(loc='upper left', fontsize=12)

    # 设置网格线
    plt.grid(True, ls=':', color='g', alpha=0.5)
    # plt.axhline(y=0, c='r', ls='--', lw=2)

    # 散点图
    plt.scatter(df_30['净值日期'], df_30['单位净值'], c='0.3', label='scatters')

    # 去掉图形上边和右侧的边框
    for spine in plt.gca().spines.keys():
        if spine == 'top' or spine == 'right':
            plt.gca().spines[spine].set_color('none')

    # plt.show()

    fig_rate.savefig('grade/{}.png'.format(title_1))
    fig_jz.savefig('grade/{}.png'.format(title_2))

if __name__ == '__main__':
    _key = 60
    _id = '162703'

    toplt_fig(_key,_id)
