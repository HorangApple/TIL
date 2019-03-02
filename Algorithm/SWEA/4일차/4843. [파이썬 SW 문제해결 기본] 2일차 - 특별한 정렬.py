import sys
sys.stdin = open("input.txt","r")


T=int(input())

for i in range(T):
    # n : 정수의 개수, a : n개의 정수
    n=int(input())
    a = list(map(int, input().split()))
    result = []
    
    # 한 번에 두 개씩 검색하니 길이의 절반만큼 반복
    for k in range(len(a)//2) :
        maxnum = 1
        minnum = 100
        maxidx = 0
        minidx = 0
        idx = 0
        # 최대, 최소 값과 index를 구하고 -1로 초기화
        while idx < len(a) :
            if a[idx]>maxnum and a[idx] != -1:
                maxnum = a[idx]
                maxidx = idx
            if a[idx]<minnum and a[idx] != -1:
                minnum = a[idx]
                minidx = idx
            idx+=1
        a[maxidx], a[minidx] = -1, -1
        result +=[str(maxnum),str(minnum)]

    if len(a)%2 !=0 :
        for j in a :
            if j >0 :
                result +=[str(j)]
                break

    # N개의 정수가 주어지면 
    # 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 
    # 큰 수와 작은 수를 번갈아 정렬
    # ex. 10 1 9 2 8 3 7 4 6 5
    print(f'#{i+1} {" ".join(result[:10])}')

    # 선생님 코드
    
TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(10):
        minI = maxI = i
        if i % 2 == 0:
            for j in range(i + 1, N):
                if nums[maxI] < nums[j] : maxI = j
            nums[i], nums[maxI] = nums[maxI], nums[i]
        else:
            for j in range(i + 1, N):
                if nums[minI] > nums[j] : minI = j
            nums[i], nums[minI] = nums[minI], nums[i]

    print("#%d"%tc, end=' ')
    for i in range(10) : print(nums[i], end=' ')
    print()