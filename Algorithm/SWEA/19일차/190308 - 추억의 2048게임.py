import sys
sys.stdin=open('input.txt','r')

dy=[1,0,-1,0]
dx=[0,1,0,-1]
def solution(d):
    diration={'down':2,'right':3,'up':0,'left':1}
    for k in range(n):
        for i in range(n):
            for j in range(n-i-1):
                if diration[d] == 0:
                    if mp[j][k]==0:
                        mp[j][k],mp[j+1][k]=mp[j+1][k],mp[j][k]
                elif diration[d] ==2:
                    if mp[(n-1)-j][k] == 0:
                        mp[(n-1)-j][k], mp[(n-1)-j - 1][k] = mp[(n-1)-j - 1][k], mp[(n-1)-j][k]
                elif diration[d] == 1:
                    if mp[k][j]==0:
                        mp[k][j],mp[k][j+1]=mp[k][j+1],mp[k][j]
                elif diration[d] == 3:
                    if mp[k][(n-1)-j]==0:
                        mp[k][(n-1)-j],mp[k][(n-1)-j-1]=mp[k][(n-1)-j-1],mp[k][(n-1)-j]
    for i in range(n):
        for j in range(n):
            if diration[d]==0:
                y,x=j+dy[diration[d]],i+dx[diration[d]]
                if -1<y<n and -1<x<n and mp[y][x]==mp[j][i]:
                    mp[j][i]+=mp[y][x]
                    mp[y][x]=0
            elif diration[d]==2:
                y,x=(n-1)-j+dy[diration[d]],i+dx[diration[d]]
                if -1<y<n and -1<x<n and mp[y][x]==mp[(n-1)-j][i]:
                    mp[(n-1)-j][i]+=mp[y][x]
                    mp[y][x]=0
            elif diration[d]==1:
                y,x=i+dy[diration[d]],j+dx[diration[d]]
                if -1<y<n and -1<x<n and mp[y][x]==mp[i][j]:
                    mp[i][j]+=mp[y][x]
                    mp[y][x]=0
            elif diration[d]==3:
                y,x=i+dy[diration[d]],(n-1)-j+dx[diration[d]]
                if -1<y<n and -1<x<n and mp[y][x]==mp[i][(n-1)-j]:
                    mp[i][(n - 1) - j]+=mp[y][x]
                    mp[y][x]=0
    for k in range(n):
        for i in range(n):
            for j in range(n-i-1):
                if diration[d] == 0:
                    if mp[j][k]==0:
                        mp[j][k],mp[j+1][k]=mp[j+1][k],mp[j][k]
                elif diration[d] ==2:
                    if mp[(n-1)-j][k] == 0:
                        mp[(n-1)-j][k], mp[(n-1)-j - 1][k] = mp[(n-1)-j - 1][k], mp[(n-1)-j][k]
                elif diration[d] == 1:
                    if mp[k][j]==0:
                        mp[k][j],mp[k][j+1]=mp[k][j+1],mp[k][j]
                elif diration[d] == 3:
                    if mp[k][(n-1)-j]==0:
                        mp[k][(n-1)-j],mp[k][(n-1)-j-1]=mp[k][(n-1)-j-1],mp[k][(n-1)-j]

TC=int(input())
for num in range(1,TC+1):
    n,diration=input().split()
    n=int(n)
    mp=[list(map(int,input().split())) for _ in range(n)]
    solution(diration)
    print("#{}".format(num))
    for i in mp:
        for j in i:
            print("{}".format(j),end=" ")
        print()

