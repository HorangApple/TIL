import sys
sys.stdin = open("input.txt","r")

T=int(input())
for num in range(1,T+1):
    n=int(input())
    mp=[[] for _ in range(n)]
    for i in range(n):
        for j in input():
            mp[i]+=[int(j)]
    l=n//2
    r=n//2
    i=1
    result=[]
    for oneLine in mp:
        result.append(sum(oneLine[l:r+1]))
        if r==n-1:
            i=-1
        l-=i
        r+=i
    print("#{} {}".format(num,sum(result)))