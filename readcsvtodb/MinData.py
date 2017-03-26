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
from confandlog.log import *
from iolib.database.ToDataBase import *
from iolib.file.Path import *

def makeParam(param):
    '''
    获取window参数
    :param param: path string
    :return: string
    '''
    result1 = (param.split('.')[0])
    if result1[-2]=='1':
        return '15min'
    elif result1[-2] == '4':
        return 'day'
    else:
        return '5min'

def addInfo(param1, param2, param3):
    '''
    遍历文件夹，更新数据
    :param param1: path string
    :param param2: sql for select * from db
    :param param3: dbName
    :return:
    '''
    instance = Path(param1)
    result1 = instance.secondFile()

    for i in result1:
        print('正在更新 '+i+' 数据。。。')
        agent = i.split('/')[-1]
        result2 = instance.csvURL(i)    #result2:list

        for k in result2:
            recordcount = 0
            window = makeParam(k)
            currencyPair = (((k.split('/')[-1]).split('.')[0])[0:6]).lower()    #货币对都是小写

            try:
                '获取需要新增的DF，调用ToDataBase方法'
                df13 = pd.read_csv(k,names=['tradedate', 'tradetime', 'buy', 'highest', 'lowest', 'end', 'volume'], header=0)
                df22 = transform(df13)
                instance0 = DataBaseOperation()
                df20 = instance0.select(param2)    #'select * from eurcad_5min_1'
                df21 = newDate(df20, df22, agent, currencyPair, window)
            except:
                logging.warning('调用ToDataBase方法出错！')

            count = df21['date'].count()

            if count>0:
                df21['agent'] = agent    #SettingWithCopyWarning
                df21['window'] = window
                df21['pair'] = currencyPair

                '需要检测数据就注释掉instance0.addToDB，logging'

                instance0.addToDB(df21, param3)    #inset record

            recordcount += count
            logging.info(agent+'-'+currencyPair+'-'+window+'新增数据：'+str(recordcount))
            # print(agent+'-'+currencyPair+'-'+window+'新增数据：'+str(recordcount))

            #为DF新增列，然后保存




def main():
    param1 = '/home/hadoop/Files/Data/test/data1'
    param2 = 'select * from minrecord'
    param3 = 'minrecord'
    # addInfo(param1, param2, param3)
if __name__ == '__main__':
    main()

