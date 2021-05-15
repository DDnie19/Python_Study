r =open('/home/d9/Desktop/tcp-10min.txt','r').readlines()
r1 =open('/home/d9/Desktop/tcp-10min-unspace.txt','w')
for x in r:
    if x.split():
        r1.write(x.split()[0] + '\n')
        print(x.strip())