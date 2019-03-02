import sys
sys.stdin = open("sample_input.txt","r")

# 해당 숫자(obj)의 갯수를 세는 함수
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
        # 갯수가 큰 쪽을 저장한다
        if my_count(numList, obj) > maxCount :
            maxCount = my_count(numList, obj)
            maxNum = obj
        # 갯수가 같으면 숫자가 큰 쪽을 저장한다
        elif my_count(numList, obj) == maxCount and maxNum < obj :
            maxNum = obj

    print(f'#{test_case} {maxNum} {maxCount}')


# 선생님 풀이

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    cards = input()
    cnt = [0]*10
    for i in range(N):
        cnt[int(cards[i])]+=1
    maxI=0
    for i in range(10):
        if cnt[maxI]<=cnt[i]:
            maxI = i
    print("#%d %d %d" % (tc,maxI,cnt[maxI]))

'''
다른 배열을 만들어 인덱스를 이용해 카운팅을 한다.
'''