# 这个是爬知乎的代码
* 入口为 begin.py ，意为执行 zhihu 这个爬虫:
```
# -*- coding: utf-8 -*-
from scrapy import cmdline
cmdline.execute("scrapy crawl zhihu".split())
```
