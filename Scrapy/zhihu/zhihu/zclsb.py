# -*- coding: utf-8 -*-
import urllib
import requests
import json

url = "https://www.zhihu.com/node/TopicFeedList"

header = {}
header['Accept'] = '*/*'
header['Accept-Encoding']='gzip, deflate, br'
header['Accept-Language']='zh-CN,zh;q=0.9'
header['Connection']='keep-alive'
header['Content-Length']='103'
header['Content-Type']='application/x-www-form-urlencoded; charset=UTF-8'
#header['Cookie']='q_c1=fd9b1c59ad51492895200e21b028eac4|1504774361000|1495972167000; _zap=52694b79-8359-4106-b1d8-40b3c20cb228; q_c1=fd9b1c59ad51492895200e21b028eac4|1508948780000|1495972167000; d_c0="AIBC4XYqlQyPTsgJRWZ0HDLVxddP0vGJTmE=|1508948782"; l_cap_id="NjU5ZDliYzdhYzg2NDE1MmFkYzUxNWUyMzY4ZTVjNGI=|1509105785|228e083a3a692055d36252e341c16f5b23258f07"; r_cap_id="Y2NiYTRlMjI3NzIyNDc1MzgxOWEwYzkxYzU3MDAyNjI=|1509105785|f1123c20313661d1f3b0d89f40592c19d92da8b6"; cap_id="NTE3YmE1NzMzMThiNDZlZjgwMTIzNmI2NDg3MjRlZWM=|1509105785|4ce6eea344c15b2c8d0b919b9f3008c0fc5e69e6"; z_c0="2|1:0|10:1509106352|4:z_c0|92:Mi4xZkVFMEF3QUFBQUFBZ0VMaGRpcVZEQ2NBQUFDRUFsVk5zSzhhV2dDY2xXaVYxWGd1TXJyZTdId0Y3dk9FLWsteDJB|5ffd2bbbabc7ebba3bc76c841a9f260f1a68aa7a414ffe075c5378a1e137b9a0"; _xsrf=3baa1d2b72907ca6993e1f4cb73215d9; aliyungf_tc=AQAAAKH5mTDeQAwAwDj3cgg2aGhruAd8; _xsrf=3baa1d2b72907ca6993e1f4cb73215d9'
header['Host']='www.zhihu.com'
header['Origin']='https://www.zhihu.com'
header['Referer']='https://www.zhihu.com/topic'
header['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
header['X-Requested']='XMLHttpRequest'
header['X-Xsrftoken']='3baa1d2b72907ca6993e1f4cb73215d9'

#data=urllib.urlencode(d)
params = json.dumps({"offset": 1, "topic_id": 108840, "feed_type": "smart_feed",})
payload = {"method": "next", "params": params,}
r = requests.post(url,data=payload,headers=header)

print (r.headers)
print (r.status_code)
print (r.text)
print (r)