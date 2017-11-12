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
        key_word = "萨德"
        trans_word = urllib.quote(key_word)
        #url = "https://www.zhihu.com/search?type=topic&q=" + trans_word
        topic_url = "https://www.zhihu.com/r/search?q=" + trans_word + "&amp;correction=1&amp;type=topic&amp;offset=0"

        header = {}
        header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        header['Accept-Encoding'] = 'gzip, deflate, br'
        header['Accept-Language'] = 'zh-CN,zh;q=0.9'
        header['Cache-Control'] = 'max-age=0'
        header['Connection'] = 'keep-alive'
        header['Host'] = 'www.zhihu.com'
        header['Upgrade-Insecure-Requests'] = '1'
        header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
        kv = {'User-Agent''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
        request = Request(topic_url, callback=self.get_topic, headers=header, dont_filter=True)
        request.meta['key_word'] = key_word
        request.meta["header"] = header
        yield request

    def get_topic(self, response):
        key_word = response.meta['key_word']
        header = response.meta["header"]
        content = json.loads(response.body)
        for num_htmls in range(len(content.get("htmls"))):
            #print (content.get("htmls")[num_htmls])
            line = content.get("htmls")[num_htmls]
            pattern = re.compile(r'(\d+)')
            topic_id = re.search(pattern,line).group(0)
            pattern = re.compile(r'alt="([^"]+)"')
            Topic_name = re.findall(pattern, line)[0].encode('utf-8')
            kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0'}
            question_url = "https://www.zhihu.com/topic/" + topic_id + "/top-answers?page=1"
            request = Request(question_url, callback=self.get_question, headers=header, dont_filter=True)
            request.meta['topic_id'] = topic_id
            request.meta['key_word'] = key_word
            request.meta['Topic_name'] = Topic_name
            yield request
        if content.get("paging").get("next") != '':
            topic_url = "https://www.zhihu.com" + content.get("paging").get("next")
            request = Request(topic_url, callback=self.get_topic, headers=header, dont_filter=True)
            request.meta['key_word'] = key_word
            request.meta["header"] = header
            yield request

    def get_question(self, response):
        topic_id = response.meta['topic_id']
        key_word = response.meta['key_word']
        Topic_name = response.meta['Topic_name']
        #question_url = response.url
        #header1 = response.meta["header"]
        #print (response.body)
        line = response.body
        questionid_list = []
        pattern = re.compile(r'<a class="question_link" href="/question/(\d+)"')
        list_id1 = re.findall(pattern,line)
        list_id2 = list(set(list_id1)) #将list_id1去重
        header = {}
        header['Accept'] = 'application/json, text/plain, */*'
        header['Accept-Encoding'] = 'gzip, deflate, br'
        header['Accept-Language'] = 'zh-CN,zh;q=0.9'
        header['authorization'] = 'Bearer 2|1:0|10:1508430241|4:z_c0|92:Mi4xZkVFMEF3QUFBQUFBY0VCb2FCUWVDaWNBQUFDRUFsVk5vVjRRV2dEMFpaN3FqZ0prLVhHbktVSDRaN1NpaWpwRFN3|727560b9b73b25bb0eeb976ab13c9c94e127281f9018e3c8b0509f5aca8e686f'
        # header['Cache-Control'] = 'max-age=0'
        header['Connection'] = 'keep-alive'
        # header['Cookie'] = 'q_c1=fd9b1c59ad51492895200e21b028eac4|1504774361000|1495972167000; _zap=52694b79-8359-4106-b1d8-40b3c20cb228; q_c1=fd9b1c59ad51492895200e21b028eac4|1508948780000|1495972167000; d_c0="AIBC4XYqlQyPTsgJRWZ0HDLVxddP0vGJTmE=|1508948782"; l_cap_id="NjU5ZDliYzdhYzg2NDE1MmFkYzUxNWUyMzY4ZTVjNGI=|1509105785|228e083a3a692055d36252e341c16f5b23258f07"; r_cap_id="Y2NiYTRlMjI3NzIyNDc1MzgxOWEwYzkxYzU3MDAyNjI=|1509105785|f1123c20313661d1f3b0d89f40592c19d92da8b6"; cap_id="NTE3YmE1NzMzMThiNDZlZjgwMTIzNmI2NDg3MjRlZWM=|1509105785|4ce6eea344c15b2c8d0b919b9f3008c0fc5e69e6"; z_c0="2|1:0|10:1509106352|4:z_c0|92:Mi4xZkVFMEF3QUFBQUFBZ0VMaGRpcVZEQ2NBQUFDRUFsVk5zSzhhV2dDY2xXaVYxWGd1TXJyZTdId0Y3dk9FLWsteDJB|5ffd2bbbabc7ebba3bc76c841a9f260f1a68aa7a414ffe075c5378a1e137b9a0"; _xsrf=3baa1d2b72907ca6993e1f4cb73215d9; aliyungf_tc=AQAAAOlUPkVJ2gQA0zj3clbRjmKK5fC7'
        header['Host'] = 'www.zhihu.com'
        # header['Upgrade-Insecure-Requests'] = 1
        header['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'

        data = {}
        data['include'] = 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,upvoted_followees;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=best_answerer)].topics'
        data['offset'] = 3
        data['limit'] = 20
        data['sort_by'] = 'default'

        for num_question in range(len(list_id2)):
            exist = 0
            #file = open("/home/hadoop/zhihuSpider/zhihu_question_list.txt","r")
            file = open("E://zhihu_question_list.txt", "r")
            for line in file.readlines():
                if line.replace("\n","") == list_id2[num_question]:
                    exist = 1
                    break
            file.close()
            if exist == 0:
                #file = open("/home/hadoop/zhihuSpider/zhihu_question_list.txt","a")
                file = open("E://zhihu_question_list.txt", "a")
                file.write(list_id2[num_question] + "\n")
                file.close()
                kv = {'user-agent':'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'}
                #answer_url = "https://www.zhihu.com/api/v4/questions/" + list2[num_question] + "/answers?limit=10&offset=0"
                #list_id2[num_question] = str(57244153)
                answer_url = "https://www.zhihu.com/api/v4/questions/" + list_id2[num_question] + "/answers?limit=10&offset=0"
                #answer_url = 'https://www.zhihu.com/api/v4/questions/20214716/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccollapsed_counts%2Creviewing_comments_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.is_blocking%2Cis_blocked%2Cis_followed%2Cvoteup_count%2Cmessage_thread_token%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=3&offset=3'

                header['Referer'] = 'https://www.zhihu.com/question/' + list_id2[num_question]
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
        #print (content)

        question_title_url = "https://www.zhihu.com/api/v4/questions/" + Question_id
        header = {}
        header['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
        header['Accept-Encoding'] = 'gzip, deflate, br'
        header['Accept-Language'] = 'zh-CN,zh;q=0.9'
        header['Cache-Control'] = 'max-age=0'
        header['Connection'] = 'keep-alive'
        header['Host'] = 'www.zhihu.com'
        header['Upgrade-Insecure-Requests'] = 1
        header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0'
        header['authorization'] = 'Bearer 2|1:0|10:1508430241|4:z_c0|92:Mi4xZkVFMEF3QUFBQUFBY0VCb2FCUWVDaWNBQUFDRUFsVk5vVjRRV2dEMFpaN3FqZ0prLVhHbktVSDRaN1NpaWpwRFN3|727560b9b73b25bb0eeb976ab13c9c94e127281f9018e3c8b0509f5aca8e686f'

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

        #print (response.body)
        line = response.body.replace("\\\"","\\\\\\\"")
        title = json.loads(line).get('title')
        #print (title)

        zhihuItem = ZhihuItem()
        zhihuItem['KeyWord'] = response.meta['key_word']
        zhihuItem['Topic_name'] = response.meta['Topic_name']
        zhihuItem['Topic_id'] = response.meta['topic_id']
        zhihuItem['Question_id'] = response.meta['Question_id']
        zhihuItem['Question_content'] = title
        zhihuItem['Content'] = response.meta['content']
        #print ("pipelines")
        yield zhihuItem
