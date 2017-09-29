# Scrapy框架
## Scrapy框架介绍
* Scrapy框架采用"5+2"结构:
	* 5个模块：`spiders`、`pipelines`、`engine`、`scheduler`、`downloader`;
	* 2个中间件：`Downloader Middleware`、`Spider Middleware`。
* 各个模块介绍:
	* `入口spiders`：解析response,产生爬取项。即:用来向整个框架提供要访问的URL链接,同时解析从网络上获取的页面内容。
	* `出口item pipelines`：负责对提供的信息进行后处理。
	* `engine`：控制所有模块的数据流,根据条件触发事件。
	* `scheduler`：对所有的爬取请求进行调度处理。
	* `downloader`:根据请求下载网页。
	* `downloader middleware`：实施engine、scheduler、downloader三者之间用户可配置的控制。
	* `spider middleware`：对请求和爬取项的再处理。
## Scrapy运行环境
```
python --version
```
个人的python版本为 Python 2.7.13 （统一使用32位）<br>
其他配置请猛戳>>>[python+scrapy安装教程](http://jingyan.baidu.com/article/14bd256e748346bb6d2612be.html)
<br>或者可以在控制台直接输入：
```
pip install scrapy
```
安装完成后测试：
```
scrapy -h
```
## Scrapy爬虫框架的使用
* 新建Scrapy爬虫工程
	```
	scrapy startproject 工程名
	example : D:\pycodes>scrapy startproject python123demo
	```
* 在工程中产生一个Scrapy爬虫
	```
	scrapy genspider 爬虫名 域
	example : D:\pycodes\python123demo>scrapy genspider demo python123.io
	```
* 运行爬虫，爬取网页
	```
	scrapy crawl 爬虫名
	example : D:\pycodes\python123demo>scrapy crawl demo
	```
