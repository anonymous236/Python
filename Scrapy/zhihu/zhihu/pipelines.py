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
        
        # 存储为json格式：
        line = "{\"KeyWord\":\""+KeyWord+"\",\"Topic_name\":\""+Topic_name+"\",\"Topic_id\":\""+Topic_id+"\",\"Question_id\":\""+Question_id+"\",\"Question_content\":\""+Question_content+"\",\"Content\":"+Content+"}"

        os.chdir('路径')
        file = codecs.open("名称.json", mode='ab', encoding='utf-8')
        file.write(line + "\n")
        file.close()
        return item
