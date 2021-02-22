import json

# count = 0

with open('', 'r') as f:
    data = json.load(f)
    # print(data["skyeye-tcpflow"][0]["sip"])

    # for sip in range(0,100000):
    #     s_ip = (data["skyeye-tcpflow"][sip]["sip"])
    #     DDOS_SIP_TXT.write(s_ip + '\n' + '\r')
    #     # continue
    # count = 0
    for rst in range(0,100000):
        rst_code = (data["skyeye-tcpflow"][rst]["status"])
        # print(rst_code)
        if rst_code == "rst":
            # count = 0
            # count + 1
            # print (count)
            STATUS_CODE_RST.write(rst_code + '\n' + '\r')
        elif rst_code == "fin":
            STATUS_CODE_FIN.write(rst_code + '\n' + '\r')
        else:
            continue
# print (count)
