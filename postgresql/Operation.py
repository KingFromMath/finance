# -*- coding: utf-8 -*-
"""
create at:17-3-9 下午8:50
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

import psycopg2
# 数据库连接参数

class Operation(object):
    def __init__(self, tableName):
        self.connection = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")

        self.tableName = tableName

    # def addToCurrencyTrade(self, tradeid, tradedate, currencypair, tradetype, tradeprice, tradevolume, stopprice, profitprice):
    #     '''
    #     往currencytrade数据库中插入数据
    #     :param tradeid:
    #     :param tradedate:
    #     :param currencypair:
    #     :param tradetype:
    #     :param tradeprice:
    #     :param tradevolume:
    #     :param stopprice:
    #     :param profitprice:
    #     :return:
    #     '''
    #     self.cur.execute("INSERT INTO %s (  \
    #                 tradeid, tradedate, currencypair, tradetype, tradeprice, tradevolume, stopprice, profitprice)  \
    #                 VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s)" \
    #                 %(self.tableName, tradeid, tradedate, currencypair, tradetype, tradeprice, tradevolume, stopprice, profitprice ))
    #
    #     self.conn.commit()
    #     self.cur.close()

    # def addToCurrencyTrace(self, tradeid, endprice, endprofit, enddate, highprice, highdate, lowprice, lowdate, agent):
    #     '''
    #     往currencytrace数据库中插入数据
    #     :param tradeid:
    #     :param endprice:
    #     :param endprofit:
    #     :param enddate:
    #     :param highprice:
    #     :param highdate:
    #     :param lowprice:
    #     :param lowdate:
    #     :return:
    #     '''
    #     self.cur.execute("INSERT INTO %s (  \
    #                     tradeid, endprice, endprofit, enddate, highprice, highdate, lowprice, lowdate, agent)  \
    #                     VALUES (%s, %s, %s, '%s', %s, '%s', %s, '%s', '%s')" \
    #                          % (self.tableName, tradeid, endprice, endprofit, enddate, highprice, highdate, lowprice, lowdate, agent))
    #
    #     self.conn.commit()
    #     self.cur.close()


    def addToCurrencyTrades(self,  agent,  ticket , opentime, type , size , item ,  price , sl ,
                            tp ,  closetime ,  closeprice ,  commission ,  taxes ,  swap ,  profit ):

        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO %s (agent,  ticket , opentime, type , size , item ,  price , sl , \
                        tp ,  closetime ,  closeprice ,  commission ,  taxes ,  swap ,  profit)VALUES  \
                      ('%s', '%s', '%s', '%s', %s, '%s', %s, %s, %s, '%s', %s, %s, %s, %s, %s)" \
                      %(self.tableName, agent,  ticket , opentime, type , size , item ,  price , sl , tp ,  \
                        closetime ,  closeprice , commission ,  taxes ,  swap ,  profit)
                cursor.execute(sql)
        finally:
            self.connection.commit()

    def compair(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "select ticket from %s"%(self.tableName)
                cursor.execute(sql)
                results = cursor.fetchall()
        finally:
            self.connection.commit()

        return results





def main():
    agent = 'xm'
    ticket = '12345'
    opentime = '2017-02-12 12:00:00'
    type = 'buy'
    size = 1.0
    item = 'usreur'
    price = 2.534
    sl = 8.353
    tp = 3.45
    closetime = '2017-02-12 12:00:00'
    closeprice = 4.3435
    commission = 2.434
    taxes = 4.2342
    swap = 3.343
    profit = 3.345

    instance = Operation('currencytrades')
    # instance.addToCurrencyTrades(agent,  ticket , opentime, type , size , item ,  price , sl ,
    #                         tp ,  closetime ,  closeprice ,  commission ,  taxes ,  swap ,  profit)
    # print(instance.compair())

if __name__ == '__main__':
    main()
