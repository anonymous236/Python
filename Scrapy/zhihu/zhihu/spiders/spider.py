# -*- coding: utf-8 -*-
from scrapy.http import Request
from scrapy import Spider
from zhihu.items import ZhihuItem
import urllib
import json
import re

class SpiderSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']

    def start_requests(self):
        key_word = "XXX"
        trans_word = urllib.quote(key_word)
        topic_url = "马赛克" + trans_word + "马赛克"

        header = {}
        header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        header['...'] = '...'
        header['User-Agent'] = 'Mozilla/5.0'
        request = Request(topic_url, callback=self.get_topic, headers=header, dont_filter=True)
        request.meta['key_word'] = key_word
        request.meta["header"] = header
        yield request

    def get_topic(self, response):
        key_word = response.meta['key_word']
        header = response.meta["header"]
        content = json.loads(response.body)
        for num_htmls in range(len(content.get("htmls"))):
            line = content.get("htmls")[num_htmls]
            pattern = re.compile(r'(\d+)')
            topic_id = re.search(pattern,line).group(0)
            pattern = re.compile(r'alt="([^"]+)"')
            Topic_name = re.findall(pattern, line)[0].encode('utf-8')
            question_url = "马赛克" + topic_id + "马赛克"
            request = Request(question_url, callback=self.get_question, headers=header, dont_filter=True)
            request.meta['topic_id'] = topic_id
            request.meta['key_word'] = key_word
            request.meta['Topic_name'] = Topic_name
            yield request
        if content.get("paging").get("next") != '':
            topic_url = "马赛克" + content.get("paging").get("next")
            request = Request(topic_url, callback=self.get_topic, headers=header, dont_filter=True)
            request.meta['key_word'] = key_word
            request.meta["header"] = header
            yield request

    def get_question(self, response):
        topic_id = response.meta['topic_id']
        key_word = response.meta['key_word']
        Topic_name = response.meta['Topic_name']
        line = response.body
        questionid_list = []
        pattern = re.compile(r'<a class="question_link" href="/question/(\d+)"')
        list_id1 = re.findall(pattern,line)
        list_id2 = list(set(list_id1)) #将list_id1去重
        header = {}
        header['Accept'] = 'application/json, text/plain, */*'
        header['...'] = '...'
        header['authorization'] = '重要字段'

        # POST方法
        data = {}
        data['...'] = '...'

        for num_question in range(len(list_id2)):
            # id 存在则不访问
            exist = 0
            file = open("文件.txt", "r")
            for line in file.readlines():
                if line.replace("\n","") == list_id2[num_question]:
                    exist = 1
                    break
            file.close()
            if exist == 0:
                file = open("文件.txt", "a")
                file.write(list_id2[num_question] + "\n")
                file.close()
                answer_url = "马赛克" + list_id2[num_question] + "马赛克"
                header['Referer'] = '马赛克' + list_id2[num_question]
                request = Request(answer_url, callback=self.get_answer, meta=data, headers=header, dont_filter=True)
                request.meta['topic_id'] = topic_id
                request.meta['key_word'] = key_word
                request.meta['Topic_name'] = Topic_name
                request.meta['Question_id'] = list_id2[num_question]
                request.meta["header"] = header
                request.meta["data"] = data
                yield request

        str1 = response.url.split("?page=")
        page_now = int(str1[1])
        try:
            page_next = page_now + 1
            question_url = str1[0] + "?page=" + str(page_next)
            request = Request(question_url, callback=self.get_question, headers=header, dont_filter=True)
            request.meta['topic_id'] = topic_id
            request.meta['key_word'] = key_word
            request.meta['Topic_name'] = Topic_name
            yield request
        except:
            pass

    def get_answer(self, response):
        topic_id = response.meta['topic_id']
        key_word = response.meta['key_word']
        Topic_name = response.meta['Topic_name']
        Question_id = response.meta['Question_id']
        header1 = response.meta["header"]
        data1 = response.meta["data"]
        content = response.body

        question_title_url = "马赛克" + Question_id
        header = {}
        header['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
        header['...'] = '...'
        header['authorization'] = '重要字段'

        request = Request(question_title_url, callback=self.get_question_title, headers=header, dont_filter=True)
        request.meta['topic_id'] = topic_id
        request.meta['key_word'] = key_word
        request.meta['Topic_name'] = Topic_name
        request.meta['Question_id'] = Question_id
        request.meta['content'] = content
        yield request

        line = json.loads(content)
        is_end = str(line.get("paging").get("is_end"))
        if is_end == "False":
            str1 = response.url.split("&offset=")
            page_now = int(str1[1])
            page_next = page_now + 10
            answer_url = str1[0] + "&offset=" + str(page_next)
            request = Request(answer_url, callback=self.get_answer, meta=data1, headers=header1, dont_filter=True)
            request.meta['topic_id'] = topic_id
            request.meta['key_word'] = key_word
            request.meta['Topic_name'] = Topic_name
            request.meta['Question_id'] = Question_id
            request.meta["header"] = header1
            request.meta["data"] = data1
            yield request

    def get_question_title(self,response):
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
