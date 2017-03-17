# -*- coding: utf-8 -*-
"""
create at:17-2-18 上午11:46
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
from pandas import Series, DataFrame
import pandas as pd
import pandas.io.sql as sql
import pymysql
import re
import json
import datetime

connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='duanyuping',
                                          db='Finance',
                                          charset='utf8',
                                          cursorclass=pymysql.cursors.DictCursor)


try:
    with connection.cursor() as cursor:
        sql = "select buytime, agent from EURCAD_Daily "
        # "select buytime, agent from (select *, row_number() over(partition by agent  order by id desc) from EURCAD_Daily )"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
finally:
    connection.commit()

#预定义数据结构
lastDataJson = {'FXCM': [{'EURCAD_Daily': '2017-02-28'}, {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''},
              {'GBPUSD_Daily': ''}, {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''}, {'USDCNH_Daily': ''}], 'FOREX': [{'EURCAD_Daily': ''},
            {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''}, {'GBPUSD_Daily': ''},
            {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''}, {'USDCNH_Daily': ''}], 'XM': [{'EURCAD_Daily': ''}, {'EURCHF_Daily': ''},
            {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''}, {'GBPUSD_Daily': ''}, {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''},
            {'USDCNH_Daily': ''}]}

def identify(argList, agent, tables, buytime):
    '''
    识别输入的记录是否是最近的，若是则记录下来
    :param argList: 预定义数据结构，和lastdata.json相同
    :param agent:
    :param table: [EURCAD_Daily,....]
    :param buytime:
    :return:
    '''
    global param    #测试用变量
    if argList[agent]:    #argList[agent]: [{'EURCAD_Daily': ''}, {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''},
        # print(argList[agent])
        for dictOne in argList[agent]:    #z: {'EURCAD_Daily': ''}
            # print(z)
            for table in tables:    #tables是一个list
                if table in dictOne:    #判断key是否在dict中
                    if len(dictOne[table]) == 0:    #{'EURCAD_Daily': ''}
                        param = 1
                        dictOne[table] = str(buytime)
                    else:
                    # print(datetime.datetime.strptime(str(buytime),'%Y-%m-%d'))
                    # print(datetime.datetime.strptime(z[table],'%Y-%m-%d'))
                        if datetime.datetime.strptime(str(buytime),'%Y-%m-%d') >= datetime.datetime.strptime(dictOne[table],'%Y-%m-%d'):    #datetime.datetime.strptime(z[table],'%Y-%m-%d')
                            param = 3
                            dictOne[table] = str(buytime)
                        else:
                            param = 4
                            pass
            else:
                pass
    else:
        pass
    # print(argList)
    return param


def updateRecords(jsonFile, lastDataJson):
    with open(jsonFile) as json_file:
        data = json.load(json_file)
    dbList = data['Currency']    #数据库列表

    for i in results:
        agent = i['agent']
        buytime = i['buytime']
        #没有就插入，有就比较后在插入
        print(identify(lastDataJson,agent,dbList,buytime))


# object = sql.read_frame('select id, buytime, agent from EURCAD_Daily',connection)
# result = pd.read_sql('select id, buytime, agent from EURCAD_Daily', connection)
# print(result)
# print(result['endprice'])
# print(result.max(axis=0, skipna=False))

# print(result.sum(axis=1, skipna=False))

from pandas_datareader.oanda import get_oanda_currency_historical_rates
# start, end = "2016-11-11", "2017-02-16"
# quote_currency = "USD"
# base_currency = ["EUR", "GBP", "JPY"]
# df_rates = get_oanda_currency_historical_rates(
#             start, end,
#             quote_currency=quote_currency,
#             base_currency=base_currency
#         )
# print(df_rates)


# url = '/home/duanyuping/Files/input/finance/USDJPY1440.csv'
# target = re.match('[A-Z]+',(url.split('/')[-1]).split('.')[0])
# print(target.group()+'_Daily')

# data = {'FXCM': [{'EURCAD_Daily': '123'}, {'EURCHF_Daily': '2345'}, {'EURGBP_Daily': 'sdgs'}]}
#
#
# with open('/home/duanyuping/PycharmProjects/finance/data/lastdata.json') as json_file:
#     data = json.load(json_file)
#     # json_file.write(json.dumps(data))
# print(data)
#
# s = {'FXCM': [{'EURCAD_Daily': ''}, {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''},
#               {'GBPUSD_Daily': ''}, {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''}, {'USDCNH_Daily': ''}], 'FOREX': [{'EURCAD_Daily': ''},
#             {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''}, {'GBPUSD_Daily': ''},
#             {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''}, {'USDCNH_Daily': ''}], 'XM': [{'EURCAD_Daily': ''}, {'EURCHF_Daily': ''},
#             {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''}, {'GBPUSD_Daily': ''}, {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''},
#             {'USDCNH_Daily': ''}]}



# import os
# import os.path
# rootdir = "/home/duanyuping/Files/input/currency"                                   # 指明被遍历的文件夹
#
# for parent,dirnames,filenames in os.walk(rootdir):   #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
#     # print(parent)
#     for dirname in  dirnames:                       #输出文件夹信息
#         print("parent is:" + parent)
#         print("dirname is" + dirname)
# #
#     for filename in filenames:                        #输出文件信息　
#         print("the full name of the file is:" + os.path.join(parent,filename)) #输出文件路径信息
#         print("parent is: " + parent)
#         print("filename is:" + filename)

# import datetime
# if datetime.datetime.strptime('2017-02-01','%Y-%m-%d') < datetime.datetime.strptime('2017.02.05','%Y.%m.%d'):
#     print('good')
