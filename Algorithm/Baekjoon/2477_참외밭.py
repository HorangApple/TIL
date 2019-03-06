import sys
sys.stdin=open("input.txt","r")

k=int(input())
maxRow = 0
maxColumn = 0
road=[]
cnt=0
for _ in range(6):
    inp=list(map(int,input().split()))
    if inp[0] in [1,2]:
        if maxRow<inp[1]:
            maxRow=inp[1]
            maxRowIdx=cnt
    elif inp[0] in [3,4]:
        if maxColumn<inp[1]:
            maxColumn=inp[1]
            maxColumnIdx=cnt
    cnt+=1
    road.append(inp)

if maxRowIdx==0 and maxColumnIdx==5:
    maxRowIdx+=2
    maxColumnIdx-=2
elif maxRowIdx==5 and maxColumnIdx==0:
    maxRowIdx-=2
    maxColumnIdx+=2
elif maxRowIdx>maxColumnIdx:
    maxRowIdx+=2
    if maxRowIdx>=6:
        maxRowIdx-=6
    maxColumnIdx-=2
else :
    maxColumnIdx+=2
    if maxColumnIdx>=6:
        maxColumnIdx-=6
    maxRowIdx-=2

print((maxRow*maxColumn-road[maxColumnIdx][1]*road[maxRowIdx][1])*k)