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
    for j in range(N, 0, -1):
        for i in range(N - j + 1):
            for k in range(j // 2):
                a = i + k
                b = i + j - k- 1
                if str[K][a] != str[K][b]:
                    break
            else:
                if maxObj < j:
                    maxObj = j

            for k in range(j // 2):
                a = i + k
                b = i + j - k - 1
                if str[a][K] != str[b][K]:
                    break
            else:
                if maxObj < j:
                    maxObj = j
    if K==N-1:
        return maxObj
    else:
        return goAround(N,K+1,maxObj,str)

for i in range(T):
    N = 100
    NC = input()
    strlist = [input() for _ in range(N)]
    result =""

    print(f'#{NC} {goAround(N, 0, 0, strlist)}')