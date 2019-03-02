import sys
sys.stdin = open("input.txt","r")

T = int(input())

# 회문인지 확인하고 회문이면 그 문자열을 리턴
def goAround (str,M):
    strlen = len(str)
    # 길이 M만큼 처음부터 strlen-M까지를 각각 시작점으로 검사
    for i in range(strlen-M+1) :
        obj = str[i:i+M]
        if obj == obj[::-1] :
            return obj
    return 0


def solution (N,M,strlist) :
    for i in range(N) :
        # 가로 방향으로 회문 탐색
        result = goAround(strlist[i], M)
        # 회문을 찾으면 리턴, 아니면 다음 절차로 넘어감
        if result :
            return result
            
        # 세로 방향으로 회문 탐색
        column = ""
        for k in range(N):
            column += strlist[k][i]
        result = goAround(column, M)
        # 회문을 찾으면 리턴, 아니면 다음 절차로 넘어감
        if result :
            return result

for i in range(T):
    N, M = map(int, input().split())
    strlist = ["" for j in range(N)]
    result =""
    for j in range(N):
        strlist[j] = input()
    print(f'#{i+1} {solution(N, M, strlist)}')

