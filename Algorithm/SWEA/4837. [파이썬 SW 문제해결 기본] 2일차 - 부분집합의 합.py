import sys
sys.stdin = open("input.txt","r")

arr = list(range(1,13))
array = []
parts = []

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
    for j in parts :
        if len(j) == n and sum(j) ==k :
            count +=1

    print(f'#{i+1} {count}')