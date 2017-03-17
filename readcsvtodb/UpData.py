# -*- coding: utf-8 -*-
"""
create at:17-2-18 下午8:25
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
import csv
import datetime
import json

from readcsvtodb.DBLink import DBlink
from confandlog.log import *

# class UpDate(object):
#     '''
#     读取数据更新文件，更新数据库数据，准确地说是插入新数据
#     '''
#     def __init__(self, csvfile):
#         '''
#         :param csvfile: '/home/duanyuping/Files/input/EURUSD1440.csv'
#         '''
#         self.csvfile = csvfile
#
#     def UpdateRate(self, row):
#         '''
#         更新rate数据
#         :return:
#         '''
#         instanceDB = DBlink(row[1])
#         try:
#             print('正在插入数据： '+str(row))
#             instanceDB.addRataData(datetime.datetime.strptime(row[3],'%Y.%m.%d'),float(row[4]),float(row[5]),float(row[6]),float(row[7]),int(row[8]))
#
#         except:
#             # logging.warning('插入数据出错: '+str(row))
#             pass
#
#     def UpdateMain(self):
#         '''
#         新增数据更新时，在try模块的条件语句中新增任务模块
#         :return:
#         '''
#         with open(self.csvfile, newline='') as csvline:
#             spamreader = csv.reader(csvline)
#             for row in spamreader:
#                 try:
#                     # print(str(row))
#                     if row[0]=='Rate' and row[2]=='1':
#                         self.UpdateRate(row)
#                         print('正在更新'+str(row[1])+'数据')
#                     elif row[0]=='' and row[2]=='':
#                         print(print('正在更新'+str(row[1])+'数据'))
#                     else:
#                         print('没有数据需要更新！')
#                 except:
#                     # logging.warning('插入数据出错: ' + str(row))
#                     pass
'''判断数据是否已经存在'''
class Identify(object):
    '''
    识别记录是否在数据库已存在，1表示不存在，0表示存在
    '''
    def __init__(self, agent, currencyDB, date, jsonURL, today):
        '''

        :param agent: 代理商
        :param currency: 货币对数据库：'EURUSD_Daily'
        :param date: 需比对数据的日期
        :param jsonURL:
        :param today: 下载外汇csv当天的日期
        '''
        self.agent = agent
        self.currency = currencyDB
        self.date = date
        self.jsonURL = jsonURL
        self.today = today

    def readJson(self):
        '''
        读取lastdata.json文件
        :return: json字符串  #{'FXCM': [{'EURCAD_Daily': ''}, {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''},
        '''
        with open(self.jsonURL) as jsonString:
            jsonData = json.load(jsonString)
        return jsonData

    def identfyFunction(self):
        '''
        首先判断代理商是否在json中，然后找到对应的代理商数据，在调用identifyCurrency函数作进一步的判断
        :return:
        '''
        # print(self.agent,self.currency,self.date,self.jsonURL,self.today)
        identifyVale = 0
        jsonData = self.readJson()
        # print(jsonData)
        if self.agent in jsonData:    #判断代理商是否在序列中
            currencyList = jsonData[self.agent]     #获取代理商对应的货币对列表
            identifyVale = self.identifyCurrency(currencyList)
        else:
            pass

        return identifyVale

    def identifyCurrency(self, currencyList):
        '''
        对给定代理商的数据进行遍历判断
        :param currencyList: 给定代理商对应的货币对数据，[{'EURCAD_Daily': ''}, {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''},
        :return:
        '''
        returnVlaue = 0
        for currency in currencyList:
            # print(list(currency.values())[0], self.date)
            # print(datetime.datetime.strptime(self.today,'%Y-%m-%d'), datetime.datetime.strptime(self.date,'%Y.%m.%d'))
            if list(currency.keys())[0] == self.currency:    #判断是否是需要比对的货币对，是才进行下一步
                if datetime.datetime.strptime(self.date,'%Y.%m.%d') == datetime.datetime.strptime(self.today,'%Y-%m-%d'):    #由于存在时差，下载的外汇数据可能可能包含当天正在交易的情况，所以当天的数据一般不插入数据库，这个应放在前面
                    returnVlaue = 0
                    # print(1)
                    break    #不设置break会导致后面的覆盖前面的rerturnVale值
                elif len(list(currency.values())[0]) == 0:  # 用来判断的json中没有日期表示该数据尚未储存到数据库中，即默认保存所有的数据
                    returnVlaue = 1
                    # print(2)
                    break
                elif datetime.datetime.strptime(list(currency.values())[0],'%Y-%m-%d') < datetime.datetime.strptime(self.date,'%Y.%m.%d'):    #比较日期，输入的日期比现有的日期大才表示是新数据
                    returnVlaue = 1
                    # print(3)
                    break
                # else:
                #     returnVlaue = 0
                #     print(4)
                #     break
            else:
                returnVlaue = 0
                # print(5)
        return returnVlaue


'''获取最近的数据记录'''
#预定义数据结构
lastDataJson = {'FXCM': [{'EURCAD_Daily': ''}, {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''},
              {'GBPUSD_Daily': ''}, {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''}, {'USDCNH_Daily': ''}], 'FOREX': [{'EURCAD_Daily': ''},
            {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''}, {'GBPUSD_Daily': ''},
            {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''}, {'USDCNH_Daily': ''}], 'XM': [{'EURCAD_Daily': ''}, {'EURCHF_Daily': ''},
            {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''}, {'GBPUSD_Daily': ''}, {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''},
            {'USDCNH_Daily': ''}]}

def identify(argList, agent, table, buytime):
    '''
    识别输入的记录是否是最近的，若是则记录下来
    :param argList: 预定义数据结构，和lastdata.json相同
    :param agent:
    :param table: [EURCAD_Daily,....]
    :param buytime:
    :return:
    '''
    global param    #测试用变量
    # print(argList, agent)
    if argList[agent]:    #argList[agent]: [{'EURCAD_Daily': ''}, {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''},
        # print(argList[agent])
        for dictOne in argList[agent]:    #z: {'EURCAD_Daily': ''}
            if table in dictOne:    #判断key是否在dict中
                if len(dictOne[table]) == 0:    #{'EURCAD_Daily': ''}
                    param = 1
                    dictOne[table] = str(buytime)
                else:
                    # print(datetime.datetime.strptime(str(buytime),'%Y-%m-%d'))
                    # print(datetime.datetime.strptime(z[table],'%Y-%m-%d'))
                    if datetime.datetime.strptime(str(buytime),'%Y-%m-%d') > datetime.datetime.strptime(dictOne[table],'%Y-%m-%d'):    #datetime.datetime.strptime(z[table],'%Y-%m-%d')
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
    return argList


def updateRecords(jsonFile, lastDataJson, lastDataInfo):
    '''
    将最近的数据记录写到lastdata.json
    :param jsonFile: 指的是dbinfo.json路径
    :param lastDataJson: 预定义数据结构
    :param lastDataInfo: 指的是lastdata.json路径
    :return:
    '''
    updateData = lastDataJson
    with open(jsonFile) as jsonFiles:
        data = json.load(jsonFiles)
    # print(data)
    dbList = data['Currency']    #数据库列表

    for tableName in dbList:
        instanceDB = DBlink(tableName)
        results = instanceDB.updateRecord()    #返回对应数据库的所有数据

        if len(results) != 0:
            for i in results:    #遍历每一条数据
                # agent = i['agent']
                # buytime = i['buytime']
                agent = i[1].strip()    #上面的mysql的提取用法，这是postgresql的用法
                buytime = i[0]
                #没有就插入，有就比较后在插入
                updateData = identify(lastDataJson,agent,tableName,buytime)

    # print(updateData)
    try:
        with open(lastDataInfo, 'w') as jsonFiles:
            jsonFiles.write(json.dumps(updateData))
        logging.info('记录最近的数据成功！')
    except:
        logging.warning('无法记录最近的数据！！')



def main():
    '''
    更新数据，更改csv文件后直接运行脚本
    :return:
    '''
    # instance = UpDate('/home/duanyuping/PycharmProjects/finacialdatabase/data/update.csv')
    # instance.UpdateMain()

    agent = 'XM'
    currency = 'EURUSD_Daily'
    date = '2017-02-21'
    jsonURL = '/home/duanyuping/PycharmProjects/finance/data/lastdata.json'
    today = '2017-02-21'
    instance = Identify(agent, currency, date, jsonURL, today)
    identify = instance.identfyFunction()
    print(identify)
    # lastDataJson = {
    #     'FXCM': [{'EURCAD_Daily': '2017-02-28'}, {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''},
    #              {'EURUSD_Daily': ''},
    #              {'GBPUSD_Daily': ''}, {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''}, {'USDCNH_Daily': ''}],
    #     'FOREX': [{'EURCAD_Daily': ''},
    #               {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''},
    #               {'GBPUSD_Daily': ''},
    #               {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''}, {'USDCNH_Daily': ''}],
    #     'XM': [{'EURCAD_Daily': ''}, {'EURCHF_Daily': ''},
    #            {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''}, {'GBPUSD_Daily': ''},
    #            {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''},
    #            {'USDCNH_Daily': ''}]}

    # jsonFile = '/home/duanyuping/PycharmProjects/finance/data/dbinfo.json'
    # updateRecords(jsonFile, lastDataJson, jsonURL)



if __name__ == '__main__':
    main()
