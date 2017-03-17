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
        self.conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
        self.cur = self.conn.cursor()

        self.tableName = tableName

    def addToCurrencyTrade(self, tradeid, tradedate, currencypair, tradetype, tradeprice, tradevolume, stopprice, profitprice):
        '''
        往currencytrade数据库中插入数据
        :param tradeid:
        :param tradedate:
        :param currencypair:
        :param tradetype:
        :param tradeprice:
        :param tradevolume:
        :param stopprice:
        :param profitprice:
        :return:
        '''
        self.cur.execute("INSERT INTO %s (  \
                    tradeid, tradedate, currencypair, tradetype, tradeprice, tradevolume, stopprice, profitprice)  \
                    VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s)" \
                    %(self.tableName, tradeid, tradedate, currencypair, tradetype, tradeprice, tradevolume, stopprice, profitprice ))

        self.conn.commit()
        self.cur.close()

    def addToCurrencyTrace(self, tradeid, endprice, endprofit, enddate, highprice, highdate, lowprice, lowdate, agent):
        '''
        往currencytrace数据库中插入数据
        :param tradeid:
        :param endprice:
        :param endprofit:
        :param enddate:
        :param highprice:
        :param highdate:
        :param lowprice:
        :param lowdate:
        :return:
        '''
        self.cur.execute("INSERT INTO %s (  \
                        tradeid, endprice, endprofit, enddate, highprice, highdate, lowprice, lowdate, agent)  \
                        VALUES (%s, %s, %s, '%s', %s, '%s', %s, '%s', '%s')" \
                             % (self.tableName, tradeid, endprice, endprofit, enddate, highprice, highdate, lowprice, lowdate, agent))

        self.conn.commit()
        self.cur.close()




def main():

    tradeid = '1703092103'
    tradedate = '2017-02-03'
    currencypair = 'ERUGBP'
    tradetype = 0
    tradeprice = 1.7434
    tradevolume = 0.5
    stopprice = 1.8343
    profitprice = 1.86544

    # instance = Operation('currencytrade')
    # instance.addToCurrencyTrade(tradeid, tradedate, currencypair, tradetype, tradeprice, tradevolume, stopprice, profitprice)


if __name__ == '__main__':
    main()
