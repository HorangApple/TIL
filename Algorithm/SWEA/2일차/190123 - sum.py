import sys
sys.stdin = open("input.txt","r")

TC=10

for i in range(TC):
    inp=[]
    maxi=0
    sums=0
    length=100
    TC1=int(input())
    for j in range(length):
        inp.append(list(map(int, input().split())))
    # 왼->오 아래 대각선
    for j in range(length):
        sums += inp[j][j]
    if maxi<sums : maxi=sums
    sums=0
    # 오->왼 아래 대각선
    for j in range(length):
        sums += inp[j][length-1-j]
    if maxi<sums : maxi=sums
    sums=0
    # 행의 합
    for j in range(length):
        for k in range(length):
            sums+=inp[j][k]
        if maxi<sums : maxi=sums
        sums=0
        
    # 열의 합
    for k in range(length):
        for j in range(length):
            sums+=inp[j][k]
        if maxi<sums : maxi=sums
        sums=0

    print(f'#{TC1} {maxi}')