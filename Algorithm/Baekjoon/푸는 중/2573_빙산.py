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
    print("실행 시간: ", elapsed,"s")
    print('종료 >>>> ')
    print(line)

log()
#------------
from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(que):
    while len(que)>0:
        v=que.popleft()
        for i in range(4):
            sx=v[1]+dx[i]
            sy=v[0]+dy[i]
            if -1<sx<m and -1<sy<n:
                if mp[sy][sx]>0:
                    mp[sy][sx]-=1

def chk(v,visited):
    que2=deque()
    que2.append(v)
    while len(que2):
        y,x=que2.popleft()
        for i in range(4):
            sx=x+dx[i]
            sy=y+dy[i]
            if -1<sx<m and -1<sy<n and [sy,sx] not in visited:
                if mp[sy][sx]>0:
                    que2.append([sy,sx])
                    visited.append([sy,sx])

def solution():
    que=deque()
    year=0
    while True:
        visited=[]
        placeCnt=0
        for i in range(n):
            for j in range(m):
                if mp[i][j]<=0 and [i,j] not in que:
                    que.append([i,j])
                elif [i,j] not in visited:
                    visited.append([i,j])
                    chk([i,j],visited)
                    placeCnt+=1
                    if placeCnt>1:
                        print(year)
                        return
        if len(que)==0:
            print(0)
            return
        bfs(que)
        year+=1

n,m=map(int,input().split())
mp=[list(map(int,input().split())) for _ in range(n)]
solution()

#------------
endlog()