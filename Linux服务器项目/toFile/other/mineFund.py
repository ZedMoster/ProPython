from pymongo import MongoClient
import pandas as pd

def mmmm(df):

    # 统计非空值数量
    count = round(df['日增长率'].count(),0)
    # 汇总值
    sum = round(df['日增长率'].sum(),2)
    # 平均值
    mean = round(df['日增长率'].mean(),3)
    # 平均绝对偏差
    mad = round(df['日增长率'].mad(),3)
    # 算数中位数
    median = round(df['日增长率'].median(),3)
    # 最小值
    min = round(df['日增长率'].min(),3)
    # 最大值
    max = round(df['日增长率'].max(),3)
    # 众数
    mode = round(df['日增长率'].mode())
    # 贝塞尔校正的样本标准偏差
    std = round(df['日增长率'].std(),3)
    # 无偏方差
    var = round(df['日增长率'].var(),3)
    # 平均值的标准误差
    sem = round(df['日增长率'].sem(),3)
    # 样本偏度 (第三阶)
    skew = round(df['日增长率'].skew(),3)
    # 样本峰度 (第四阶)
    kurt = round(df['日增长率'].kurt(),3)

    # 样本分位数 (不同 % 的值)
    quantile_10 = round(df['日增长率'].quantile(.10),3)
    quantile_20 = round(df['日增长率'].quantile(.20),3)
    quantile_25 = round(df['日增长率'].quantile(.25),3)
    quantile_33 = round(df['日增长率'].quantile(.33),3)
    quantile_50 = round(df['日增长率'].quantile(.50),3)
    quantile_75 = round(df['日增长率'].quantile(.75),3)
    quantile_90 = round(df['日增长率'].quantile(.90),3)

    data = {
        'count': count,
        'sum': sum,
        'mean': mean,
        'min': min,
        'max': max,
        'std': std,
        'describe':{
            '10%': quantile_10,
            '20%': quantile_20,
            '25%': quantile_25,
            '33%': quantile_33,
            '50%': quantile_50,
            '75%': quantile_75,
            '90%': quantile_90,
        }
    }

    return data

def zero(x,y):
    for i in range(len(y)):
        if y[i] > 0:
            y1 = y[i-1]
            y2 = y[i]
            x1 = float(x[i-1].strip('%'))/100.0
            x2 = float(x[i].strip('%'))/100.0
            k = (y2-y1)/(x2-x1)
            b = y2 - k*x2
            x3 = (-b)/k
            q = (x3 - x1)/(x2 - x1)

            z0 = (i-1)+q
            word = str(int(round(x3, 2) * 100)) + '%'
            break
    return x3,word

client = MongoClient('111.229.98.184', 27017)

db = client['scrapy_CX']
mydb = client["scrapy_TTJJ_LSJZ"]

my_set = db['fund_base']

# 过滤条件 base ==[3.0,6.0] and total >= 20
myques = {"base":{"$in":(3.0,6.0)},'total':{'$gte':20}}

date = []

for i in my_set.find(myques).sort([('base',1),("total",1)]):
    _id = i['code']
    mycol = mydb[_id]
    df = pd.DataFrame(list(mycol.find().sort([('净值日期', -1)])))
    try:
        df[['日增长率', '单位净值', '累计净值']] = df[['日增长率', '单位净值', '累计净值']].apply(pd.to_numeric)
        df_des = mmmm(df)

        # 近30天的数据
        x = list(df_des['describe'].keys())
        y = list(df_des['describe'].values())
        z0, word = zero(x, y)

        # 增长率等于0 的概率值
        if z0 <= 0.47 and df_des['count'] > 1000:
            result = {
                '基金代码': i['code'],
                '基金名称': i['name'],
                '规模亿元': i['total'],
                '成立日期': i['setupday'],
                '类型分类': i['classify'],
                '负增长率': round(z0,2),
            }
            print(result)
            date.append(result)
    except:
        pass


dd = pd.DataFrame(date).sort_values('负增长率', ascending=True)
filename = 'grade/xml_morningstar.xlsx'

with pd.ExcelWriter(filename) as writer:
    # sheet name
    sheet_name = '成长型'
    columns  = ['基金代码','基金名称','类型分类','规模亿元','成立日期','负增长率']
    # 保存数据
    dd[columns].to_excel(writer, sheet_name=sheet_name, index=False)

    # 美化列宽
    writer.sheets[sheet_name].set_column("A:A", 10)
    writer.sheets[sheet_name].set_column("B:B", 50)
    writer.sheets[sheet_name].set_column("C:C", 25)
    writer.sheets[sheet_name].set_column("D:D", 10)
    writer.sheets[sheet_name].set_column("E:E", 11)
    writer.sheets[sheet_name].set_column("F:F", 10)



