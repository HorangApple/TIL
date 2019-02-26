import sys
sys.stdin = open("input.txt","r")

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def startSearch(n):
    for i in range(n):
        for j in range(n):
            if inp[i][j]=='2':
                return [i,j]
def solution(n,start):
    deep=-1
    x,y=0,0
    que=[[start[0],start[1],deep]]
    while True:
        if len(que)==0:
            return 0
        y,x,deep=que.pop(0)
        if inp[y][x]=='3':
            return deep
        deep+=1
        inp[y][x]='-1'
        for i in range(4):
            x_=x+dx[i]
            y_=y+dy[i]
            if 0<=x_<n and 0<=y_<n and (inp[y_][x_]=='0' or inp[y_][x_]=='3'):
                que.append([y_,x_,deep])

TC=int(input())
for num in range(1,TC+1):
    n=int(input())
    inp=[list(input()) for _ in range(n)]
    start=startSearch(n)
    print(f'#{num} {solution(n,start)}')