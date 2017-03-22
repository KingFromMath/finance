# -*- coding: utf-8 -*-
"""
create at:17-3-22 上午10:47
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
from iolib.database.ToDataBase import *
from iolib.file.Path import *

def makeParam(param):
    result1 = (param.split('.')[0])
    if result1[-2]=='15':
        return '15min'
    else:
        return '5min'

def addInfo(param1):
    instance = Path(param1)
    result1 = instance.secondFile()

    for i in result1:
        agent = i.split('/')[-1]
        result2 = instance.csvURL(i)    #result2:list

        for k in result2:
            window = makeParam(k)
            print(window)


def mian():
    path = '/home/hadoop/Files/Data/test/data1'
    addInfo(path)

if __name__ == '__main__':
    main()