import sys
sys.stdin = open("input.txt","r")

n,k = map(int,input().split())
money = []
result = []
for _ in range(n):
    money.append(int(input()))

for i in money[::-1]:
    if k>=i:
        cnt=0
        while k>=i:
            k-=i
            cnt+=1
        result.append(cnt)

print(sum(result))