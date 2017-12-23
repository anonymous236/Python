Python访问数据库(MySQL)
========
* python 连接 数据库:Python DB API<br>
* Python DB QPI访问数据库的流程:
```
开始 --> 创建connection --> 获取cursor --> 执行命令、获取数据、处理数据 --> 关闭cursor --> 关闭connection
```
* DB API-数据库连接对象connection:
 * 连接对象:建立Python客户端与数据库的网络连接
 * 创建方法:MySQLdb.Connect参数
 参数名|类型|说明
 -----|----|----
 host|字符串|MySQL服务器地址
