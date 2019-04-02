import sys
sys.stdin = open('input.txt','r')
# https://wkdtjsgur100.github.io/python-dijkstra/
def solution(v):
    global total,n
    visited=[False]*(n+1)
    d = [0xffffff]*(n+1)
    d[v] = 0
    while True:
        m = 0xffffff
        idx = 0 
        for i in range(n+1):
            if not visited[i] and m>d[i]:
                m=d[i]
                idx=i
        
        if m == 0xffffff:
            break

        visited[idx]=True
       
        for i in range(n+1):
            if visited[i]:continue
            via = d[idx]+a[idx][i]
            if d[i]>via:
                d[i]=via
    return d
        

TC = int(input())
for num in range(1,TC+1):
    n,e= map(int,input().split())
    a = [[0xffffff]*(n+1) for _ in range(n+1)]
    for i in range(e):
        y,x,v=map(int,input().split())
        a[y][x]=v
    
    print(f'#{num}',solution(0)[-1])