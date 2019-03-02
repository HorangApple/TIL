import sys
sys.stdin = open("input.txt","r")

def go(road,end):
    h=99
    while h>0:
        h-=1 # 위로 한칸 이동
        # 왼쪽에 길이 있으면 
        if end-1>-1 and road[h][end-1] == 1 :
            # 왼쪽으로 쭉 직진
            while end-1>-1 and road[h][end-1] :
                end-=1 
        # 오른쪽에 길이 있으면 
        elif end+1<100 and road[h][end+1] == 1 :
            # 오른쪽으로 쭉 직진
            while end+1<100 and road[h][end+1] :
                end+=1 
    return end

TC=10
for t in range(TC):
    case=int(input())
    road=[list(map(int,input().split())) for _ in range(100)]
    end=0
    # 마지막 줄에서 도착 위치를 우선 검색
    for i in road[99]:
        if i==2:
            break
        end+=1
    print(f'#{t+1} {go(road,end)}')