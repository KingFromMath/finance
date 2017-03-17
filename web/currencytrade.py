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

with open("/home/hadoop/PycharmProjects/finance/data/fxcm.html","r") as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, "lxml")
    table = soup.find_all("table")
    print(table)