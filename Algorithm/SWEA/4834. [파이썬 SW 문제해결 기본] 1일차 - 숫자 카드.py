import sys
sys.stdin = open("sample_input.txt","r")

def my_count(numList, obj) :
    count = 0
    for i in numList :
        if obj == i :
            count += 1
    return count
        

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numList = [int(x) for x in input()]
    maxNum = 0
    maxCount = 0
    for obj in numList :
        if my_count(numList, obj) > maxCount :
            maxCount = my_count(numList, obj)
            maxNum = obj
        elif my_count(numList, obj) == maxCount and maxNum < obj :
            maxNum = obj

    print(f'#{test_case} {maxNum} {maxCount}')