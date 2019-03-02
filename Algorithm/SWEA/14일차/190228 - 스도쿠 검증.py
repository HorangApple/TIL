import sys
sys.stdin = open("input.txt","r")

def detect():
    # 가로
    for i in mp:
        # 0부터 9까지의 합인 45가 아니면 리턴
        if sum(i)!=45:
            return 0
    # 세로
    for i in range(9):
        total=0
        for j in range(9):
            total+=mp[j][i]
        # 0부터 9까지의 합인 45가 아니면 리턴
        if total!=45:
            return 0
    # 3X3
    for j in range(3):
        total1=0
        total2=0
        total3=0
        # 한 번에 세 군데를 검증    
        for i in mp[3*j:3*(j+1)]:
            total1+=sum(i[0:3])
            total2+=sum(i[3:6])
            total3+=sum(i[6:9])
        if total1 !=45 or total2 !=45 or total3 !=45 :
            return 0
    return 1 

TC=int(input())
for num in range(1,TC+1):
    mp=[list(map(int, input().split())) for _ in range(9)]
    print(f'#{num} {detect()}')
            