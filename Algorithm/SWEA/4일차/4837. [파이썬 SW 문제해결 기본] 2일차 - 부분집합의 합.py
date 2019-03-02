import sys
sys.stdin = open("input.txt","r")

arr = list(range(1,13))
array = []
parts = []

# 1부터 12까지의 모든 부분집합을 구함
for i in range(1<<12):
    for j in range(12):
        if i &(1<<j):
            array.append(arr[j])
    parts.append(array)
    array = []

T=int(input())

for i in range(T):
    count = 0
    n,k = map(int, input().split())
    # 부분집합의 길이(n)과 합(k)에 만족하는 부분집합을 count
    for j in parts :
        if len(j) == n and sum(j) ==k :
            count +=1

    print(f'#{i+1} {count}')


# 선생님 코드
TC = int(input())

for tc in range (1, TC+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1, 1 << 12):
        bitCnt = sum = 0
        for j in range(12):
            if i & (1 << j) :
                sum += (j + 1)
                bitCnt += 1
        if sum == K and bitCnt == N:
            cnt += 1

    print("#%d %d"%(tc, cnt))