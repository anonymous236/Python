#-*- coding: UTF-8 -*-
import requests

def Request():
    try:
        url = "http://www.baidu.com/s"
        kv = {'wd':'Python'}
        r = requests.get(url,params=kv)
        r.encoding = r.apparent_encoding
        r.raise_for_status
        print(r.request.url)
        print(r.text[1000:2000])
    except:
        print("爬取失败")
        
if __name__ == "__main__":
    Request()
