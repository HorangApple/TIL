import sys
sys.stdin = open("input.txt","r")

def dfs(v):
    visited[v]=True
    print(v, end = " ")
    for w in inp[v]:
        if not visited[w]:
            dfs(w)

n,m = map(int, input().split())
inp = [[] for _ in range(m)]
for _ in range(m):
    u,v = map(int,input().split())
    inp[u].append(v)
    inp[v].append(u)
visited=[False]*(n+1)
stack=[1]

dfs(1)