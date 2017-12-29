#-*- coding: UTF-8 -*-
import requests
import os

def main():
    url = "http://img3.redocn.com/tupian/20150421/xiaohuakafeikafeibeibiankuangsucai_4013296.jpg"
    root = "E://Document//Python//dmeo//mooc//"
    path = root + url.split('/')[-1]
    
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            r.raise_for_status
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功.")
        else:
            print("文件已存在.")
    except:
        print("爬取失败.")

main()
