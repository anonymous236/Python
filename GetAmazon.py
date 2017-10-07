def getAmazon() :
    url = "https://www.amazon.cn/"
    content = "gp/product/B01M8L5Z3Y"

    #需要设置文件头，将爬虫模拟为浏览器进行对网站的访问
    kv = {"User-Agent" :"Mozilla/5.0"}
    try :
        r = requests.get(url+content, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[1000:2000])
    except :
        return "爬取失败"
 
