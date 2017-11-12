# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class ZhihuPipeline(object):
    def process_item(self, item, spider):

        KeyWord = item.get("KeyWord")
        Topic_name = item.get("Topic_name")
        Topic_id = str(item.get("Topic_id"))
        Question_id = str(item.get("Question_id"))
        Question_content = item.get("Question_content")
        Content = item.get("Content").replace("\\\"", "\\\\\\\"").replace("\\\\","\\").decode("unicode_escape")

        line = "{\"KeyWord\":\""+KeyWord+"\",\"Topic_name\":\""+Topic_name+"\",\"Topic_id\":\""+Topic_id+"\",\"Question_id\":\""+Question_id+"\",\"Question_content\":\""+Question_content+"\",\"Content\":"+Content+"}"

        #os.chdir("/home/hadoop/zhihuSpider/")
        os.chdir('E:\\')
        file = codecs.open("zhihu_answer_list.json", mode='ab', encoding='utf-8')
        file.write(line + "\n")
        file.close()

        '''
        os.chdir('E:\\')
        print ("Content: ", item.get("Content"))
        #print (item.get("Question_content"))
        file = codecs.open("zhihu_answer_list.json", mode='ab', encoding='utf-8')
        #print (item)
        line = json.dumps(dict(item))
        #print (line)
        line = line.replace("\\\"", "\\\\\"").replace("\\\\", "\\").replace("\"Content\": \"{","\"Content\": {").replace("\", \"Topic_id\"",", \"Topic_id\"")
        #print(line.decode("unicode_escape"))
        #line = line.decode("unicode_escape")
        file.write(line.decode("unicode_escape") + "\n")
        file.close()
        '''

        '''
        file = codecs.open('1_zhihu.json', mode='ab', encoding='utf-8')
        line = json.dumps(dict(item)) + '\n'
        line = line.replace("\"Content\": \"{","\"Content\": {").replace("\", \"Topic_id\"",", \"Topic_id\"")
        file.write(line.decode("unicode_escape"))
        file.close()
        '''
        return item
