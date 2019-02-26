import sys
sys.stdin = open("input.txt","r")

# 4방향
dx=[0,1,0,-1]
dy=[1,0,-1,0]

# 시작 지점 물색
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
        # 목적지를 못찾으면 0을 리턴
        if len(que)==0:
            return 0
        # 다음 갈 곳 팦바팦파팦ㅍ
        y,x,deep=que.pop(0)
        # 목적지에 도착하면 깊이를 리턴
        if inp[y][x]=='3':
            return deep
        deep+=1
        # 이미 지나간 곳은 다시 안가게 -1로 표시
        inp[y][x]='-1'
        # 4방향으로 갈 길이 있는지 물색 후 추가
        for i in range(4):
            x_=x+dx[i]
            y_=y+dy[i]
            # 맵 안에 있고 값이 0이거나 3인 지점만 거른다
            if 0<=x_<n and 0<=y_<n and (inp[y_][x_]=='0' or inp[y_][x_]=='3'):
                que.append([y_,x_,deep])

TC=int(input())
for num in range(1,TC+1):
    n=int(input())
    inp=[list(input()) for _ in range(n)]
    start=startSearch(n)
    print(f'#{num} {solution(n,start)}')