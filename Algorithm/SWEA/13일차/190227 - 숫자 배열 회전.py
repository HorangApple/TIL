import sys
sys.stdin = open("input.txt","r")

TC=int(input())
for num in range(1,TC+1):
    n=int(input())
    mp=[list(input().split()) for _ in range(n)]
    print(f'#{num}')
    for i in range(n):
        oneline1=""
        oneline2=""
        oneline3=""
        for j in range(n):
            oneline1+=mp[n-1-j][i]
            oneline2+=mp[n-1-i][n-1-j]
            oneline3+=mp[j][n-1-i]
        print(f'{oneline1} {oneline2} {oneline3}')