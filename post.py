# @By LYN
# v 1.0.

import requests
from bs4 import BeautifulSoup as bs
from lxml import etree

url="https://news.baidu.com/tech"
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
cookies={}
r=requests.get(url,headers=headers,allow_redirects=True)
info=r.text
data=etree.HTML(info)
content=data.xpath("//ul[@class=\"ulist mix-ulist\"]/li/a/text()")
link_list=data.xpath("//ul[@class=\"ulist mix-ulist\"]/li/a/@href")
for link in link_list:
    content_list=requests.get(link,headers=headers)
    f_name=link.split("=")[1]
    # with open(f_name,"w",encoding="utf-8"):
    #     f_name.write(content_list,)
    print(f_name)
        
print(link_list)

