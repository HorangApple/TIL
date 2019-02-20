import sys
sys.stdin = open("input.txt","r")

for num in range(10):
    length=int(input())
    nsMap=[list(map(int,input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(i,100):
            nsMap[i][j],nsMap[j][i]=nsMap[j][i],nsMap[i][j]
    count=0
    for oneline in nsMap:
        before=0
        for i in range(100):
            if oneline[i] == 1:
                before=1
            elif oneline[i] == 2 and before==1:
                before=0
                count+=1
    print(f'#{num+1} {count}')
            