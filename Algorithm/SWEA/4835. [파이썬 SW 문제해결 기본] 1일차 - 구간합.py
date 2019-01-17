import sys
sys.stdin = open("4835_input.txt","r")

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

    for i in range(1, N-M+1) :
        obj = mySum(numList[i:i+M])
        if minSum > obj :
            minSum = obj
        if maxSum < obj :
            maxSum = obj

    print(f'#{test_case} {maxSum-minSum}')