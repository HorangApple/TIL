import sys
sys.stdin = open("input.txt","r")

def solution(s,g,v):
    start=s
    deep=0
    que=[[start,deep]]
    visited=[False]*(v+1)
    while True:
        if len(que)==0:
            return 0
        start,deep=que.pop(0)
        if start==g:
            return deep
        for i in range(1,v+1):
            if road[start][i]>0 and not visited[i]:
                que.append([i,deep+1])
        visited[start]=True

TC=int(input())
for num in range(1,TC+1):
    v,e=map(int,input().split())
    road=[[0]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        line=list(map(int,input().split()))
        road[line[0]][line[1]]=line[1]
        road[line[1]][line[0]]=line[0]
    s,g=map(int,input().split())
    print(road)
    print(f'#{num} {solution(s,g,v)}')