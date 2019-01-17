import sys
sys.stdin = open("input.txt","r")

def searchMax (lists) :
    maxValue = max(lists)
    maxIdx = lists.index(maxValue)
    return maxIdx

def searchMin (lists) :
    minValue = min(lists)
    minIdx = lists.index(minValue)
    return minIdx

def result (lists, maxIdx, minIdx) :
    return lists[maxIdx]-lists[minIdx] 

for j in range(1, 11):
    dump = int(input())
    lists = list(map(int, input().split()))
    
    # 최고점 찾기
    maxIdx = searchMax (lists)
    # 최저점 찾기
    minIdx = searchMin (lists)  
    # 덤프 횟수만큼 반복
    for i in range(dump) :
        # 최고점 - 최저점이 1 이하이면 break
        if result(lists, maxIdx, minIdx) <= 1:
            break
        # 최고점에서 -1, 최저점에 +1
        lists[minIdx]+=1
        lists[maxIdx]-=1
        # 최고점 찾기
        maxIdx = searchMax (lists)
        # 최저점 찾기
        minIdx = searchMin (lists)    
    # 최고점 - 최저점 출력
    print(f'#{j} {result(lists, maxIdx, minIdx)}')