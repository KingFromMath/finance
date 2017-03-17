# -*- coding: utf-8 -*-
"""
create at:17-3-2 下午9:49
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
import os
import os.path
from readcsvtodb.ReadCSVToDB import ReadCSVToDB
from readcsvtodb.UpData import updateRecords

class FileOperation(object):
    '''
    扫描指定文件夹中的csv文件，往数据库中插入不存在的数据，并记录最新的记录
    '''
    def __init__(self, dir, jsonURL, today):
        '''

        :param dir: csv文件路径
        :param jsonURL: 记录最近数据的json文件路径
        :param today: 下载csv文件的日期，用来避免交易记录不完整
        '''
        self.dir = dir
        self.jsonURL = jsonURL
        self.today = today
        self.lastDataJson = {
            'FXCM': [{'EURCAD_Daily': ''}, {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''},
                     {'EURUSD_Daily': ''},
                     {'GBPUSD_Daily': ''}, {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''}, {'USDCNH_Daily': ''}],
            'FOREX': [{'EURCAD_Daily': ''},
                      {'EURCHF_Daily': ''}, {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''},
                      {'GBPUSD_Daily': ''},
                      {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''}, {'USDCNH_Daily': ''}],
            'XM': [{'EURCAD_Daily': ''}, {'EURCHF_Daily': ''},
                   {'EURGBP_Daily': ''}, {'EURJPY_Daily': ''}, {'EURUSD_Daily': ''}, {'GBPUSD_Daily': ''},
                   {'USDCHF_Daily': ''}, {'USDJPY_Daily': ''},
                   {'USDCNH_Daily': ''}]}
        self.jsonFile = '/home/duanyuping/PycharmProjects/finance/data/dbinfo.json'

    def csvURL(self, dir):
        '''
        获取csv文件路径
        :param dir: /home/duanyuping/Files/input/currency/fxcm
        :return:/home/duanyuping/Files/input/currency/fxcm/xxx.csv
        '''
        csvURL = []
        for parent,dirNames,fileNames in os.walk(dir):    #parent,dirNames,fileNames 顺序还不能乱，也不能少dirNames，尽管没有用到他
            for fileName in fileNames:
                # csv = os.path.join(parent, fileName)
                csvURL.append(os.path.join(parent, fileName))
        return list(set(csvURL))

    def secondFile(self):
        '''
        获取代理商文件路径
        :return: /home/duanyuping/Files/input/currency/fxcm
        '''
        secondURL = []
        for parent,dirNames,fileNames in os.walk(self.dir):    #parent,dirNames,fileNames 顺序还不能乱，也不能少dirNames，尽管没有用到他
            for fileName in fileNames:
                # print("parent is: " + parent)
                # parentFile = parent
                secondURL.append(parent)
        return list(set(secondURL))

    def agentName(self):
        '''
        获取代理商名
        :return: 代理商文件夹名，对应lastdata的最外层key
        '''
        agent = []
        for parent,dirNames,fileNames in os.walk(self.dir):
            for dirName in dirNames:
                # agent = dirName
                agent.append(dirName)
        return agent


    def csvOperation(self):
        '''
        更新外汇数据的入口函数
        :return:
        '''
        for agent in self.agentName():
            for second in self.secondFile():
                if agent == second.split('/')[-1]:
                    for csvURL in self.csvURL(second):
                        # print(agent)
                        # print(csvURL)
                        instance = ReadCSVToDB(csvURL)    #调用插入模块
                        instance.readCSVFile(agent, self.jsonURL, self.today)
        print('正在记录最新数据......')
        updateRecords(self.jsonFile, self.lastDataJson, self.jsonURL)    #记录最新的数据

def main():
    '''
    扫描指定文件夹中的csv文件，往数据库中插入不存在的数据，并记录最新的记录
    :return:
    '''
    dir = '/home/duanyuping/Files/input/currency'
    jsonURL = '/home/duanyuping/PycharmProjects/finance/data/lastdata.json'
    today = '2017-03-11'

    instance = FileOperation(dir,jsonURL,today)
    instance.csvOperation()    #插入数据主入口
    # instance.secondFile()

if __name__ == '__main__':
    main()



