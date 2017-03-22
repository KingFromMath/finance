# -*- coding: utf-8 -*-
"""
create at:17-3-22 上午11:28
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
# import psycopg2
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


def transform(param):
    '''
    替换和补全DF（把日期和时间弄在一起），合并列后返回新的DF
    :param param: dataframe
    :return: dataframe
    '''
    '替换和补全'
    param['tradedate'] = param['tradedate'].map(lambda x: x.replace('.','-'))
    param['tradetime'] = param['tradetime'].map(lambda x: x+':00')

    '遍历每一行，拼接tradedate和tradetime，然后返回新的DF'
    df9 ={'date': pd.Series([param['tradedate'][i]+' '+param['tradetime'][i] for i in range(0,param['tradedate'].count())])}    #TODO  可以看看DF有没有内置接口

    '合并DF，截取需要的列'
    df11 = pd.concat([param, pd.DataFrame(df9)], axis=1)
    df12 = df11.loc[:,['date','buy', 'highest', 'lowest', 'end', 'volume']]

    '转换数据类型为日期时间型'
    df12['date'] = df12['date'].astype(np.datetime64)

    return df12

def newDate(param1, param2, param3, param4, param5):
    '''
    获取csv中的更新数据

    :param param1: DF from DB
    :param param2: DF from csv
    :param param3: agent
    :param param4: pair
    :param param5: window
    :return: DF
    '''
    '多条件筛选，避免先插入的数据影响后续判断'
    x = param1.loc[(param1['agent'] == param3) & (param1['pair'] == param4) & (param1['window'] == param5), :]
    '如果数据库中没有相应的值就直接返回csv DF'
    if x['date'].count()>0:
        '排序，获取最近的日期'
        dfsort = x.sort_values('date', ascending=False)
        df14 = dfsort.head(1)
        df15 = df14.stack()[1]    #df15:<class 'pandas.tslib.Timestamp'>

        df16 = param2[param2.date > df15]    #TODO 这里把date写死在程序里了
        return df16
    else:
        return param2

class DataBaseOperation(object):
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:123456@localhost/postgres')
        # engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/postgres')

    def select(self, param):
        '''
        从DB中查询数据
        :param param: sql string
        :return:
        '''
        with self.engine.connect() as conn, conn.begin():
            df6 = pd.read_sql(param, self.engine)    #'select * from eurcad_5min_1'

        return df6

    def addToDB(self, param1, param2):
        '''
        保存DF到table
        :param param1: DF
        :param param2: tableName String
        :return:
        '''
        param1.to_sql(param2, self.engine, if_exists='append')    #if_exists='append'表示追加数据



def main():
    'transform测试'
    df13 = pd.read_csv('/home/hadoop/Files/Data/test/USDCNH5.csv',
                  names=['tradedate','tradetime','buy', 'highest', 'lowest', 'end', 'volume'], header=0)
    df22 = transform(df13)

    'DataBaseOperation测试'
    instance = DataBaseOperation()
    df20 = instance.select('select * from minrecord')
    # print(df20)

    'lastDate测试'
    df21 = newDate(df20, df22, 'xm', 'usdchf', '15min')
    print(df21)

    'general test'
    # instance = DataBaseOperation()
    # df23 = instance.select('select * from minrecord')
    # x = df23.loc[(df23['agent']=='xm')&(df23['pair']=='eurchf')&(df23['window']=='15min'),:]
    # print(x['date'].count())







if __name__ == '__main__':
    main()

'''
API:


'''