'''
下载博客的sitemap.xml文件保存到本地，
利用xml解析出url，将url保存至对应的url文件，
然后利用curl将blog-url推送到百度。
'''
import requests
import os
import xml.dom.minidom


Files = "sitemap.xml"
Files2 = "urls.txt"

Url_list = []

Os_Curl = "curl -H 'Content-Type:text/plain' --data-binary @urls.txt \"link\""
File_Path = os.getcwd()


if os.path.exists(File_Path +"/" + Files):
    print("sitemap--已经存在！" + File_Path +"/" + Files)
else:
    print("sitemap--正在下载！")
    xml_file = requests.get("https://dnie9.com/sitemap.xml")
    xml_save = open("sitemap.xml" , "w")
    xml_save.write(xml_file.text)
    xml_save.close()
    print("sitemap--已经保存" + File_Path + "/" + Files)


if os.path.exists(File_Path +"/" + Files2):
    print("urls.txt--已经存在！" + File_Path +"/" + Files2)
else:
    #打开xml文档
    Dom = xml.dom.minidom.parse(Files)
    #得到文档元素对象
    Root = Dom.documentElement
    Root_Next = Root.getElementsByTagName('loc')
    #将节点元素的数据遍历出来，写入url.txt
    x = range(len(Root_Next))
    for n in x :
        Url = (Root_Next[n].firstChild.data)
        Url_list.append(Url)
    Url_Files = open("urls.txt" , "w")
    for l in x :
        Url_Files.write(Url_list[l] + "\n")
    print("url.txt--输出完成!" + File_Path +"/" + Files2)


os.system(Os_Curl)