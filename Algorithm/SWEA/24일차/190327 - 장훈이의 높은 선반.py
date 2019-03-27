import sys
sys.stdin = open('input.txt','r')

def solution(n):
    global mini
    for i in range(1<<n):
        # 최소값은 b와 같은 수이므로 이것만 구하면 나간다.
        if mini==b:
            break
        total=0
        for j in range(n):
            if i & 1<<j:
                total+=inp[j]
                if mini<total:
                    break
        else:
            if mini>total and total>=b:
                mini=total

TC = int(input())
for num in range(1,TC+1):
    n,b = map(int,input().split())
    inp = list(map(int,input().split()))
    inp.sort(reverse=True)
    mini = 999999
    solution(n)
    print(f"#{num}",abs(b-mini))

# 최소, 최대가 명확하게 기준이 정해져 있다면 이를 이용해 추가 계산을 하지 않도록
# 자르는 것이 중요하다.