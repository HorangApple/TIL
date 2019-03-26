import sys
sys.stdin = open("input.txt","r")

n = int(input())
table = [list(map(int,input().split())) for _ in range(n)]+[[0,0]]

table.sort(key=lambda element: (element[1],element[0]))
j = 1
cnt=1
for i in range(2,n+1):
    if table[i][0] >= table[j][1]:
        cnt+=1
        j = i

print(cnt)

# https://twpower.github.io/118-sort-list-elements-by-using-key