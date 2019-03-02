import sys
sys.stdin = open("input.txt","r")

TC=int(input())
# 4방향으로 갈 길이 있는지 탐색, 갈 수 있는 길의 수를 반환함
def search(y,x):
    count=0
    if y+1<length and inp[y+1][x]==0:
        count+=1
    if y-1>-1 and inp[y-1][x]==0:
        count+=1
    if x+1<length and inp[y][x+1]==0:
        count+=1
    if y-1>-1 and inp[y][x-1]==0:
        count+=1
    return count
def go(start):
    re=[]
    fobi=[1,-1]
    y=start[0]
    x=start[1]
    stack=[]
    direc=0
    # 4방향으로 갈 길이 있는지 탐색, 갈 수 있는 길의 수만큼 stack에 저장
    for _ in range(search(y,x)):
        stack.append([y,x])
    while True:
        # 위로 움직임
        if y+1<length and (inp[y+1][x] not in fobi) or (y+1<length and inp[y+1][x]==0):
            while y+1<length and inp[y+1][x]!=1:
                # 지나간 길은 -1로 초기화
                inp[y][x]=-1
                y+=1
                # 목적지 발견하면 1을 리턴
                if inp[y][x]==3:
                    return 1
                # 진행하다가 만약 좌,우에 길이 있다면 동일하게 stack에 저장
                if x+1<length and inp[y][x+1]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1 # 아직 둘러 볼 곳이 있음을 나타냄
                elif x-1>0 and inp[y][x-1]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
        # 아래로 움직임            
        elif y-1>-1 and (inp[y-1][x] not in fobi) or (y-1>-1 and inp[y-1][x]==0):
            while y-1>-1 and inp[y-1][x]!=1:
                inp[y][x]=-1
                y-=1
                if inp[y][x]==3:
                    return 1
                if x+1<length and inp[y][x+1]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
                elif x-1>0 and inp[y][x-1]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
        # 오른쪽으로 움직임
        elif x+1<length and (inp[y][x+1] not in fobi) or (x+1<length and inp[y][x+1]==0):
            while x+1<length and inp[y][x+1]!=1:
                inp[y][x]=-1
                x+=1
                if inp[y][x]==3:
                    return 1
                if y+1<length and inp[y+1][x]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
                elif y-1>0 and inp[y-1][x]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
        # 왼쪽으로 움직임
        elif x-1>-1 and (inp[y][x-1] not in fobi) or (x-1>-1 and inp[y][x-1]==0):
            while x-1>-1 and inp[y][x-1]!=1:
                inp[y][x]=-1
                x-=1
                if inp[y][x]==3:
                    return 1
                if y+1<length and inp[y+1][x]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
                elif y-1>0 and inp[y-1][x]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
        if len(stack)==0:
            return 0
        # 다 찾아 봤다면 이전 위치로 돌아감
        elif direc!=1:
            re=stack.pop()
            y=re[0]
            x=re[1]
        # 한 방향으로 탐색이 완료되면 0으로 초기화
        else:
            direc=0

for num in range(1,TC+1):
    length=int(input())
    inp=[[int(i) for i in input()]for _ in range(length)]
    start=[]
    
    for i in range(length):
        for j in range(length):
            if inp[i][j]==2:
                start=[i,j]
            if start==True:
                break
        if start==True:
                break
    print(f'#{num} {go(start)}')

# 00013
# 01110
# 20000
# 01111
# 00000
# 이 테스트 케이스에서 되질 않았다 이를 해결했더니 통과함

# 선생님 풀이
import sys
sys.stdin = open("input.txt", "r")

def check(x, y):
    if x < 0 or x > N-1 : return False
    if y < 0 or y > N-1 : return False
    if maze[x][y] == 1  : return False
    return True


def DFS(x, y):
    stack = [0] * (N*N)
    top = -1

    top += 1 ; stack[top] = x, y

    while top != -1:
        x, y = stack[top] ; top -= 1

        if maze[x][y] == 3 : return 1
        if maze[x][y] != 1 :
            maze[x][y] = 1
            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i]
                if check(newX, newY) :
                    top += 1 ; stack[top] = newX, newY
    return 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2 :
                sX = i
                sY = j

    print('#%d'%tc, DFS(sX, sY))



# 선생님 풀이
# 재귀ver.
import sys
sys.stdin = open("input.txt", "r")

def DFSr(x, y):
    global found
    if not 0 <= x < N or not 0 <= y < N or found or maze[x][y] == 1 : return
    if maze[x][y] == 3 : found = 1; return

    maze[x][y] = 1
    DFSr(x, y+1)
    DFSr(x, y-1)
    DFSr(x+1, y)
    DFSr(x-1, y)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2 :
                sX = i
                sY = j

    found = 0
    DFSr(sX, sY)
    print('#%d'%tc, found)