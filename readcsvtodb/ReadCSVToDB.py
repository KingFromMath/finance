# -*- coding: utf-8 -*-
"""
create at:17-2-13 上午6:58
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
import re

from readcsvtodb.DBLink import DBlink
from readcsvtodb.UpData import Identify
from confandlog.log import *

class ReadCSVToDB(object):
    '''
    读取外汇csv文件，向数据库插入数据
    '''
    def __init__(self, csvfile):
        '''
        :param csvfile: '/home/duanyuping/Files/input/EURUSD1440.csv'
        '''
        self.csvfile = csvfile

    def DBName(self):
        '''
        从输入的csv路径中获取数据表名
        eg:  '/home/duanyuping/Files/input/finance/USDJPY1440.csv'--------->USDJPY_Daily
        :return:
        '''
        target = re.match('[A-Z]+', (self.csvfile.split('/')[-1]).split('.')[0])    #  eg:USDJPY
        DBname = target.group() + '_Daily'

        return DBname

    def readCSVFile(self, agent, jsonURL, today):
        '''

        :param agent: 代理商
        :return:
        '''
        instanceDB = DBlink(self.DBName())    #直接通过DBName函数获取数据表名

        with open(self.csvfile, newline='') as csvline:
            spamreader = csv.reader(csvline)
            count = 1
            newRecord = 1
            for row in spamreader:
                # print(jsonURL)
                try:
                    instanceIdentify = Identify(agent, self.DBName(), row[0], jsonURL, today)    #判断是否需要插入数据
                    identifyValue = instanceIdentify.identfyFunction()

                    # print(identifyValue)
                    if identifyValue == 1:
                        # print(row[0],row[2])
                        instanceDB.addRataData(datetime.datetime.strptime(row[0],'%Y.%m.%d'),float(row[2]),float(row[3]),float(row[4]),float(row[5]),int(row[6]),agent)
                        print(self.csvfile+' 正在插入数据： ' + str(count))
                        newRecord += 1
                    else:
                        # logging.warning('无法往数据库插入数据，identifyValue等于： ' + str(identifyValue))
                        # print("0921")
                        pass
                except:
                    logging.warning('插入数据出错: '+str(self.csvfile)+' 数据判断模块出现Error')
                    # print('插入数据出错:  '+str(row))
                count += 1
        logging.info(self.csvfile+'文件共有'+str(count-1)+'条数据，'+'其中插入新数据'+str(newRecord-1)+'条。')
                # exit()

    #with: 只能一边读一边写，不能采取返回一个迭代对象在遍历写入数据库的设计方式，会发生IO错误

def main():
    '''
    目前是手动输入数据表名和源文件名
    :return:
    '''
    jsonURL = '/home/duanyuping/PycharmProjects/finance/data/lastdata.json'
    today = '2017-02-27'

    instance = ReadCSVToDB('/home/duanyuping/Files/input/currency/FXCM/EURCAD60.csv')
    instance.readCSVFile('FXCM', jsonURL, today)



if __name__ == '__main__':
    main()