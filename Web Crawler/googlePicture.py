# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import re
import urllib
import os
key_word = "墨镜"
trans_word = urllib.quote(key_word)

path = "G:\\picture"
os.chdir(path)
if not os.path.exists(key_word.decode("utf-8")):
    os.mkdir(key_word.decode("utf-8"))
os.chdir(key_word.decode("utf-8"))

url="https://www.google.com.hk/search?&safe=strict&yv=2&newwindow=1&tbm=isch&q=" + trans_word + "使用开发者工具获得URL"

list = []
sum = total = 0
while(1):
    url = url.split("&ijn=")[0] + "&ijn=" + str(sum) + "&start=" + str(sum*100) + "&asearch=" + url.split("&asearch=")[1]
    sum += 1
    r = requests.get(url)
    print r.text
    pattern = re.compile(r'imgurl=(.+?)\u0026amp')
    object_url = re.findall(pattern, r.text)

    for i in range(len(object_url)):
        try:
            suburl = object_url[i].replace("\\","")
            if suburl not in list:
                r = requests.get(suburl,timeout=30)
                list.append(suburl)
                total += 1
                path = str(total) + ".jpg"
                file = open(path, "wb")
                file.write(r.content)
                file.close()
        except:
            print object_url[i].replace("\\", "")
    if total>550:
        break
