#encoding:utf-8
import urllib2
def download(url):
    return urllib2.urlopen(url).read()  #导入urllib进行页面简单抓取

def download1(url):
    respone=urllib2.urlopen(url,timeout=10) #设置超时时间
    print (respone.info()) #获取respone请求信息
    print (respone.read(100))#抓取前100个字符
    print (respone.readlines())#每一行压入列表读取

url = "http://www.google.com"

#print download1(url)
try:      #try catch 捕获异常
    print (download1(url))
    pass
except urllib2.URLError as e:
    print ("web status error",e)
