import json

# # count = 0
# DDOS_SIP_TXT = open('/home/d9/Desktop/tcp-10min.txt','w')
# with open('/home/d9/Desktop/tcp-10min.json', 'r') as f:
#     data = json.load(f)
#     print(data["skyeye-tcpflow"][0]["sip"])

#     for sip in range(0,68194):
#         s_ip = (data["skyeye-tcpflow"][sip]["sip"])
#         DDOS_SIP_TXT.write(s_ip + '\n' + '\r')
#         # continue
#         print(s_ip)
    
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
r = open('/home/d9/top-10min-unspace.txt','r')
r1 =open('/home/d9/top-10min-topcount.txt','w')
