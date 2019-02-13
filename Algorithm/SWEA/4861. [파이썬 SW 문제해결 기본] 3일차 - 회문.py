import sys
sys.stdin = open("input.txt","r")

T = int(input())

def goAround (str,M):
    strlen = len(str)
    for i in range(strlen-M+1) :
        obj = str[i:i+M]
        if obj == obj[::-1] :
            return obj
    return 0


def solution (N,M,strlist) :
    for i in range(N) :
        result = goAround(strlist[i], M)
        if result :
            return result
        column = ""
        for k in range(N):
            column += strlist[k][i]
        result = goAround(column, M)
        if result :
            return result

for i in range(T):
    N, M = map(int, input().split())
    strlist = ["" for j in range(N)]
    result =""
    for j in range(N):
        strlist[j] = input()
    print(f'#{i+1} {solution(N, M, strlist)}')

