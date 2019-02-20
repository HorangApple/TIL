import sys
sys.stdin = open("input.txt","r")

TC=int(input())

for num in range(1,TC+1):
    length=int(input())
    inp=[list(map(int,input().split())) for _ in range(length)]
    total=0
    minidxX=0
    xList=list(range(length))
    for i in range(length):
        for k in xList:
            if k>-1:
                minidxX=k
                break
        for j in range(length):
            if (j in xList) and inp[i][minidxX]>inp[i][j] :
                minidxX=j
        xList[minidxX]=-1
        total+=inp[i][minidxX]
    
    
    print(f'#{num} {total}')