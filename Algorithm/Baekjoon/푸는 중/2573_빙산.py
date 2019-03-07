import sys
sys.stdin=open('input.txt','r')

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(que,deletePoint,visited):
    while que:
        v=que.pop(0)
        visited.append(v)
        cnt=0
        for i in range(4):
            x=v[1]+dx[i]
            y=v[0]+dy[i]
            if -1<x<m and -1<y<n:
                if mp[y][x]==0:
                    cnt+=1
                elif mp[y][x]!=0 and ([y,x] not in visited) and ([y,x] not in que):
                    que.append([y,x])
        deletePoint.append([v[0],v[1],cnt])

def search():
    cnt=0
    for i in range(n):
        for j in range(m):
            if mp[i][j]>0:
               cnt+=1
    return cnt

def solution():
    year=0
    fullnum=1
    while fullnum:
        visited=[]
        fullnum=search()
        for i in range(n):
            for j in range(m):
                if mp[i][j]>0 and ([i,j] not in visited):
                    deletePoint=[]
                    que=[[i,j]]
                    bfs(que,deletePoint,visited)
                    # for q in mp:
                    #     print(q)
                    # print(len(visited),len(deletePoint))
                    if len(visited)!=fullnum:
                        print(year)
                        return
                    for k in deletePoint:
                        mp[k[0]][k[1]]-=k[2]
                        if mp[k[0]][k[1]]<0:
                            mp[k[0]][k[1]]=0
        year+=1
    print(0)

n,m=map(int,input().split())
mp=[list(map(int,input().split())) for _ in range(n)]
solution()