import sys
sys.stdin = open('test.txt', 'r')

n,m = map(int,input().split())
r,c,d = map(int,input().split())

mp = [list(map(int,input().split())) for _ in range(n)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def test(y,x,d):
    print(y,x,d)
    for i in mp:
        print(i)
    print()

def spin(y,x,d):
    goback = False
    mp[y][x] = 2
    # test(y, x, d)
    for i in range(1,5):
        cd = (d-i)%4
        cy = y + dy[cd]
        cx = x + dx[cd]
        limit = 0<= cy <n and 0<= cx < m
        if limit:
            if mp[cy][cx] == 0 :
                return spin(cy, cx, cd)
            elif i == 2 and mp[cy][cx] != 1:
                goback = True
    else:
        if goback :
            cy = y + dy[d - 2]
            cx = x + dx[d - 2]
            return spin(cy, cx, d)
        else :
            return

def cnt():
    total = 0
    for i in range(n):
        for j in range(m):
            if mp[i][j] == 2:
                total += 1
    return total

spin(r,c,d)
print(cnt())