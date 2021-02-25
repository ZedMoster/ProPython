#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from with_id_to_describe import *
from with_id_to_PIC import *
import pymongo

class ttjj_group_to_excel:
    '''
    分析生成表格
    '''

    def __init__(self):
        # mongodb服务的地址和端口号
        self.myClient = pymongo.MongoClient('mongodb://long:ailong.123@localhost:27017')
        # 连接到 fund 数据库
        self.mydb = self.myClient["fund_data"]

    def to_fund_dtph(self):
        # 定投排行
        mycol = self.mydb['fund_dtph']

        data_0 = pd.DataFrame(list(mycol.find()))
        # data_0.head()

        # 删除_id列
        del data_0['_id']


        ## 评级为五星 & 定投时间超过五年
        df_0 = data_0[(data_0['上海证券评级'] == '★★★★★') & (data_0['近5年定投收益'] != '--')]

        return df_0


    def to_fund_rate(self):
        # 四维等级
        mycol = self.mydb['fund_rate']

        data_1 = pd.DataFrame(list(mycol.find()))

        # 删除_id列
        del data_1['_id']

        # 设置筛选条件
        # 基金规模大于8亿元 & 三年内评级全为优秀
        key1_0 = data_1['基金规模'].map(lambda x : x != '--' and float(x) >= 8)

        key1_1 = data_1['最近1周_k'].map(lambda x : x == '优秀')
        key1_2 = data_1['最近1月_k'].map(lambda x : x == '优秀')
        key1_3 = data_1['最近3月_k'].map(lambda x : x == '优秀')
        key1_4 = data_1['最近6月_k'].map(lambda x : x == '优秀')
        key1_5 = data_1['今年以来_k'].map(lambda x : x == '优秀')
        key1_6 = data_1['最近1年_k'].map(lambda x : x == '优秀')
        key1_7 = data_1['最近2年_k'].map(lambda x : x == '优秀')
        key1_8 = data_1['最近3年_k'].map(lambda x : x == '优秀')

        # 设置过滤条件
        df_1 = data_1[key1_0 & key1_1 & key1_2 & key1_3 & key1_4 & key1_5 & key1_6 & key1_7 & key1_8]

        return df_1




    def to_fund_zqpj(self):
        # 证券评级
        mycol = self.mydb['fund_zqpj']

        data_2 = pd.DataFrame(list(mycol.find()))

        # print(data_2.shape)

        # 删除_id列
        del data_2['_id']

        # 设置筛选条件
        # 三家证券公司中对该基金5星评价 >= 2
        key2_1 = data_2['5星评价'].map(lambda x : x >= '2')

        df_2 = data_2[key2_1]

        return df_2


    def to_fund_jjpj(self):
        # 基金排行
        mycol = self.mydb['fund_jjph']

        data_3 = pd.DataFrame(list(mycol.find()))

        # 删除_id列
        del data_3['_id']

        # data_3.head()

        # 设置筛选条件
        # 基金累计净值大于4.0
        key3_1 = data_3['累计净值'].map(lambda x : x >= '4.0')

        df_3 = data_3[key3_1]
        # df_3[['基金代码','基金名称','单位净值','累计净值']]
        return df_3



    def to_fund_jjjl(self):
        # 基金经理
        mycol = self.mydb['fund_jjjl']

        data_5 = pd.DataFrame(list(mycol.find()))

        # 删除_id列
        del data_5['_id']

        # data_5.head()

        # 设置筛选条件
        # 从业时间大于1000天，现任基金总规模大于100亿元，现任基金最佳回报大于 50%
        key5_1 = data_5['从业时间'].map(lambda x : x >= 1000)
        key5_2 = data_5['现任基金总规模'].map(lambda x : x >= 300.0)
        key5_3 = data_5['现任基金最佳回报'].map(lambda x : x >= 50.0)

        df_5 = data_5[key5_1 & key5_2 & key5_3]

        return df_5




    def to_fund_company(self):
        # 公司评级
        mycol = self.mydb['fund_company']

        data_6 = pd.DataFrame(list(mycol.find()))

        # 删除_id列
        del data_6['_id']

        # data_6.head()

        # 设置筛选条件
        # 天相评级 ★存在 并且管理规模 大于等于1000亿元
        key6_1 = data_6['天相评级'].map(lambda x : '★' in x)
        key6_2 = data_6['管理规模'].map(lambda x : x != None and float(x) >= 1000)

        df_6 = data_6[key6_1 & key6_2]

        return df_6


    def group_1(self,df_0,df_1,df_2,df_3,df_5,df_6):
        ## 基金排行 & 定投排行

        # 基金代码
        dx_1 = pd.merge(df_3,df_0,on=['基金代码','基金名称','手续费','单位净值','今日日期','是否可购'])

        # # 查看列名
        # print(dx_1.columns)

        dx_1 = dx_1[['基金代码','基金名称']]

        return dx_1


    def group_2(self,df_0,df_1,df_2,df_3,df_5,df_6):
        ## 基金排行 & 四维等级

        # 基金代码
        dx_2 = pd.merge(df_3,df_1,on=['基金代码','基金名称','成立日期'])

        # # 查看列名
        # print(df_001.columns)


        dx_2 = dx_2[['基金代码','基金名称']]

        # 提取代码
        # for a in df_001['基金代码']:
        #     print(a)

        return dx_2



    def group_3(self,df_0,df_1,df_2,df_3,df_5,df_6):
        ## 基金排行 & 证券排行

        # 基金代码
        dx_3 = pd.merge(df_3,df_2,on=['基金代码','基金名称','是否可购','手续费'])

        # # 查看列名
        # print(dx_3.columns)


        dx_3 = dx_3[['基金代码','基金名称']]

        return dx_3



    def group_4(self,df_0,df_1,df_2,df_3,df_5,df_6):
        ## 基金经理 & 基金公司

        # 基金公司_id
        dx_4 = pd.merge(df_6,df_5,on=['基金公司_id'])

        # # 查看列名
        # print(df_004.columns)


        dx_4 = dx_4[['基金代码','基金名称']]



        # df_004[['公司_id','公司名称','个人_id','姓名','现任最佳基金_id','现任最佳基金名称']]

        return dx_4


    def group_5(self,df_0,df_1,df_2,df_3,df_5,df_6):
        ## 基金经理 & 证券评级

        # 基金代码
        dx_5 = pd.merge(df_5,df_2,on=['基金代码','基金经理','基金公司_id','基金经理_id','基金名称'])

        # # 查看列名
        # print(dx_5.columns)

        dx_5 = dx_5[[ '基金代码', '基金名称']]

        return dx_5


    def group_6(self,df_0,df_1,df_2,df_3,df_5,df_6):
        ## 基金经理 & 四维评级

        # 基金经理
        dx_6 = pd.merge(df_5,df_1,on=['基金经理','基金代码','基金名称'])

        # # 查看列名
        # print(dx_6.columns)

        dx_6 = dx_6[['基金代码','基金名称']]

        return dx_6


    def group_7(self,df_0,df_1,df_2,df_3,df_5,df_6):
        ## 基金经理 & 基金评级

        # 基金代码
        dx_7 = pd.merge(df_5,df_3,on=['基金名称','基金代码'])

        # # 查看列名
        # print(dx_7.columns)



        dx_7 = dx_7[['基金代码','基金名称']]

        return dx_7


    def to_group(self,dx_1,dx_2,dx_3,dx_4,dx_5,dx_6,dx_7):
        _dx = pd.concat([dx_1,dx_2,dx_3,dx_4,dx_5,dx_6,dx_7],axis=0)

        # # 去重
        # _dxEveryone = _dx.drop_duplicates()

        # 汇总
        dxGroup = _dx.groupby(['基金代码','基金名称'], as_index=False).size().sort_values(ascending=False).reset_index(name='出现次数')

        # _dxGroup = dxGroup[dxGroup['出现次数'] >1]

        return dxGroup


    def to_excel_inter(self,df_0,df_1,df_2,df_3,df_5,df_6):

        # 写入初步筛选的数据
        filename1 = 'toFile/xml_inter.xlsx'

        with pd.ExcelWriter(filename1) as writer1:
            # sheet name
            name0 = '定投排行'
            name1 = '四维评级'
            name2 = '证券评级'
            name3 = '基金排行'
            name5 = '基金经理'
            name6 = '基金公司'

            # 列排序
            columns_0 = "基金代码 基金名称 单位净值 今日日期 近1年定投收益 近2年定投收益 近3年定投收益 近5年定投收益 上海证券评级 是否可购 手续费".split()
            columns_1 = "基金代码 基金名称 基金类型 基金经理 基金规模 管理公司 最近1周_k 最近1月_k 最近3月_k 最近6月_k 今年以来_k 最近1年_k 最近2年_k 最近3年_k".split()
            columns_2 = "基金代码 基金名称 基金类型 基金经理 基金经理_id 5星评价 上海证券 招商证券 济安金信 公司简称 是否可购 手续费".split()
            columns_3 = "基金代码 基金名称 今日日期 单位净值 累计净值 日增长率 最近1周 最近1月 最近3月 最近6月 今年以来 最近1年 最近2年 最近3年 成立日期 成立至今 是否可购 手续费".split()
            columns_5 = "基金经理 基金经理_id 所属公司 基金公司_id 从业时间 基金代码 基金名称 现任基金最佳回报 现任基金总规模 现任基金 管理基金_id".split()
            columns_6 = "基金公司 基金公司_id 总经理 数据日期 天相评级 成立日期 基金数量 管理规模 ".split()

            # 保存数据
            df_0.to_excel(writer1, sheet_name=name0, index=False, columns=columns_0)
            df_1.to_excel(writer1, sheet_name=name1, index=False, columns=columns_1)
            df_2.to_excel(writer1, sheet_name=name2, index=False, columns=columns_2)
            df_3.to_excel(writer1, sheet_name=name3, index=False, columns=columns_3)
            df_5.to_excel(writer1, sheet_name=name5, index=False, columns=columns_5)
            df_6.to_excel(writer1, sheet_name=name6, index=False, columns=columns_6)

            # # 美化列宽
            # writer1.sheets[name0].set_column("B:B", 30)
            # writer1.sheets[name1].set_column("B:B", 30)
            # writer1.sheets[name2].set_column("B:B", 30)
            # writer1.sheets[name3].set_column("B:B", 30)
            # writer1.sheets[name5].set_column("G:G", 30)
            # writer1.sheets[name6].set_column("A:A", 30)

    def to_excel_outer(self,dxGroup=None):
        # 筛选过后的数据合并
        filename2 = 'toFile/xml_outer.xlsx'

        with pd.ExcelWriter(filename2) as writer2:

            # sheet name
            name = '长期表现优异基金'

            # 保存数据
            dxGroup.to_excel(writer2, sheet_name=name, index=False)

            # # 美化列宽
            # writer2.sheets[name].set_column("B:B", 30)
            
    def withID_fig(self,data=None):
        _dxGroup = data[data['出现次数'] >1]
        # print(_dxGroup['基金代码'])
        for code in _dxGroup['基金代码']:
            try:
                mainID(code)
                toplt_fig(30,code)
            except:
                print('**error to file')

    def main(self):
        try:
            df_0 = self.to_fund_dtph()
            df_1 = self.to_fund_rate()
            df_2 = self.to_fund_zqpj()
            df_3 = self.to_fund_jjpj()
            df_5 = self.to_fund_jjjl()
            df_6 = self.to_fund_company()

            dx_1 = self.group_1(df_0,df_1,df_2,df_3,df_5,df_6)
            dx_2 = self.group_2(df_0,df_1,df_2,df_3,df_5,df_6)
            dx_3 = self.group_3(df_0,df_1,df_2,df_3,df_5,df_6)
            dx_4 = self.group_4(df_0,df_1,df_2,df_3,df_5,df_6)
            dx_5 = self.group_5(df_0,df_1,df_2,df_3,df_5,df_6)
            dx_6 = self.group_6(df_0,df_1,df_2,df_3,df_5,df_6)
            dx_7 = self.group_7(df_0,df_1,df_2,df_3,df_5,df_6)

            dxGroup = self.to_group(dx_1,dx_2,dx_3,dx_4,dx_5,dx_6,dx_7)

            # 导出图片
##            self.withID_fig(dxGroup)

            self.to_excel_inter(df_0,df_1,df_2,df_3,df_5,df_6)
            self.to_excel_outer(dxGroup)

            return True

        except Exception as e:
            print("Oh!NO! have error :",e)



if __name__ == '__main__':
    ttjj_group_to_excel = ttjj_group_to_excel()
    start = ttjj_group_to_excel.main()
    path = 'toFile'
    if not os.path.exists(path):
        os.makedirs(path)
    if start:
        print("-- good job to files")
