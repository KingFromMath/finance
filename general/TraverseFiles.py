# -*- coding: utf-8 -*-
"""
create at:17-3-6 下午9:47
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

class TraverseFiles(object):
    '''
    遍历文件库
    基本模型：
    -----path
    --------secondfiles
    -------------------thirdfiles
    提供的API：secondfilesName，secondfilsPath，thirdfilesPath
    '''
    def __init__(self, path):
        '''

        :param path: /home/duanyuping/Files/currency
        '''
        self.path = path

    def secondFilesName(self):
        for parent, dirNames, fileNames in os.walk(self.path):
            for dirName in dirNames:
                yield dirName    #没有成功


def main():
    path = '/home/duanyuping/Files/output'
    instance = TraverseFiles(path)
    results = instance.secondFilesName()
    for i in results:
        print(i)


if __name__ == '__main__':
    main()