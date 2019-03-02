import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1, T+1):
    k, n, m = list(map(int, input().split()))
    mSet = list(map(int, input().split()))
    count = 0
    location = 0
    maxCharger = 0
    # 0번 정류장부터 시작
    for i in range(m) :
        # 도착여부 확인
        if location + k >= n :
            break
        # k칸을 앞으로 가서 충전소(mSet[j])를 지나면 maxCharger에 초기화
        for j in range(i,m):        
            if location + k >= mSet[j] :
                maxCharger = mSet[j] 
            else :
                break
        # 어차피 충전소를 거쳐야 앞으로 가니 다음 출발점은 지나갔던 충전소로 초기화
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
굳이 인덱스를 사용하여 리스트 요소를 비교하지 않고 인덱스만으로만 비교해서 풀 수도 있다.
"""
# # 선생님 코드
# T= int(input())
# for tc in range(1,T+1) :
#     K,N,M = map(int, input().split())
#     charging_station = list(map(int, input().split()))
#     stations = [0] * N
#     for i in range(M):
#         stations[charging_stations[i]] = 1
        
#     cnt = cur = 0
#     while(True) :
#         pre=cur
#         cur += k
#         if cur >= N :
#             break
#         if stations[cur] == 1 :
#             cnt+= 1
#         else :
#             for i in range(1,k+1):
#                 if stations[cur-1] == 1:
#                     cur-=i
#                     cnt+=1
#             if cur == pre :
#                 cnt = 0
#                 break
#     print("#%d" %tc, cnt)