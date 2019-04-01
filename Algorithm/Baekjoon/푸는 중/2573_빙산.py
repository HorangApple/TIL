import sys
sys.stdin=open('input.txt','r')
from time import time, strftime, localtime
from datetime import timedelta

def log():
    global start
    start = time()
    print('시작 >>>> ')

def endlog():
    line = "=" * 40
    elapsed = time() - start
    print("실행 시간: ", elapsed*1000,"s")
    print('종료 >>>> ')
    print(line)

log()
#------------

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(que,deletePoint,visited):
    global placeCnt,front,back
    placeCnt+=1
    while front<=back:
        v=que[front]
        front+=1
        visited[v[0]][v[1]]=True 
        cnt=0
        for i in range(4):
            x=v[1]+dx[i]
            y=v[0]+dy[i]
            if -1<x<m and -1<y<n:
                if mp[y][x]<=0:
                    cnt+=1
                elif mp[y][x]>0 and not visited[y][x]:
                    for k in range(front,back+1):
                        if que[k]==[y,x]:
                            break
                    else:
                        back+=1
                        que[back]+=[y,x]
        deletePoint.append([v[0],v[1],cnt])
    

def solution():
    global placeCnt,front,back
    year=0
    while placeCnt:
        visited=[[False]*m for _ in range(n)]
        placeCnt=0
        for i in range(n):
            for j in range(m):
                if mp[i][j]>0 and not visited[i][j]:
                    deletePoint=[]
                    front=0
                    back=-1
                    que=[[] for _ in range(10000)]
                    back+=1
                    que[back]+=[i,j]
                    bfs(que,deletePoint,visited)
                    if placeCnt>1:
                        print(year)
                        return
        for k in deletePoint:
            mp[k[0]][k[1]]-=k[2]
        year+=1
    print(0)

n,m=map(int,input().split())
mp=[list(map(int,input().split())) for _ in range(n)]
placeCnt=1
front,back=0,0
solution()

#------------
endlog()

# index로 접근하는 것이 가장 빠르다.