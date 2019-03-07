import sys
sys.stdin=open('input.txt','r')
dx=[1,-1]

def go(i):
    start=[i[1]]
    x = i[1]
    y = i[0]
    cnt=0
    while y<100:
        for j in range(2):
            if -1<x+dx[j]<100 and mp[y][x+dx[j]]=='1':
                k=1
                while True:
                    if -1<x+dx[j]*k<100 and mp[y][x+dx[j]*k]=='1':
                        k+=1
                        cnt+=1
                    else:
                        break
                cnt-=1
                x=x+dx[j]*(k-1)
                break
        y+=1
        cnt+=1
    result.append(start+[cnt])

TC=10
for num in range(1,TC+1):
    n = input()
    mp=[input().split() for _ in range(100)]
    start=[]
    result=[]
    for i in range(100):
        if mp[0][i]=='1':
            start.append([0,i])
    for i in start:
        go(i)

    minidx=0
    mini=10000
    for i in result:
        if mini>i[1]:
            mini=i[1]
            minidx=i[0]
        elif mini==i[1]:
            if minidx>i[0]:
                minidx=i[0]
    print("#{} {}".format(num,minidx))