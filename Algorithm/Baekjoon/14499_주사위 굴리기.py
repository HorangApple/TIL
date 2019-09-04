import sys
sys.stdin = open("pratice1.txt", "r")

n,m,y,x,order_cnt = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]

# [0,1,2,3] 동서북남
orders = list(map(lambda x: int(x)-1, input().split()))

dy = [0,0,-1,1]
dx = [1,-1,0,0]

dice = [[0,0,0] for _ in range(3)]

# 시작은 [1,1]
def diceGo(order):
    if order == 0:
        temp = dice[1][2]
        for idx in [1,0]:
            dice[1][idx+1] = dice[1][idx]
        dice[1][0] = dice[0][0]
        dice[0][0] = temp
    elif order == 1:
        temp = dice[1][0]
        for idx in range(1,3):
            dice[1][idx-1] = dice[1][idx]
        dice[1][2] = dice[0][0]
        dice[0][0] = temp
    elif order == 2:
        temp = dice[0][1]
        for idx in range(1,3):
            dice[idx-1][1] = dice[idx][1]
        dice[2][1] = dice[0][0]
        dice[0][0] = temp
    else :
        temp = dice[2][1]
        for idx in [1,0]:
            dice[idx+1][1] = dice[idx][1]
        dice[0][1] = dice[0][0]
        dice[0][0] = temp
    print(dice[1][1])
    # print('order:',order)
    # for i in dice:
    #     print(i)


for order in orders:
    y = y+dy[order]
    x = x+dx[order]

    limit = 0<= y <n and 0<= x <m
    if limit :
        diceGo(order)
        if mp[y][x] == 0:
            mp[y][x] = dice[0][0]
        else :
            dice[0][0] = mp[y][x]
            mp[y][x] = 0
    else:
        y = y-dy[order]
        x = x-dx[order]
