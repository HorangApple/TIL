import sys
sys.stdin = open("input.txt","r")

def search(v):
    for i in road[v]:
        if i>0 and str(i) not in dfsVisited:
            return i
def dfs(n):
    dfsVisited.append(str(n))
    while n:
        w=search(n)
        if w:
            stack.append(n)
        while w:
            dfsVisited.append(str(w))
            stack.append(n)
            n=w
            w=search(n)
        n=stack.pop()

def bfs(v):
    que.append(v)
    while que:
        t=que.pop(0)
        if str(t) not in bfsVisited:
            bfsVisited.append(str(t))
        for i in road[t]:
            if i>0 and str(i) not in bfsVisited:
                que.append(i)

n,m,v=map(int,input().split())
que=[]
stack=[0]
dfsVisited=[]
bfsVisited=[]
road=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    oneEdge=list(map(int,input().split()))
    road[oneEdge[0]][oneEdge[1]]=oneEdge[1]
    road[oneEdge[1]][oneEdge[0]]=oneEdge[0]

dfs(v)
bfs(v)
print(" ".join(dfsVisited))
print(" ".join(bfsVisited))

# dfs와 bfs 학습 부족