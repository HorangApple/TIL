import sys
sys.stdin=open("input.txt","r")

def bfs():
    visited=[]
    cnt=0
    while que:
        v=que.pop(0)
        visited.append(v)
        mp[v[0]][v[1]]=0
        cnt+=1
        for i in range(4):
            x=v[1]+dx[i]
            y=v[0]+dy[i]
            if -1<y<n and -1<x<n and ([y,x] not in que) and mp[y][x]==1:
                que.append([y,x])
    cnts.append(cnt)

dx=[0,1,0,-1]
dy=[1,0,-1,0]

n=int(input())
mp=[[0]*n for _ in range(n)]
for i in range(n):
    k=0
    for j in input():
        mp[i][k]=int(j)
        k+=1
que=[]
cnts=[]
for i in range(n):
    for j in range(n):
        if mp[i][j]==1:
            que.append([i,j])
            bfs()
print(len(cnts))
cnts.sort()
for i in cnts:
    print(i)