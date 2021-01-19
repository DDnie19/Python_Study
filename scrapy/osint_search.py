#encoding:utf-8
import re
import json
import selenium
import selenium.webdriver
from selenium import webdriver

def get_search_byname(searname,seartype):
    url="https://www.osint-labs.org/search/s.php?q="+searname+"&sid="+seartype+""#抓取的页面
    driver= selenium.webdriver.Chrome()#打开谷歌浏览器模拟访问
    driver.get(url)
    pagesource=driver.page_source#获取页面源代码
    restr="""<div class="gsc-result-info" id="resInfo-0">([\s\S]*?)</div>"""#正则抓取想要的内容
    regx= re.compile(restr,re.IGNORECASE)#正则匹配忽略大小写
    mylist=regx.findall(pagesource)
    driver.close()#关闭浏览器
    if len(mylist)==0:#如果没有抓取到指定内容则中断程序
        return "not ok"
    else:
        return mylist[0]#返回抓取到的内容

new_input=str(raw_input("Enter Some For Search:"))#获取用户的输入

sid_dic={"0":"默认","1":"文档","2":"代码","3":"脑图","4":"安全",#抓取匹配的字典
        "5":"漏洞","6":"维基","7":"员工档案","8":"电报"}
for sid in sid_dic.keys():
    print new_input,sid,get_search_byname(new_input,sid)
