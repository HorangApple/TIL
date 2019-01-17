import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1, T+1):
    k, n, m = list(map(int, input().split()))
    mSet = list(map(int, input().split()))
    count = 0
    location = 0
    maxCharger = 0
    for i in range(m) :
        if location + k >= n :
            break # 도착
        for j in range(i,m):        
            if location + k >= mSet[j] :
                maxCharger = mSet[j] 
            else :
                break
        if location != maxCharger :
            location = maxCharger
            count +=1
            if location + k >= n :
                break
    else :
        count = 0

    print(f'#{test_case} {count}')

"""
변수를 임의의 상수로 설정하면 오류가 나는 경우도 있으니 주의해야한다.
"""