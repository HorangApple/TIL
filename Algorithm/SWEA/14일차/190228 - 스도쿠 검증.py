import sys
sys.stdin = open("input.txt","r")

def detect():
    for i in mp:
        if sum(i)!=45:
            return 0
    for i in range(9):
        total=0
        for j in range(9):
            total+=mp[j][i]
        if total!=45:
            return 0
    for j in range(3):
        total1=0
        total2=0
        total3=0    
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
            