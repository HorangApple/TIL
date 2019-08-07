import sys
sys.stdin = open("input.txt","r")

dx=[0,1]
dy=[1,0]

def solution(start,n):
    que=[start]
    while que:
        go=que.pop(0)
        for i in range(2):
            x=go[1]+dx[i]
            y=go[0]+dy[i]
            if x<n and y<n and inp[y][x]>0:
                inp[y][x]=0
                if [y,x] not in que:
                    que.append([y,x])
    return go

def merge(l,r):
    result=[]
    i,j=0,0
    while i<len(l) and j<len(r):
        a=l[i][0]*l[i][1]
        b=r[j][0]*r[j][1]
        if a > b:
            result.append(r[j])
            j+=1
        elif a==b:
            if l[i][0]>r[j][0]:
                result.append(r[j])
                j+=1
            else:
                result.append(l[i])
                i+=1 
        else:
            result.append(l[i])
            i+=1
    if i!=len(l):
        for k in 

def mySort(result,y,x):
    middle=(x+y)//2
    if len(result)==1:
        return result
    l=result[:middle]
    r=result[middle:]
    l=mySort(l,0,middle)
    r=mySort(r,0,y-middle)

    return merge(l,r)
            

TC=int(input())
for num in range(1,TC+1):
    n=int(input())
    inp=[list(map(int,input().split())) for _ in range(n)]
    result=[]
    for i in range(n):
        for j in range(n):
            if inp[i][j]>0:
                start=[i,j]
                end=solution(start,n)
                result.append([end[0]-start[0]+1,end[1]-start[1]+1])
    mySort(result)
    print(f'#{num} {len(result)}',end=" ")
    for i in result:
        print(i[0],i[1],end=" ")
    print("")