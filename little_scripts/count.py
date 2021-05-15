from collections import Counter

r = open('little_scripts/top5-sessions.txt', 'r').readlines()
# r1 = open('')
print(len(r))
count1 = 0
for x in r:
    r1 = open('/home/d9/Desktop/tcp-10min-unspace.txt', 'r').readlines()
    count = 0
    for y in r1:
        if y.find(x) >= 0:
            count += 1
    print(x + ' ==== ' + str(count))
    count1+=count
print('******************************************')
print(count1)


# collection_words = Counter(r)
# print(collection_words)
# print(type(collection_words))

#