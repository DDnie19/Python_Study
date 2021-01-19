#encoding:utf-8
#简单抓取页面python2.7
import urllib2
def download1(url):
    return urllib2.urlopen(url).read()

def download2(url):
    return urllib2.urlopen(url).readlines()

def download3(url):
    respone=urllib2.urlopen(url)
    while True:
        line=respone.readlines()
        if not line :
            break
        print line
        pass
url="http://www.baidu.com"
print download3(url)
#urllib2只能抓取http页面，无法抓取https。read方法抓取整个页面。readlines将页面存为列表。
#正则表达式
