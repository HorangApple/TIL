"""

"""

# 내 풀이
import sys
sys.stdin = open("ViewInput.txt","r")

for j in range(1, 11):
    case = int(input())
    lists = list(map(int, input().split()))
    count = 0
    # 강 이후 시작되는 건물(index 2부터)을 기준으로 양쪽 방향으로 
    # 1칸, 2칸 떨어진 건물과 비교
    for i in range(2, len(lists)-2) :
        a = lists[i] - lists[i-1]
        b = lists[i] - lists[i-2]
        c = lists[i] - lists[i+1]
        d = lists[i] - lists[i+2]
        # 차이로 비교해서 현재의 건물이 주변건물보다 작은 경우 다른 건물로 넘어감
        if a < 0 or b < 0 or c < 0 or d < 0:
            continue
        # 현재의 건물이 크다면 a,b,c,d가 나타내는 
        # 건물 높이간의 차이가 적었던 건물 (조망권이 확보된 건물)을 선택하고 count에 누적
        else :
            mini1 = b if a>b else a
            mini2 = d if c>d else c
            mini = mini2 if mini1 > mini2 else mini1
            count += mini
    print(f'#{j} {count}')

# 선생님 풀이
import sys
sys.stdin = open("ViewInput.txt","r")

def getMax (idx) :
    tmax = heights[idx-2]
    if tmax < heights[idx-1]: tmax = heights[idx-1]
    if tmax < heights[idx+1]: tmax = heights[idx+1]
    if tmax < heights[idx+2]: tmax = heights[idx+2]
    return tmax

TC = 10
for tc in range(1, TC+1):
    N = int(input())
    heights = list(map(int, input().split()))
    view = 0

    for i in range(2, N-2) :
        side = getMax(i)
        if side < heights[i] :
            view += heights[i] - side
    print("#%d %d"%(tc, view))