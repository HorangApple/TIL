import sys
sys.stdin=open('input.txt','r')

dy = [0,0,-1,1]
dx = [1,-1,0,0]

dic = {(0,-1):0,(1,0):1,(0,1):2,(-1,0):3}
startDirec = {
    1:[[0,1],[1,0],[-1,0],[0,-1]],
    2:[[1,0],[-1,0]],
    3:[[0,1],[0,-1]],
    4:[[-1,0],[0,1]],
    5:[[1,0],[0,1]],
    6:[[1,0],[0,-1]],
    7:[[-1,0],[0,-1]]
    }

def block(y,x,direc,mode):
    if mode==2:
        gdy=[0,1,0,-1]
        gdx=[1,0,-1,0]
    elif mode==3:
        gdy=[0,-1,0,1]
        gdx=[-1,0,1,0]
    elif mode==4:
        gdy=[-1,0,0,1]
        gdx=[0,1,-1,0]
    elif mode==5:
        gdy=[1,-1,0,0]
        gdx=[0,0,-1,1]
    elif mode==6:
        gdy=[0,-1,1,0]
        gdx=[1,0,0,-1]
    elif mode==7:
        gdy=[0,0,-1,1]
        gdx=[1,-1,0,0]
    
    return [gdy[dic[direc[0],direc[1]]],gdx[dic[direc[0],direc[1]]]]

def solution(y,x,directions,time):
    que=[[y,x,directions,time]]
    while len(que)>0:
        y,x,directions,time=que.pop(0)
        if time==0:
            continue
        for go in directions:
            sy=y+go[0]
            sx=x+go[1]
            if -1<sy<n and -1<sx<m and mp[sy][sx]!=0 and [sy,sx] not in visited:
                if mp[sy][sx]!=1:
                    direct=[block(sy,sx,go,mp[sy][sx])]
                    if direct[0]==[-1*go[0],-1*go[1]]:
                        continue
                else:
                    direct=[[1,0],[0,1],[-1,0],[0,-1]]
                    
                visited.append([sy,sx])
                que.append([sy,sx,direct,time-1])

TC = int(input())
for num in range(1,TC+1):
    n,m,r,c,l = map(int,input().split())
    mp=[list(map(int,input().split())) for _ in range(n)]
    visited=[[r,c]]
    solution(r,c,startDirec[mp[r][c]],l-1)
    print(f'#{num}',len(visited))
    