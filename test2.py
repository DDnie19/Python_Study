import json

# # count = 0
# DDOS_SIP_TXT = open('/home/d9/Desktop/data_web.txt','w')
with open('/home/d9/Desktop/web.json', 'r') as f:
    data = json.load(f)
    # print(data["skyeye-weblog"][0]["sip"])

    # for sip in range(0,10000):
        # s_ip = (data["skyeye-weblog"][sip]["data"])
        # s_ip = (data["skyeye-weblog"][sip]["host_raw"])
        # DDOS_SIP_TXT.write(s_ip + '\n' + '\r')
        # continue
    # for key in data:
        # if key == "host_raw":
    # print(len(data[0]))
    # print(str(data["skyeye-weblog"][0]["host_raw"]))
    print(type(data))
    # print(type(data["skyeye-weblog"][0]["host_raw"])
    # print(len(data["skyeye-weblog"][0]))
    for x in range(0,1000):
        # print(data["skyeye-weblog"][x]["host_raw"])
        if "15.1.2.6" == data["skyeye-weblog"][x]["host_raw"]:
            print(data["skyeye-weblog"][x]["host_raw"])
    # print(data["skyeye-weblog"])

    # for rst in range(0,100000):
    #     rst_code = (data["skyeye-tcpflow"][rst]["status"])
    #     # print(rst_code)
    #     if rst_code == "rst":
    #         # count = 0
    #         # count + 1
    #         # print (count)
    #         STATUS_CODE_RST.write(rst_code + '\n' + '\r')
    #     elif rst_code == "fin":
    #         STATUS_CODE_FIN.write(rst_code + '\n' + '\r')
    #     else:
    #         continue
# print (count)
# r = open('/home/d9/tcp-full-unspace-1.txt','r').readlines()
# r1 = open('/home/d9/ip-new-2.txt','w')
# for i in range(171488,342977):
#     print(r[i])
#     r1.write(r[i])
# r = open('/home/d9/top-10min-unspace.txt','r')
# r1 =open('/home/d9/top-10min-topcount.txt','w')
