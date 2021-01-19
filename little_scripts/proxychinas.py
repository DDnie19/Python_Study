import  json
import  requests
import  time
import  os
from bs4 import BeautifulSoup

url ="http://www.kuaidaili.com/free/"
headers ={'User-Agent':'Mozilla/4.0(windows NT 6.1; WOW 64; rv:57.0) Gecko/20100101 Chorme'} 

def get_proxy_datas():
    r = requests.get(url,headers=headers)
    content = r.content
    soup =BeautifulSoup(content,'lxml')
    ips = soup.find_all('td',attrs={'data-title':'IP'})
    ports = soup.find_all('td',attrs={'data-title':'ports'})
    print('开始写入代理IP和端口……')
    write_conf(ips,ports)
    print("代理IP和端口写入完成，将退出……")

def write_conf(ips,ports):
    for i in range(0,len(ips)):
        print("--->IP:"+ips[i].string+"PORT:"+ports[i].string+"<---")
        time.sleep(1)
        with open('/etc/proxychains.conf','a+') as f:
            f.write('http %s %s/n' %(ips[i].string,ports[i].string))
