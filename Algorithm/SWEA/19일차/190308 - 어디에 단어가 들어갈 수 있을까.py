import sys
sys.stdin=open('input.txt','r')

dx=[1,0]
dy=[0,1]
# mode
def bfs(s,mode):
    que=[[s[0],s[1]]]
    cnt=0
    while que:
        v=que.pop(0)
        visited.append(v)
        cnt+=1
        if cnt>k:
            return cnt
        x,y=v[1]+dx[mode],v[0]+dy[mode]
        if -1<x<n and -1<y<n and mp[y][x]==1 and ([y,x] not in visited) and ([y,x] not in que):
            que.append([y,x])
            visited.append([y,x])
    return cnt

TC=int(input())
for num in range(1,TC+1):
    n,k=map(int,input().split())
    mp=[list(map(int, input().split())) for _ in range(n)]
    visited=[]
    cnt=0
    for i in range(n):
        for j in range(n):
            if mp[i][j]==1 and [i,j] not in visited:
                space=bfs([i,j],0)
                if space==k:
                    cnt+=1
    visited=[]
    for i in range(n):
        for j in range(n):
            if mp[j][i]==1 and [j,i] not in visited:
                space=bfs([j,i],1)
                if space==k:
                    cnt+=1
    print("#{} {}".format(num,cnt))
