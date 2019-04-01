import sys
sys.stdin=open("input.txt","r")

# https://www.acmicpc.net/problem/1325
def bfs(start):
    global maxCnt,cnt,result
    que = [0]*(n+1)
    front=-1
    back=0
    que[back]=start
    back+=1
    while front<=back:
        front+=1
        v=que[front]
        cnt += 1
        visited[v]=True
        for i in mp[v]:
            if i>0 and not visited[i]:
                que[back]=i
                back+=1
    if maxCnt<cnt:
        maxCnt=cnt
        result = []
        result.append(start)
    elif maxCnt==cnt:
        result.append(start)

n,m=map(int,input().split())
mp=[[] for _ in range(n+1)]
for _ in range(m):
    inp=list(map(int,input().split()))
    mp[inp[1]]+=[inp[0]]
maxCnt=0
result=[]
for i in range(1,n+1):
    cnt = 0
    visited = [False]*(n+1)
    bfs(i)
for i in result:
    print(i,end=" ")
print()
