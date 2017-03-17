# -*- coding: utf-8 -*-
"""
create at:17-2-17 上午6:21
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

import pymysql
import psycopg2

class DBlink(object):
    def __init__(self, table_name):
        # self.connection = pymysql.connect(host='localhost',
        #                                   user='root',
        #                                   password='duanyuping',
        #                                   db='Finance',
        #                                   charset='utf8',
        #                                   cursorclass=pymysql.cursors.DictCursor)
        self.connection = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1",
                                     port="5432")

        self.table_name = table_name

    def addRataData(self,buytime, startprice, highest, lowest, endprice, volume, agent):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO %s (buytime, startprice, highest, lowest, endprice, volume, agent) " \
                      "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
                      % (self.table_name, buytime, startprice, highest, lowest, endprice, volume, agent)
                cursor.execute(sql)
        finally:
            self.connection.commit()
            # self.connection.cursor().close()

    def selectData(self,id):
        try:
            with self.connection.cursor() as cursor:
                sql = "select * from %s where id=%d" %(self.table_name, id)
                cursor.execute(sql)
                results = cursor.fetchall()
        finally:
            self.connection.commit()
            # self.connection.cursor().close()

        return results

    def selectRecentData(self, date):
        '''
        设计用来查询最近添加的记录，也就是验证新记录是否插入成功
        :param date: 对应外汇数据中的buytime
        :return: 查询结果
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "select * from %s where buytime='%s' "%(self.table_name, date)
                cursor.execute(sql)
                results = cursor.fetchall()
        finally:
            self.connection.commit()
            # self.connection.cursor().close()

        return results

    def updateRecord(self):
        '''
        获取数据库所有记录，然后通过程序找到最近的记录
        :return:
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "select buytime, agent from %s "%(self.table_name)
                cursor.execute(sql)
                results = cursor.fetchall()
                # print(results)
        finally:
            self.connection.commit()
            # self.connection.cursor().close()

        return results


def main():
    instance = DBlink('EURCAD_Daily')
    # instance.addRataData('2017-02-01', 1.07964, 1.08065, 1.07290, 1.07674, 84487, 'XM')
    # print(instance.selectData(1))
    # instance.updateRecord()

if __name__ == '__main__':
    main()