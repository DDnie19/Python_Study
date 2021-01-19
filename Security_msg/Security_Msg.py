'''
python3
author:D9
实现功能：抓取阿里安全预警，腾讯应急响应中心blog，
将安全通告的名称/链接，以邮件的形式发送到网络安全部的邮箱
全自动实现，可以在服务器设置定时任务每隔3小时运行一次。
1.确定权威的国内外安全厂商公告，确定要抓取的站点。
2.实现email-发送功能。
3.不涉及数据库存储，将内容放在邮箱中。
'''
import smtplib, ssl , time , datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import requests
from bs4 import BeautifulSoup


#定义e-mail所需信息，使用ssl，根据不同邮箱定义。
port = 465  
smtp_server = "smtp.163.com"
sender_email = "XXXXXX"  
receiver_email = "XXXXXX"  
password = 'XXXXX'

#定义requests变量，使用bs4进行指定tag标签爬取，获得链接，标题，时间。
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
Tencent_Url = "https://security.tencent.com/index.php/blog"
Tencent_Url_2 = "https://security.tencent.com/" 
Ali_Url = "https://m.aliyun.com/doc/notice_list/9213612.html"
Ali_Url_2 = "https://m.aliyun.com"

#时间用于对比是否为今天最新的,一般第一个tag的日期和系统时间一致就是最新的发布，则进行邮件推送。
ISOTIMEFORMAT_1 = '%Y-%m-%d'
ISOTIMEFORMAT_2 = '%m-%d'
Ostime_Tencent = datetime.datetime.now().strftime(ISOTIMEFORMAT_1)
Ostime_Ali = datetime.datetime.now().strftime(ISOTIMEFORMAT_2)

#阿里通告抓取。
def AliYun(url):
    Ali_Title = []
    Ali_Link = []
    Ali_Text = requests.get(Ali_Url,headers = headers ).text
    Ali_Soup = BeautifulSoup(Ali_Text,features="lxml")
    Ali_First = Ali_Soup.find("div","date")
    if str(Ostime_Ali) == str(Ali_First.string):
        try:
            for i in Ali_Soup.find_all("a","notice-list-item"):
                Ali_Link.append(Ali_Url_2 + i['href'])
                pass
            for x in Ali_Soup.find_all("div","title"):
                Ali_Title.append(x.string)
                pass
                text = """
                    您好!
                    网络安全部-安全漏洞通告！
                    阿里漏洞通告
                    通告信息全部来自阿里漏洞通告
                    自动获取并分享安全信息
                    Python脚本自动生成--作者：D9
                    """
                html = '<html> \
                            <body> \
                                    <h4>阿里漏洞通告</h4>\
                                    通告信息全部来自: \
                            <a href = "https://m.aliyun.com/doc/notice_list/9213612.html">“阿里云漏洞通告”</a> \
                            <div class="content_title"><a href='+ Ali_Link[0] +' target="_blank">'+ Ali_Title[0] + '</a></div> \
                                <br></br>利用Python脚本自动获取安全漏洞，使用电子邮件定时分享.<br></br>网络安全部:D9\
                                <br></br><img class="img2" src="http://XXXX.png " alt="">\
                            </body>\
                        </html>\
                            '
            mail(port=port,sender_email=sender_email,receiver_email=receiver_email,password=password,text=text,html=html)
        except :
            # mail(port=port,sender_email=sender_email,receiver_email=receiver_email,password=password,text="爬虫挂掉了",html="<h3>爬虫挂掉了！</h3>")
            print("Pro is Die")
            pass
    else:
        # mail(port=port,sender_email=sender_email,receiver_email=receiver_email,password=password,text="没有最新告警",html="没有最新告警")
        print("no one")

#腾讯响应中心Blog抓取。
def Tencent(url):
    Tencent_Title = []
    Tencent_link = []
    Tencent_Text = requests.get(url,headers=headers).text
    Tencent_Soup = BeautifulSoup(Tencent_Text,features="lxml")
    Tencent_First = Tencent_Soup.find("span","info_date")
    if str(Ostime_Tencent) == str(Tencent_First.span.string):
        try:
            for i in Tencent_Soup.find_all('div','content_title'):
                Tencent_Title.append(i.string)
                Tencent_link.append(Tencent_Url_2 + i.a['href'])
                pass
                # Create the plain-text and HTML version of your message
                text = """
                您好!
                网络安全部-安全漏洞通告！
                腾讯应急响应中心-安全漏洞通告
                通告信息全部来自腾讯应急响应中心Blog
                自动获取并分享安全信息
                Python脚本自动生成--作者：D9
                """
                html = '<html> \
                            <body> \
                                    <h4>腾讯应急响应中心-安全信息</h4>\
                                    通告信息全部来自: \
                            <a href = "https://security.tencent.com/index.php/blog">“腾讯应急响应中心Blog”</a> \
                            <div class="content_title"><a href='+ Tencent_link[0] +' target="_blank">'+ Tencent_Title[0] + '</a></div> \
                            <br></br>利用Python脚本自动获取安全信息，使用电子邮件定时分享.<br></br>网络安全部:D9\
                                <br></br><img class="img2" src="http://XXXX.png " alt="">\
                            </body>\
                        </html>\
                            '
            mail(port=port,sender_email=sender_email,receiver_email=receiver_email,password=password,text=text,html=html)
        except :
            # mail(port=port,sender_email=sender_email,receiver_email=receiver_email,password=password,text="爬虫挂掉了",html="<h3>爬虫挂掉了！</h3>")
            print("Pro is Die")
            pass
    else:
        print("no one")


#邮件函数接收端口，发件人，收件人，密码和html消息。我这里是网易的把自己的发件服务器替换即可。
def mail(port,sender_email,receiver_email,password,text,html):
    time.sleep(10)
    message = MIMEMultipart("alternative")
    message["Subject"] = "安全信息共享"
    message["From"] = sender_email
    message["To"] = receiver_email
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.163.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
        server.quit()


if __name__ == "__main__":
    Tencent(Tencent_Url)
    AliYun(Ali_Url)
    pass
