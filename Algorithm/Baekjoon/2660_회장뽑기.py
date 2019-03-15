import sys
sys.stdin=open('input.txt','r')

def bfs():
    cnt=-1
    depth=que[:]
    while que:
        v=que.pop(0)
        visited.append(v)
        for i in range(n+1):
            w=mp[v][i]
            if w>0 and (w not in visited) and (w not in que):
                que.append(w)
        depth.pop(0)
        if depth==[]:
            depth=que[:]
            cnt+=1
    return cnt

n=int(input())
mp=[[0]*(n+1) for _ in range(n+1)]
while True:
    inp=list(map(int,input().split()))
    if inp==[-1,-1]:
        break
    mp[inp[0]][inp[1]]=inp[1]
    mp[inp[1]][inp[0]] = inp[0]
result=[0]*(n+1)
for i in range(1,n+1):
    que=[]
    visited = []
    que.append(i)
    depth = que[:]
    cnt=bfs()
    result[i]=cnt

idx=1
mini=1000
minidx=[]
for i in result[1:]:
    if i<mini:
        mini=i
        minidx=[]
        minidx.append(idx)
    elif i==mini:
        minidx.append(idx)
    idx+=1
print(mini,len(minidx))
for i in minidx:
    print(i,end=" ")