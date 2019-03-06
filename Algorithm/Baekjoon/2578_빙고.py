# https://www.acmicpc.net/problem/2578
import sys
sys.stdin = open("input.txt","r")

bingo=[list(map(int,input().split())) for _ in range(5)]
orders=[list(map(int,input().split())) for _ in range(5)]
bingoIdx=[[] for _ in range(26)]
for i in range(5):
    for j in range(5):
        bingoIdx[bingo[i][j]]+=[j,i] # [y,x]
#----
rowSum=[]
columnSum=[]
diagonalLineSum=[]
for i in bingo:
    rowSum.append(sum(i))
for i in range(5):
    total=0
    for j in range(5):
        total+=bingo[j][i]
    columnSum.append(total)
total=0
for i, j in zip(range(5),range(5)):
    total+=bingo[i][j]
diagonalLineSum.append(total) # i==j
total=0
for i, j in zip(range(4,-1,-1),range(5)):
    total += bingo[i][j]
diagonalLineSum.append(total) # i+j=4
#----
cnt=0
cnt2=0
for order in orders:
    for i in order:
        point=bingoIdx[i]
        rowSum[point[1]]-=i
        if rowSum[point[1]]==0:
            cnt+=1
        columnSum[point[0]]-=i
        if columnSum[point[0]]==0:
            cnt+=1
        if point[0]==point[1]:
            diagonalLineSum[0]-=i
            if diagonalLineSum[0]==0:
                cnt+=1
        if (point[0]+point[1])==4:
            diagonalLineSum[1]-=i
            if diagonalLineSum[1]==0:
                cnt+=1
        cnt2+=1
        if cnt>=3:
            print(cnt2)
            break
    if cnt >= 3:
        break