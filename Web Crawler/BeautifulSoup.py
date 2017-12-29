#-*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

def main():
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get("http://python123.io/ws/demo.html",headers = kv)
    demo = r.text
    soup = BeautifulSoup(demo,"html.parser")
    print(soup.prettify())
    
    print(soup.title,"\n",soup.head,"\n",r.request.headers)
    
    #print(soup.head,"\n",soup.head.name)
    #print(soup.head.parent,"\n",soup.head.parent.name)
    
    print("\n\n",soup.a,"\n",soup.a.attrs,"\nhref is: ",soup.a.attrs['href'])
    print(type(soup.a)," , ",type(soup.a.attrs))
    print(soup.a.string)
main()
