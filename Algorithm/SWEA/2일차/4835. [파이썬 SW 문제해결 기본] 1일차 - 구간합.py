import sys
sys.stdin = open("4835_input.txt","r")
# 합치는 함수
def mySum(numList):
    result = 0
    for i in numList:
        result += i
    return result

T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    numList = list(map(int, input().split()))
    minSum = mySum(numList[0:0+M])
    maxSum = mySum(numList[0:0+M])

    # 길이 M 만큼 합쳐서 비교한다.
    for i in range(1, N-M+1) :
        obj = mySum(numList[i:i+M])
        if minSum > obj :
            minSum = obj
        if maxSum < obj :
            maxSum = obj

    print(f'#{test_case} {maxSum-minSum}')


# 선생님 풀이
TC = int(input())
for tc in range(1, TC+1) :
    N,M = map(int, input().split())
    v = [i for i in range(1, N+1)]
    for i in range(M) :
        sum+= v[i]
    minv = maxv = sum
    for i in range(1, N-M+1):
        sum = 0
        for j in range(i, i+M):
            sum+= v[j]
        if maxv<sum:maxv = sum
        if minv>sum:minv = sum
    print("#%d %d"%(tc,maxv-minv))