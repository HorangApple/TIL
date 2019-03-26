import sys
sys.stdin = open("input.txt","r")

n = int(input())
mp = list(map(int,input().split()))

mp.sort()

total=0
result=[]
for i in mp:
    total+=i
    result.append(total)

print(sum(result))