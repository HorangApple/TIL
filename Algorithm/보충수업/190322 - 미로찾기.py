import sys
sys.stdin = open("input.txt", "r")

dx=[1,-1]
dy=[0,0]

def dfs(v):
    x=v[1]
    y=v[0]
    if y-1>0 and mp[y-1][x]=='2':
        return True
    elif y>=100:
        return False

    visited.append([y,x])
    for i in range(2):
        sx=x+dx[i]
        sy=y+dy[i]
        if -1<sx<100 and -1<sy<100 and mp[sy][sx]=='1' and [sy,sx] not in visited:
            return dfs([sy,sx])

    return dfs([y+1,x])

for num in range(1,11):
    n = input()
    mp = [input().split() for _ in range(100)]
    for x in range(100):
        if mp[0][x]=='1':
            visited=[]
            result=dfs([0,x])
            if result:
                print(f'#{num}',x)
                break
## 선생님 코드
# def dfs(x,y):
#     if x==0:
#         ans = y
#         return
#     visit[x][y]=True
#     if y-1>=0 and arr[x][y-1] and not visit[x][y-1]:
#         dfs(x,y-1)
#     elif y+1<100 and arr[x][y+1] and not visit[x][y+1]:
#         dfs(x,y-1)
#     else:
#         dfs(x-1,y)

# for tc in range(1,11):
#     case = int(input())
#     arr = [list(map(int,input().split())) for _ in range(100)]
#     sx=sy=0
#     for i in range(100):
#         if arr[99][i]==2:
#             sx,sy = 99, i
#             break
#     visit = [[False] * 100 for _ in range(100)]
#     print(f"#{num}",dfs(sx,sy))

# 5643, 키 문제 재귀로만 풀어봐라