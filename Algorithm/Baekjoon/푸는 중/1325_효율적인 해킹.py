import sys
sys.stdin=open("input.txt","r")

def search(start):
    global cnt
    for i in mp[start]:
        if i>0 and i not in visited:
            que.append(i)

def bfs(start):
    global maxCnt
    global cnt
    que.append(start)
    while que:
        v=que.pop(0)
        cnt += 1
        visited.append(v)
        search(v)

    if maxCnt<cnt:
        maxCnt=cnt
        result.clear()
        result.append(start)
    elif maxCnt==cnt:
        result.append(start)

n,m=map(int,input().split())
mp=[[0,[]]*(n+1) for _ in range(n+1)]
for _ in range(m):
    inp=list(map(int,input().split()))
    mp[inp[1]][inp[0]]=inp[0]
maxCnt=0
result=[]
for i in range(1,n+1):
    cnt = 0
    que = []
    visited = []
    bfs(i)
for i in result:
    print(i,end=" ")
print()
