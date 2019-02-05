import sys
sys.stdin = open("input.txt","r")

def mysplit(inp):
    result = []
    for i in range(len(inp)//2): 
        result.append([inp[2*i],inp[2*i+1]])
    return result

def search(a, n):
    result = []
    result += a[0]
    while True :
        resultfront = result[0]
        resultback = result[-1]
        for i in a :
            if i[0]==resultback :
                result += i
            elif i[-1]==resultfront:
                result = i+result
        if len(result) == n :
            return result      


T=int(input())

for i in range(T):
    # n : 막대의 개수, a : 2n개, 2개씩 수나사 굵기, 암나사 굵기를 뜻함
    n = int(input())
    a = mysplit(input().split())

    # 어떤 순서로 연결해야 가장 많이 연결?
    print(f'#{i+1} {" ".join(search(a,2*n))}')

# 선생님 코드
TC = int(input())
for tc in range (1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        found = False
        for j in range(N):
            if arr[i * 2] == arr[j * 2 + 1] :
                found = True
                break
        if found == False:
            start_position = i
            break

    arr[0], arr[start_position * 2] = arr[start_position * 2], arr[0]
    arr[1], arr[start_position * 2 + 1] = arr[start_position * 2 + 1], arr[1]

    for i in range(1, N - 1):
        for j in range(i, N):
            if arr[i * 2 - 1] == arr[j * 2]:
                arr[i * 2], arr[j * 2] = arr[j * 2], arr[i * 2]
                arr[i * 2 + 1], arr[j * 2 + 1] = arr[j * 2 + 1], arr[i * 2 + 1]
                break

    print("#%d "%tc, end=' ')
    for i in range(N*2):
        print("%d "%arr[i], end=' ')
    print()