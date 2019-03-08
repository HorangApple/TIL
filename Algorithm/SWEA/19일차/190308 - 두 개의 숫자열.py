import sys
sys.stdin=open('input.txt','r')

TC=int(input())
for num in range(1,TC+1):
    n,m = map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    result=[]
    i,j=0,0
    start=0
    while True:
        total=0
        while i<n and j<m:
            total+=a[i]*b[j]
            i+=1
            j+=1
        result.append(total)
        if n>m:
            start+=1
            i=start
            j=0
        elif n<m:
            start += 1
            j = start
            i = 0
        if start > abs(n - m):
            break
    print("#{} {}".format(num,max(result)))