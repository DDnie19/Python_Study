import requests
#print(ip_txt.readlines())
url = "https://api.threatbook.cn/v3/scene/ip_reputation"
#query = {
#  "apikey":"XXXXXX",
#  "resource":"158.203.93.255"
#
ip_txt = open('/home/d9/1self/Pentester_tools/self_little_scripts/1.python/Python_study/little_scripts/top5-sessions.txt','r')

for ip in ip_txt:
    ip_new = str(ip).strip()
    #response_list = []
    query = {
        "apikey":"XXXXXX",
        "resource": ip_new,
        "lang":"zh"
    }
    try:
        response = requests.request("GET", url, params=query, timeout = 2)
        print(response.json())
    except requests.exceptions.ConnectionError as e:
        print ("Name or service not known")
        continue
    #response_data = response.json()
    #response_list.append(response_data)
    #for D in response_list:
    #    dicc.wirte(D)
    #    dicc.close()
