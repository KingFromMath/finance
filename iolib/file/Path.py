# -*- coding: utf-8 -*-
"""
create at:17-3-22 上午11:29
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

class Path(object):
    def __init__(self, dir):
        self.dir = dir

    def csvURL(self, param):
        '''
        获取csv文件路径
        :param param: /home/duanyuping/Files/input/currency/fxcm
        :return:/home/duanyuping/Files/input/currency/fxcm/xxx.csv
        '''
        csvURL = []
        for parent,dirNames,fileNames in os.walk(param):    #parent,dirNames,fileNames 顺序还不能乱，也不能少dirNames，尽管没有用到他
            for fileName in fileNames:
                # csv = os.path.join(parent, fileName)
                csvURL.append(os.path.join(parent, fileName))
        return list(set(csvURL))

    def secondFile(self):
        '''
        获取dir的子文件夹路径
        :return: ['/home/hadoop/Files/Data/test/data1/xm', '/home/hadoop/Files/Data/test/data1/forex', '/home/hadoop/Files/Data/test/data1/fxcm']
        '''
        secondURL = []
        for parent,dirNames,fileNames in os.walk(self.dir):
            for fileName in fileNames:
                # print("parent is: " + parent)
                # parentFile = parent
                secondURL.append(parent)
        return list(set(secondURL))

    def agentName(self):
        '''
        获取dir的子文件夹名
        :return: ['fxcm', 'forex', 'xm']
        '''
        agent = []
        for parent,dirNames,fileNames in os.walk(self.dir):
            for dirName in dirNames:
                # agent = dirName
                agent.append(dirName)
        return agent

def main():
    'secondFile()'
    instance = Path('/home/hadoop/Files/Data/test/data1')
    result = instance.secondFile()
    # print(result)
    'csvURL()'
    # for i in result:
    #     result0 = instance.csvURL(i)
    #     print(result0)
    ''
    result1 = instance.agentName()
    print(result1)


if __name__ == '__main__':
    main()

'''
API:

'''