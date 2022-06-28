# encoding = UTF-8


import pymysql

db = pymysql.connect(host='192.168.65.137', port=3306, user='root', password='123456', database="jiuyi")
db.autocommit(True)
cors = db.cursor()
sql_str = "select * from uc_members"
cors.execute(sql_str)
ret = cors.fetchall()
print(ret)
cors.close()
db.close()
