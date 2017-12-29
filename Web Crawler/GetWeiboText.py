'''
  # 本代码实现从text中读取微博id信息，进而爬取到微博内容
  # 用了BeautifulSoup库、json库得到text信息；用正则表达式去掉text中的标签信息
'''

#-*- coding: UTF-8 -*-
import requests
import json
import re
from bs4 import BeautifulSoup

def webpage(link):
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(link,headers = kv)
    demo = r.text
    soup = BeautifulSoup(demo,"html.parser")
    line = str(soup.body.script)
    loc1 = line.index("\"status\":")
    loc2 = line.index("\"tipScheme\":")
    loc2 = line.index("}",loc2+2)
    
    # 得到"status"的JSON信息
    line = line[loc1+10:loc2+1]
    
    # 将已编码的 JSON 字符串解码为 Python 对象
    json_line = json.loads(line)
    text = json_line.get('text')
    
    # 将正则表达式的字符串形式编译为dr实例
    dr = re.compile(r'<[^>]*>',re.S)
    text = dr.sub('',text).replace('\n','').replace('\r','')
    
    weibo_id = json_line.get('mid')
    user_id = json_line.get('user').get('id')
    reposts_count = str(json_line.get('reposts_count'))
    file_out = open('文件名.txt','a')
    file_out.write(str(weibo_id)+'\t'+str(user_id)+'\t'+reposts_count+'\t'+text.encode('utf-8')+'\n')
    file_out.close()

url = "微博URL"
# 读取微博id
file = open('文件名.txt','r')
for line in file.readlines():
    id = line.split('\t')[0]
    link = url+id
    try:
        webpage(link)
    except:
        print(link)
    
file.close()
    
