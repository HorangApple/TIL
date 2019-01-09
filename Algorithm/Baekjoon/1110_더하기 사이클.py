n = input()
def makeList (inputs):
    return [x for x in str(inputs)]
lists = makeList(n)

if(len(lists)==1):
    lists.insert(0,'0')

count = 0
firstlists = lists[:]
while 1 :
    twoSum = int(lists[0]) + int(lists[1])
    resultList = makeList(twoSum)
    lists.append(resultList[-1])
    lists.remove(lists[0])
    count += 1
    if firstlists == lists :
        break
print(count)
        