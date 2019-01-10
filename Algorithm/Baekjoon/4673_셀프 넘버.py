def d (n, lists):
    numList = [int(x) for x in str(n)]
    sumAll = sum(numList)+n
    if sumAll in lists:
        lists.remove(sumAll)
    return lists

lists = list(range(1,10001))


for i in range(1,10001) :
    d(i,lists)

for i in lists :
    print(i)