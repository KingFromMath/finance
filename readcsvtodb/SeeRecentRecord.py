# -*- coding: utf-8 -*-
"""
create at:17-2-21 下午8:47
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
from readcsvtodb.DBLink import DBlink

class SeeRecentRecord(object):
    '''
    查询某个日期的外汇数据
    '''
    def __init__(self, tableList, date):
        '''

        :param tableList: 需要添加数据的数据表名
        :param date: 查询日期
        '''
        self.tableList = tableList
        self.date = date

    def recentRocord(self):
        '''

        :return:
        '''
        for tableName in self.tableList:
            instance = DBlink(tableName)
            try:
                result = instance.selectRecentData(self.date)
                print('正在打印'+tableName+'的数据： '+str(result))
            except:
                print(tableName + ' oh,程序运行出错！')


def main():
    tableList = ['EURCAD_Daily', 'EURCHF_Daily', 'EURGBP_Daily', 'EURJPY_Daily', 'EURUSD_Daily', 'GBPUSD_Daily', 'USDCHF_Daily', 'USDJPY_Daily', 'USDCNH_Daily']
    date = '2017-01-22'
    instance = SeeRecentRecord(tableList, date)
    instance.recentRocord()

if __name__ == '__main__':
    main()

