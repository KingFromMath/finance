# -*- coding: utf-8 -*-
"""
create at:17-3-21 上午10:52
create by:duanyuping
create for:
  ┏┓   ┏┓
 ┏┛┻━━━┛┻┓
 ┃   ☃  ┃
 ┃ ┳┛ ┗┳ ┃
 ┃   ┻   ┃
 ┗━┓   ┏━┛
   ┃   ┗━━━┓
   ┃ 神兽保佑 ┣┓
   ┃ 永无BUG！ ┏┛
   ┗┓┓┏━┳┓┏┛
    ┃┫┫  ┃┫┫
    ┗┻┛  ┗┻┛
"""
import psycopg2
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


'还不能没有pd.Categorical(["XM","FOREX"]'
# df2 = pd.DataFrame({  'tradedate' : '2017-03-21',
#                       'tradetime' : '08:00:03',
#                       'buy' : 5.343,
#                       'highest' : 35.3432,
#                       'lowest':0.9232,
#                       'end':1.2,
#                       'volume':pd.Categorical([2.1, 1.0])
#                        })

# print(df2.loc[:,['tradedate','tradetime']])
df13 = pd.read_csv('/home/hadoop/Files/Data/USDCNH5.csv',
                  names=['tradedate','tradetime','buy', 'highest', 'lowest', 'end', 'volume'], header=0)

# print(df3)

engine = create_engine('postgresql://postgres:123456@localhost/postgres')
# engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/postgres')
with engine.connect() as conn, conn.begin():
    # data = pd.read_sql_table('eurcad_daily', conn)

    # df3.to_sql('eurcad_5min_4', engine)    #if_exists='append'面临字段不统一的问题
    df6 = pd.read_sql('select * from eurcad_5min_1',engine)

def transform(df6):
    f = lambda x: x.replace('.','-')
    f1 = lambda x: x+':00'
    df6['tradedate'] = df6['tradedate'].map(f)
    df6['tradetime'] = df6['tradetime'].map(f1)

    df7 = df6['tradedate']
    df8 = df6['tradetime']

    df9 ={'date': pd.Series([df7[i]+' '+df8[i] for i in range(0,9)])}
    df10 = pd.DataFrame(df9)

    df11 = pd.concat([df6, df10], axis=1)
    df12 = df11.loc[:,['date','buy', 'highest', 'lowest', 'end', 'volume']]

    df12['date'] = df12['date'].astype(np.datetime64)
    # print(df12.dtypes)
    # print(df12)

    return df12


dfcsv = transform(df13)

dfsort = df6.sort_values('date',ascending=False)
# print(dfsort.reindex([i for i in range(9)]))
# print(dfsort)
df14 = (dfsort.head(1))
# print(df14.stack()[1])
# print(type(df14.stack()[1]))
# print(type(df14.at[0,'date']))
# print(type(dfsort.at[0,'date']))    #<class 'pandas.tslib.Timestamp'>

df15 = df14.stack()[1]

df16 = dfcsv[dfcsv.date >= df15]
print(df6)



with engine.connect() as conn, conn.begin():
    df16.to_sql('eurcad_5min_1', engine, if_exists='append')    #if_exists='append'面临字段不统一的问题

#运行很完美，明天进行封装






















