Python访问数据库(MySQL)
========
* python 连接 数据库：Python DB API<br>
* Python DB QPI访问数据库的流程：
```
开始 --> 创建connection --> 获取cursor --> 执行命令、获取数据、处理数据 --> 关闭cursor --> 关闭connection
```
## DB API-数据库连接对象connection：
* 连接对象：建立Python客户端与数据库的网络连接
* 创建方法：MySQLdb.Connect参数

参数名|类型|说明
-----|----|----
host|字符串|MySQL服务器地址
port|数字|MySQL服务器端口号
user|字符串|用户名
passwd|字符串|密码
db|字符串|数据库名称
charset|字符串|连接编码

* connection对象支持的方法：

方法名|说明
-----|----
cursor()|使用该连接创建并返回游标
commit()|提交当前事务
rollback()|回滚当前事务
close()|关闭连接

## DB API-数据库游标对象cursor：
* 游标对象：用于执行查询和获取结果
* cursor对象支持的方法：

参数名|说明
-----|----
execute(op[,args])|执行一个数据库查询和命令
fetchone()|获取结果集的下一行
fetchmany(size)|获取结果集的下size行
fetchall()|获取结果集中**剩下的**所有行
rowcount|最近一次execute返回数据的行数或影响行数
close()|关闭游标对象

```
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
for row in r: # 元组的形式
    print row[2]
    print row
print cursor.rowcount
cursor.close()
conn.close()
```
## insert/updata/delete操作
* 事务：访问和更新数据库的一个程序执行单元（操作的集合）
    * 原子性：事务中包括的操作要么都做，要么都不做
    * 一致性：事务必须使数据库从一致性状态变道另一个一致性状态
    * 隔离性：一个事务的执行不能被其他事务干扰
    * 持久性：事务一旦提交，它对数据库的改变就是永久性的

```
使用cursor.execute()执行语句
    --> 出现异常，使用conn.rollback()回滚事务
    --> 没有异常，使用conn.commit()提交事务
```

