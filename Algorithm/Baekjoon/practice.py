import sys
sys.stdin = open("input.txt","r")

for j in range(1, 11):
    case = int(input())
    lists = list(map(int, input().split()))
    count = 0
    for i in range(2, len(lists)-2) :
        a = lists[i] - lists[i-1]
        b = lists[i] - lists[i-2]
        c = lists[i] - lists[i+1]
        d = lists[i] - lists[i+2]
        if a < 0 or b < 0 or c < 0 or d < 0:
            continue
        else :
            mini1 = b if a>b else a
            mini2 = d if c>d else c
            mini = mini2 if mini1 > mini2 else mini1
            count += mini
    print(f'#{j} {count}')