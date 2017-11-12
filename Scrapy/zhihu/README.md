# 这个是爬知乎的代码
* 入口为 ./begin.py ，意为执行 zhihu 这个爬虫:
```
# -*- coding: utf-8 -*-
from scrapy import cmdline
cmdline.execute("scrapy crawl zhihu".split())
```
* 爬虫入口 ./zhihu/spiders/spider.py :
执行爬虫。输入关键词，检索对应的话题:
```
def start_requests(self):
    key_word = "XXX"
    trans_word = urllib.quote(key_word)
    topic_url = "马赛克" + trans_word + "马赛克"
    ...
    request = Request(topic_url, callback=self.get_topic, headers=header, dont_filter=True)
    yield request
```
得到关键字下的所有话题，检索对应的问题：
```
def get_topic(self, response):
    ...
    content = json.loads(response.body)
    for num_htmls in range(len(content.get("htmls"))):
        # 采用正则表达式获得 话题id号、话题名称：
        line = content.get("htmls")[num_htmls]
        pattern = re.compile(r'(\d+)')
        topic_id = re.search(pattern,line).group(0)
        pattern = re.compile(r'alt="([^"]+)"')
        Topic_name = re.findall(pattern, line)[0].encode('utf-8')
        question_url = "马赛克" + topic_id + "马赛克"
        request = Request(question_url, callback=self.get_question, headers=header, dont_filter=True)
        yield request
    # 若没有结束，继续调用该函数
```
得到某话题下的精华问题，检索回答：
```
def get_question(self, response):
    # 得到问题id：
    line = response.body
    pattern = re.compile(r'<a class="question_link" href="/question/(\d+)"')
    list_id1 = re.findall(pattern,line)
    list_id2 = list(set(list_id1)) #将list_id1去重
    for num_question in range(len(list_id2)):
        answer_url = "https://www.zhihu.com/api/v4/questions/" + list_id2[num_question] + "/answers?limit=10&offset=0"
        request = Request(answer_url, callback=self.get_answer, meta=data, headers=header, dont_filter=True)
        yield request
    # 若没有结束，继续调用该函数
```
得到某问题下的回答，检索问题名称：
```
def get_answer(self, response):
    content = response.body
    question_title_url = "马赛克" + Question_id
    request = Request(question_title_url, callback=self.get_question_title, headers=header, dont_filter=True)
    yield request
    # 若没有结束，继续调用该函数
```
得到问题名称，将所有信息存储到items中：
```
def get_question_title(self,response):
    # 将内容中的 \" 变为 \\\"
    line = response.body.replace("\\\"","\\\\\\\"")
    title = json.loads(line).get('title')
    zhihuItem = ZhihuItem()
    zhihuItem['KeyWord'] = response.meta['key_word']
    zhihuItem['Topic_name'] = response.meta['Topic_name']
    zhihuItem['Topic_id'] = response.meta['topic_id']
    zhihuItem['Question_id'] = response.meta['Question_id']
    zhihuItem['Question_content'] = title
    zhihuItem['Content'] = response.meta['content']
    yield zhihuItem
```
* 爬虫出口：./zhihu/pipelines.py:
```
# 处理中文编码的问题：
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ZhihuPipeline(object):
    def process_item(self, item, spider):
        ...
        Content = item.get("Content").replace("\\\"", "\\\\\\\"").replace("\\\\","\\").decode("unicode_escape")
        # 执行写文件操作
        return item
```
