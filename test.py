import requests
#print(ip_txt.readlines())
url = "https://api.threatbook.cn/v3/scene/ip_reputation"
#query = {
#  "apikey":"32b25a6f5cbc4c459acf68a04b38ac406f1c159e923224208b02407d7bf5f81ae",
#  "resource":"158.203.93.255"
#}
for ip in ip_txt[12:-1]:
    ip_new = str(ip).strip()
    #response_list = []
    query = {
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
