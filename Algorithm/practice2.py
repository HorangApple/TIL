import sys
sys.stdin = open("input.txt","r")

for num in range(10):
    length=int(input())
    results=[]
    nsMap=[list(map(int,input().split())) for _ in range(100)]
    for i in range(100):
        result=[]
        for j in range(100):
            if nsMap[j][i]>0:
                result.append(nsMap[j][i])
        results.append(result)
    count=0
    for oneline in results:
        before=0
        for i in range(len(oneline)):
            if oneline[i] == 1:
                before=1
            elif oneline[i] == 2 and before==1:
                before=0
                count+=1
    print(f'#{num+1} {count}')
            