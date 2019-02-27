import sys
sys.stdin = open("input.txt","r")

def solution(s,g,v):
    start=s
    deep=0
    que=[[start,deep]]
    visited=[False]*(v+1)
    while True:
        # 목적지를 찾지 못하면 out
        if len(que)==0:
            return 0
        # 다음 목적지 팝팝팝팝
        start,deep=que.pop(0)
        # 목적지에 도착하면 깊이를 리턴
        if start==g:
            return deep
        # 다음 목적지 물색 후 큐에 추가
        for i in range(1,v+1):
            if road[start][i]>0 and not visited[i]:
                que.append([i,deep+1])
        # 현재 들른 노드에 방문했다고 표시
        visited[start]=True

TC=int(input())
for num in range(1,TC+1):
    v,e=map(int,input().split())
    road=[[0]*(v+1) for _ in range(v+1)]
    # 무방향이니 양방향으로 인접행렬 제작
    for _ in range(e):
        line=list(map(int,input().split()))
        road[line[0]][line[1]]=line[1]
        road[line[1]][line[0]]=line[0]
    s,g=map(int,input().split())
    
    print(f'#{num} {solution(s,g,v)}')