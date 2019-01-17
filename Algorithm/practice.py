import sys
sys.stdin = open("input.txt","r")

TC = int(input())

for i in range(TC):
    K, N, M = list(map(int, input().split()))
    S = list(map(int, input().split()))

    # 모든 정류장
    stops = [0] * (N+1)
    # 버스스탑 채우기
    for stop in S:
        stops[stop] = 1

    pre_index = -2
    cur_index = 0
    stopnum = 0
    while True:
        if pre_index == cur_index:
            print("#{} {}".format(i+1, 0))
            break
        if cur_index + K >= N:
            print("#{} {}".format(i+1, stopnum))
            break
        if stops[cur_index + K] == 1:
            pre_index = cur_index
            cur_index = cur_index + K
            stopnum += 1            
        else:
            cur_index -= 1 