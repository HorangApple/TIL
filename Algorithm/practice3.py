import sys
sys.stdin = open("input.txt","r")

TC=10

for i in range(TC):
    inp=[]
    result=[]
    sums=0
    length=100
    TC1=int(input())
    for j in range(length):
        inp.append(list(map(int, input().split())))

    for j in range(length):
        sums += inp[j][j]
    result.append(sums)
    sums=0
    for j in range(length):
        sums += inp[j][length-1-j]
    result.append(sums)
    sums=0
    for j in range(length):
        for k in range(length):
            sums+=inp[j][k]
            result.append(sums)
        sums=0
    for k in range(length):
        for j in range(length):
            sums+=inp[j][k]
            result.append(sums)
        sums=0

    print(f'#{TC1} {max(result)}')