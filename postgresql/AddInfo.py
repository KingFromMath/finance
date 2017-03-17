# -*- coding: utf-8 -*-
"""
create at:17-3-9 下午9:20
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
import configparser
from postgresql.Operation import Operation

cf = configparser.ConfigParser()
cf.read("/home/duanyuping/PycharmProjects/finance/confandlog/currency.conf")

def currencytrade(tableName):
    '''
    读取conf文件信息，新增交易信息
    :param tableName: currencytrade
    :return:
    '''
    tradeid = cf.get("currencytrade", "tradeid")    #tradeid的构成规则：年月日+交易编号， eg：2017031101
    tradedate = cf.get("currencytrade", "tradedate")
    currencypair = cf.get("currencytrade", "currencypair")
    tradetype = cf.get("currencytrade", "tradetype")    #0:sell, 1:buy
    tradeprice = cf.get("currencytrade", "tradeprice")
    tradevolume = cf.get("currencytrade", "tradevolume")
    stopprice = cf.get("currencytrade", "stopprice")
    profitprice = cf.get("currencytrade", "profitprice")

    instance = Operation(tableName)
    instance.addToCurrencyTrade(tradeid, tradedate, currencypair, tradetype, tradeprice, tradevolume, stopprice,
                                profitprice)
    print('add info successful!')


def currencytrace(tableName):
    '''
    读取conf文件信息，新增交易信息
    :param tableName: currencytrace
    :return:
    '''
    tradeid = cf.get("currencytrace", "tradeid")    #tradeid的构成规则：年月日+交易编号， eg：2017031101
    endprice = cf.get("currencytrace", "endprice")
    endprofit = cf.get("currencytrace", "endprofit")
    enddate = cf.get("currencytrace", "enddate")
    highprice = cf.get("currencytrace", "highprice")
    highdate = cf.get("currencytrace", "highdate")
    lowprice = cf.get("currencytrace", "lowprice")
    lowdate = cf.get("currencytrace", "lowdate")
    agent = cf.get("currencytrace", "agent")

    instance = Operation(tableName)
    instance.addToCurrencyTrace(tradeid, endprice, endprofit, enddate, highprice, highdate, lowprice, lowdate, agent)
    print('add info successful!')

def main():
    # currencytrade('currencytrade')
    currencytrace('currencytrace')


if __name__ == '__main__':
    main()