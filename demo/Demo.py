# -*- coding: utf-8 -*-
"""
create at:17-3-1 下午9:13
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
import json
import datetime
# with open('/home/duanyuping/PycharmProjects/finance/data/lastdata.json') as json_file:
#     data = json.load(json_file)
    # json_file.write(json.dumps(data))
# print(data)


# if datetime.datetime.strptime('2017-02-21','%Y-%m-%d') == datetime.datetime.strptime('2017.02.21','%Y.%m.%d'):
#     print("098")

import psycopg2
# 数据库连接参数
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute("select * from testDB")
rows = cur.fetchall()
print(rows)
for i in rows:
    print(i)
conn.commit()
cur.close()