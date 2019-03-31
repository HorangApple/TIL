import sys
sys.stdin = open('p1.txt','r')

dx = [2,2,3,3,-2,-2,-3,-3]
dy = [3,-3,2,-2,3,-3,2,-2]

def bfs(v,cnt):
    one=[]
    for i in range(8):
        sx = v[0]+dx[i]
        sy = v[1]+dy[i]
        if -1<sx<n and -1<sy<n and [sx,sy] not in visited:
            if [sx,sy]==[tx,ty]:
                result.append(cnt)
                return
            one.append([sx,sy])
            visited.append([sx,sy])
    cnt+=1
    for _ in range(len(one)):
        v=one.pop(0)
        bfs(v,cnt)

T = int(input())
for num in range(1,T+1):
    n = int(input())
    x,y,tx,ty = map(int,input().split())
    cnt=1
    visited=[[x,y]]
    result = []
    bfs([x,y],cnt)
    print('#{}'.format(num),min(result))
