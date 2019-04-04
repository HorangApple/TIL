import sys
sys.stdin = open('input.txt','r')

import copy
dy = [0,-1,0,1]
dx = [1,0,-1,0]
def solution(y,x):
    global maxi
    visited=[[False]*n for _ in range(n)]
    visited[y][x]=True
    k=1
    cnt=0
    line=[]
    lenght=0
    while cnt<homeCnt:
        cost=k*k+(k-1)*(k-1)
        if k!=1:
            save=copy.deepcopy(line)
            if k==2:
                save+=[[y,x]]
            line=[]
            for j in save:
                one=[]
                for i in range(4):
                    sy = j[0]+dy[i]
                    sx = j[1]+dx[i]
                    if -1<sy<n and -1<sx<n and not visited[sy][sx] and [sy,sx] not in line:
                        visited[sy][sx]=True
                        one+=[[sy,sx]]
                line+=one
            for i in line:
                if mp[i[0]][i[1]]>0:
                    cnt+=1
        elif k==1 and mp[y][x]>0:
            cnt+=1
            
        income = cnt*m-cost
        if income>=0:
            maxi=max(maxi,cnt)
        k+=1


TC = int(input())
for num in range(1,TC+1):
    n,m= map(int,input().split())
    mp=[list(map(int,input().split())) for _ in range(n)]
    maxi=0
    homeCnt=0
    for i in range(n):
        for j in range(n):
            if mp[i][j]>0:
                homeCnt+=1
    for i in range(n):
        for j in range(n):
                solution(i,j)
    print(f'#{num}',maxi)