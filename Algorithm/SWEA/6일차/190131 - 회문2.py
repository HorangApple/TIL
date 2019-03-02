# import sys
# sys.stdin = open("input.txt","r")
#
# T = 10
#
# def goAround (str):
#     strlen = len(str)
#     for j in range(strlen,0,-1):
#         for i in range(strlen-j+1) :
#             obj = str[i:i+j]
#             if obj == obj[::-1] :
#                 return len(obj)
#     return 1
#
# def solution (N,strlist) :
#     maxObj = 0
#     for i in range(N) :
#         result = goAround(strlist[i])
#         if maxObj < result :
#             maxObj = result
#         column = ""
#         for k in range(N):
#             column += strlist[k][i]
#         result = goAround(column)
#         if maxObj < result :
#             maxObj = result
#
#     return maxObj
#
# for i in range(T):
#     N = 100
#     NC = input()
#     strlist = ["" for j in range(N)]
#     result =""
#     for j in range(N):
#         strlist[j] = input()
#     print(f'#{NC} {solution(N,strlist)}')

import sys
sys.stdin = open("input.txt","r")

T = 10

def goAround(N,K,maxObj,str):
    # j는 회문인지 조사하는 길이
    for j in range(N, 0, -1):
        # i는 앞부터 회문 조사 길이 끝까지의 길이
        for i in range(N - j + 1):
            # 양 쪽에서 움직이기 때문에 길이의 절반 횟수만큼 조사
            # K번째 가로 줄 조사
            for l in range(j // 2):
                a = i + l # 앞 쪽 인덱스
                b = i + j - l- 1 # 뒷 쪽 인덱스
                if str[K][a] != str[K][b]: # 앞 뒤가 다르면 break
                    break
            # 끝까지 비교해서 회문이면 가장 긴 길이인지 확인
            else:
                if maxObj < j:
                    maxObj = j

            # K번째 세로 줄 조사
            for l in range(j // 2):
                a = i + l
                b = i + j - l - 1
                if str[a][K] != str[b][K]:
                    break
            else:
                if maxObj < j:
                    maxObj = j
    # 마지막까지 다 조사하면 리턴
    if K==N-1:
        return maxObj
    # 재귀를 이용해 다음 줄 조사
    else:
        return goAround(N,K+1,maxObj,str)

for i in range(T):
    N = 100
    NC = input()
    strlist = [input() for _ in range(N)]
    result =""

    print(f'#{NC} {goAround(N, 0, 0, strlist)}')