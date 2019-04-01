import sys
sys.stdin = open('input.txt','r')

import collections
def cal(v,p):
    if p==0:
        v+=1
    elif p==1:
        v-=1
    elif p==2:
        v*=2
    else:
        v-=10
    return v

def bfs(n):
    global mini
    que=collections.deque()
    que.append([n,1])
    while len(que)>0:
        a=que.popleft()
        v=a[0]
        cnt=a[1]
        for i in range(4):
            value = cal(v,i)
            if value>1000000 or value<1:
                continue
            if value==m:
                mini=min(mini,cnt)
                return
            if not visited[value]:
                visited[value]=True
                que.append([value,cnt+1])


T=int(input())
for num in range(1,1+T):
    n,m = map(int,input().split())
    visited=[False]*1000001
    mini=99999999999999999999
    bfs(n)
    print(f'#{num}',mini)