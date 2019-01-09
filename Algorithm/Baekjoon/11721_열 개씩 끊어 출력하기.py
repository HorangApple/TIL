sen = input()
lists = []
count = len(sen)//10
i = 0
while i<count+1 :
    lists.append(sen[i*10:10*(i+1)])
    i += 1
for i in lists :
    print(i)