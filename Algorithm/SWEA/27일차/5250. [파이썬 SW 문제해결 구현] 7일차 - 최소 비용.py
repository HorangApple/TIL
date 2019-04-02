import sys
sys.stdin = open('input.txt','r')

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def solution(v):
    global mini
    que=[v]
    while len(que)>0:
        v = que.pop(0)
        for i in range(4):
            sy = v[0]+dy[i]
            sx = v[1]+dx[i]
            if -1<sy<n and -1<sx<n :
                gap=mp[sy][sx]-mp[v[0]][v[1]]
                if gap>=0:
                    val=visited[v[0]][v[1]]+1+gap
                else:
                    val=visited[v[0]][v[1]]+1
                if visited[sy][sx]==0xfffff or visited[sy][sx]>val:
                    visited[sy][sx]=val
                    que.append([sy,sx])

TC = int(input())
for num in range(1,TC+1):
    n = int(input())
    mp = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0xfffff]*n for _ in range(n)]
    visited[0][0] = 0
    solution([0,0])
    print(f'#{num}',visited[n-1][n-1])

# 같은 크기의 리스트를 하나 더 만들어서 그걸 이용해 값을 계산하고 풀어나간다.

'''
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def solution(v):
    global total
    d = [[0x999999]*n for _ in range(n)]
    d[0][0] = mp[0][0]
    d[0][1] = abs(mp[0][1]-mp[0][0])
    d[1][0] = abs(mp[1][0]-mp[0][0])
    visited=[[False]*n for _ in range(n)]
    while v != [n-1,n-1]:
        visited[v[0]][v[1]]=True
        mini=99999
        for i in range(4):
            sy = v[0]+dy[i]
            sx = v[1]+dx[i]
            if -1<sy<n and -1<sx<n and not visited[sy][sx]:
                gap = d[sy][sx]
                if mini>gap:
                    if gap>0:
                        mini=gap
                    else:
                        mini=0
                    save = [sy,sx]

        v=save
        total+=mini+1
        for i in range(4):
            sy = v[0]+dy[i]
            sx = v[1]+dx[i]
            if -1<sy<n and -1<sx<n and not visited[sy][sx]:
                gap = abs(mp[sy][sx]-mp[v[0]][v[1]])
                d[sy][sx]=min(gap,total)

        for i in d:
            print(i)
        print()
'''
'''
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def solution(v):
    global total,n
    visited=[[False]*n for _ in range(n)]
    d = [[0xffffff]*n for _ in range(n)]
    d[v][v] = 0
    while True:
        m = 0xffffff
        idxX = 0
        idxY = 0
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and m>=d[i][j]:
                    m=d[i][j]
                    idxY=i
                    idxX=j
        total+=d[idxY][idxX]
        print(d[idxY][idxX])
        visited[idxY][idxX]=True
       
        for i in range(4):
            sy = idxY+dy[i]
            sx = idxX+dx[i]
            if -1<sy<n and -1<sx<n and not visited[sy][sx]:
                gap = abs(mp[idxY][idxX]-mp[sy][sx])
                via = d[idxY][idxX]+gap
                if d[sy][sx]>via:
                    d[sy][sx]=via
                if [sy,sx] == [n-1,n-1]:
                    total+=gap
                    return
        for i in d:
            print(i)
        print()
'''