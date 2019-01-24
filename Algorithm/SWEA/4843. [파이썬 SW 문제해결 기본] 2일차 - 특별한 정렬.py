import sys
sys.stdin = open("input.txt","r")


T=int(input())

for i in range(T):
    # n : 정수의 개수, a : n개의 정수
    n=int(input())
    a = list(map(int, input().split()))
    result = []
    
    for k in range(len(a)//2) :
        maxnum = 1
        minnum = 100
        maxidx = 0
        minidx = 0
        idx = 0
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