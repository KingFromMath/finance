# -*- coding: utf-8 -*-
"""
create at:17-3-22 下午2:01
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
from readcsvtodb.MinData import  addInfo
from web.CurrencyTrade import *

'''
更新5min/15min/day数据
'''
param1 = '/home/duanyuping/Files/input/currency_min'    #文件结构：data1/xm/ERUCAD15.csv
param2 = 'select * from minrecord'
param3 = 'minrecord'
# addInfo(param1, param2, param3)


'''
更新交易记录
'''
webContent("/home/duanyuping/Files/input/finance/fxcm.htm", 'currencytrades')

