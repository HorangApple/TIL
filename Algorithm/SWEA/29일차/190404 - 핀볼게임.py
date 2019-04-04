import sys
sys.stdin = open('input.txt','r')

dy = [0,-1,0,1]
dx = [1,0,-1,0]

dic = {(0,-1):0,(1,0):1,(0,1):2,(-1,0):3}

def block(y,x,direc,mode):
    if mode==1:
        gdy=[-1,0,0,1]
        gdx=[0,1,-1,0]
    elif mode==2:
        gdy=[1,-1,0,0]
        gdx=[0,0,-1,1]
    elif mode==3:
        gdy=[0,-1,1,0]
        gdx=[1,0,0,-1]
    elif mode==4:
        gdy=[0,0,-1,1]
        gdx=[1,-1,0,0]
    elif mode==5:
        gdy=[0,-1,0,1]
        gdx=[1,0,-1,0]
    
    return [gdy[dic[direc[0],direc[1]]],gdx[dic[direc[0],direc[1]]]]

def solution(stY,stX):
    global maxi
    for i in range(4):
        direc=[dy[i],dx[i]]
        end=[stY,stX]
        score=0
        movY,movX=-1,-1
        while end!=[movY,movX]:
            movY=stY+direc[0]
            movX=stX+direc[1]
            if -1<movY<n and -1<movX<n:
                if mp[movY][movX] != 0 and mp[movY][movX]!=-1:
                    if 1<=mp[movY][movX]<=5:
                        score+=1
                        direc=block(movY,movX,direc,mp[movY][movX])
                        stY,stX=movY,movX
                    else:
                        for j in hole[mp[movY][movX]-6]:
                            if [movY,movX]!=j:
                                stY,stX=j
                                movY,movX=stY,stX
                                break
                elif mp[movY][movX] == -1:
                    break
                else:
                    stY,stX=movY,movX
            else:
                score+=1
                direc=[-1*direc[0],-1*direc[1]]
                stY,stX=movY,movX
        maxi=max(maxi,score)

TC = int(input())
for num in range(1,TC+1):
    n= int(input())
    mp = [list(map(int,input().split())) for _ in range(n)]
    hole=[[] for _ in range(5)] # idx=웜홀 번호-6
    maxi=0
    for i in range(n):
        for j in range(n):
            if mp[i][j]>5:
                hole[mp[i][j]-6]+=[[i,j]]
    for i in range(n):
        for j in range(n):
            if mp[i][j]==0:
                solution(i,j)
    print(f'#{num}',maxi)