import sys
sys.stdin = open("input.txt","r")

def solution(n):
    result = []
    for i in range(1<<n):
        part= []
        for j in range(n):
            if i&(1<<j):
                part.append(j)
        if len(part) == n//2:
            result.append(part)
    return result

n = int(input())
mp = [list(map(int, input().split())) for _ in range(n)]
arr = solution(n)

mini = 999999999999
half = len(arr)//2
for i, j in zip(arr[:half],arr[-1:-half-1:-1]):
    total1 = 0
    total2 = 0
    k=0
    while k<len(i):
        for q in i[k+1:]:
            total1=total1+mp[i[k]][q]+mp[q][i[k]]
        k+=1
    k=0
    while k<len(j):
        for q in j[k+1:]:
            total2=total2+mp[j[k]][q]+mp[q][j[k]]
        k+=1

    val = abs(total1-total2)
    if val<mini:
        mini=val

print(mini)

# 단순 덧셈에 메모이제이션을 사용하면 오히려 느리다.
# [[0, 1], [0, 2], [1, 2], [0, 3], [1, 3], [2, 3]] 0과 -1, 1과 -2와 같이 두 개씩 짝지어진다.