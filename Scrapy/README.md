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
