import sys
sys.stdin = open("input.txt","r")

n=int(input())
line=[0]*1001
for _ in range(n):
    inp=list(map(int,input().split()))
    line[inp[0]]=inp[1]
top=max(line)
cnt=0
idx=0
topIdxList=[]
for i in line:
    if i>0:
        cnt+=1
        if i==top:
            topIdxList.append(idx)
    if cnt==n:
        break
    idx+=1

maxi=0
total1=0
cnt1=0
for i in line:
    if i==top:
        break
    elif i > maxi:
        maxi=i
    total1+=maxi
    cnt1+=1

maxi=0
total2=0
cnt2=0
for i in line[::-1]:
    if i==top:
        break
    elif i> maxi:
        maxi=i
    total2+=maxi

print(total1+top*(topIdxList[-1]-topIdxList[0]+1)+total2)