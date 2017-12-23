# -*- coding: UTF-8 -*-
import MySQLdb

conn = MySQLdb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'admin',
    passwd = 'admin',
    db = 'weibo',
    charset = 'utf8',
)
cursor = conn.cursor()
sql = "select * from information"
cursor.execute(sql)
r = cursor.fetchall()
for row in r:
    print row[2]
    print row
print cursor.rowcount

try:
    sql_insert = "insert into information(id,weibo_id,created_time) values('10086','10001','2018-1-1')"
    sql_update = "update information set weibo_id = '369' where id = '123'"
    sql_delete = "delete from information where id = '456'"
    cursor.execute(sql_insert)
    cursor.execute(sql_update)
    cursor.execute(sql_delete)

    conn.commit() # 将事务生效
except Exception as e:
    print e
    conn.rollback()
cursor.close()
conn.close()
