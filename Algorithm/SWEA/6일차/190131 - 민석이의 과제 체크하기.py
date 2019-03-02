import sys
sys.stdin = open("input.txt","r")

T = int(input())

def solution(N,K,goodstd) :
    badStdList=""
    for i in range(1,N+1):
        # 제출한 사람에 해당하지 않는 사람만 리스트에 추가
        if i not in goodstd :
            badStdList +=f'{i} '
    return badStdList

for i in range(T):
    N, K = list(map(int, input().split()))
    goodstd = list(map(int, input().split()))
    print(f'#{i+1} {solution(N,K,goodstd)}')