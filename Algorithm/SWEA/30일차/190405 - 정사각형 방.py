import sys
sys.stdin = open('input.txt','r')

dy=[0,1,0,-1]
dx=[1,0,-1,0]

def solution(y,x):
    global i,j
    cnt=1
    que=[[y,x]]
    temp=[[y,x]]
    while len(que)>0:
        y,x=que.pop(0)
        k=0
        for idx in range(4):
            sy=y+dy[idx]
            sx=x+dx[idx]
            if -1<sy<n and -1<sx<n:
                if mp[sy][sx]-mp[y][x] == 1:
                    if visited[sy][sx]>-1:
                        cnt+=visited[sy][sx]
                        for one in temp:
                            visited[one[0]][one[1]]=cnt-visited[one[0]][one[1]]
                        return visited[i][j]
                    que.append([sy,sx])
                    temp.append([sy,sx])
                    visited[sy][sx]=cnt
                    cnt+=1
                    k+=1
                    break
        if k==0:
            for one in temp:
                visited[one[0]][one[1]]=cnt-visited[one[0]][one[1]]
            return visited[i][j]
            

TC = int(input())
for num in range(1,TC+1):
    n = int(input())
    mp=[list(map(int,input().split())) for _ in range(n)]
    visited=[[-1]*n for _ in range(n)]
    maxi=0
    roomNum=999999
    result=[]
    for i in range(n):
        for j in range(n):
            if visited[i][j]>-1:
                cnt=visited[i][j]
            else:
                visited[i][j]=0
                cnt=solution(i,j)
            if maxi<cnt:
                maxi=cnt
                roomNum=mp[i][j]
            elif maxi==cnt:
                roomNum=min(roomNum,mp[i][j])
    print(f'#{num}',roomNum,maxi)
    