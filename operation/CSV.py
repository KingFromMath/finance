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

'更新5min/15min数据'
param1 = '/home/hadoop/Files/Data/test/data1'
param2 = 'select * from minrecord'
param3 = 'minrecord'
addInfo(param1, param2, param3)
