import sys
sys.stdin = open("input.txt","r")

TC= int(input())
for num in range(1,TC+1):
    n,m=map(int,input().split())
    mp=[list(map(int,input().split())) for _ in range(n)]
    result=[]
    for i in range(n-m+1):
        for j in range(n-m+1):
            a=i
            one = []
            while a<i+m:
                one+=mp[a][j:j+m]
                a+=1
            result.append(one)
    maxi=0
    for i in result:
        a=sum(i)
        if maxi<a:
            maxi=a
    print("#{} {}".format(num,maxi))