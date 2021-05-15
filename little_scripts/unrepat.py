import chardet


# list = open("/home/d9/self/Pentester_tools/Web_Tools/dirsearch/db/dicc.txt","r")
# data =open(r"D:\NLP\rt-polaritydata\rt-polarity.pos", "rb").read()
data = open("/home/d9/tcp-full.txt","r",encoding="utf-8").readlines()

# list(filter(lambda x:data.count(x) == 1, data))

lst2 = {}.fromkeys(data).keys()

dicc = open("/home/d9/Desktop/tcp-full-new.txt","w",encoding="utf-8")

for x in lst2:
    dicc.write(x)

# print(len(dicc))
print(type(lst2))
dicc.close()
# for x in list2:
    # print(x)


