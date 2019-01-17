import sys
sys.stdin = open("input.txt","r")

def my_max(lists, n):
    for i in range(n-1, 0, -1):
        for j in range(0,i):
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
    return lists[-1]

def my_min(lists,n):
    for i in range(0, n-1):
        for j in range(i, 0, -1):
            if lists[j] < lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
    return lists[0]    
        

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    lists = list(map(int, input().split()))
    result = my_max(lists, n)-my_min(lists, n)

    print(f'#{test_case} {result}')