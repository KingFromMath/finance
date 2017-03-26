# -*- coding: utf-8 -*-
"""
create at:17-3-17 下午9:32
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
from bs4 import BeautifulSoup
import copy

from postgresql.Operation import Operation;


def webTitle_tp(param):
    '''
    解析："td", title="[tp]"
    :param param:
    :return:
    '''
    content = param.find_all("td", title="[tp]")
    return content


def webTitle_sl(param):
    '''
    解析："td", title="[sl]"
    :param param:
    :return:
    '''
    content = param.find_all("td", title="[sl]")
    return content


def siblings(param):
    '''
    获取兄弟节点
    :param param:
    :return:
    '''
    cube = []
    for i in param:
        cube.append(i.text)
        for k in i.find_next_siblings():
            cube.append(k.text)

    return cube


def splitList(param):
    '''
    把文本信息转换为二维数组
    :param param:
    :return:
    '''
    cube = []
    cube1 = []
    for i in range(0, int(len(param) / 14)):
        cube.extend(param[i * 2 * 7:i * 2 * 7 + 14])
        cube1.append(copy.deepcopy(cube))
        cube.clear()

    return cube1

def findAgent(path):
    '''
    从路径中获取agent
    :param path:
    :return:
    '''
    agent = (path.split('/')[-1]).split('.')[0]
    return agent

def compair(param1):
    '''
    生成用于判别数据是否有重复的列表
    :param param1: table name
    :return: list
    '''
    cube = []
    instance = Operation(param1)
    result = instance.compair()    #[('136603800 ',), ('136603960 ',), ('136278140 ',), ('136603775 ',)]
    for i in result:
        cube.append(i[0].strip())    # .strip() 移除首尾的空格

    return cube

def addToDB(tableName, info, agent):
    '''
    向数据库中插入数据
    :param tableName:
    :param info:
    :param agent:
    :return:
    '''
    # agent = 'xm'
    # ticket = '12345'
    # opentime = '2017-02-12 12:00:00'
    # type = 'buy'
    # size = 1.0
    # item = 'usreur'
    # price = 2.534
    # sl = 8.353
    # tp = 3.45
    # closetime = '2017-02-12 12:00:00'
    # closeprice = 4.3435
    # commission = 2.434
    # taxes = 4.2342
    # swap = 3.343
    # profit = 3.345
    compairList = compair(tableName)
    try:
        if(info[0].strip() not in compairList):
            instance = Operation(tableName)
            instance.addToCurrencyTrades(agent,info[0],info[1],info[2],float(info[3]),info[4],
                                     float(info[5]),float(info[6]),float(info[7]),info[8],
                                     float(info[9]),float(info[10]),float(info[11]),float(info[12]),float(info[13]))
            print('add info to db:' + info[0])
        else:
            print('重复数据： '+info[0])

    except:
        print('error: '+agent+info[0]+info[2])

'''主函数'''
def webContent(param, tableName):
    with open(param, 'r')as file:
        soup = BeautifulSoup(file, "lxml")
        table = soup.find_all("table")
        for th in table:  # only one object

            record = siblings(webTitle_tp(th))    #解析结果1
            # print(record)
            for i in splitList(record):
                # print(i)
                addToDB(tableName,i,findAgent(param))
            # print('+++++++++++++++++++++++++++++++++++++++')
            record1 = siblings(webTitle_sl(th))    #解析结果2
            for k in splitList(record1):
                # print(k)
                addToDB(tableName,k,findAgent(param))


'''调用函数新增数据'''
# webContent("/home/duanyuping/Files/input/finance/forex.html", 'currencytrades')
