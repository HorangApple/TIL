import sys
sys.stdin = open("input.txt","r")

# [수나사,암나사] 형식으로 저장
def mysplit(inp):
    result = []
    for i in range(len(inp)//2): 
        result.append([inp[2*i],inp[2*i+1]])
    return result

# 일치한 것끼리 있는지 조사
# 여기서 a는 나사들, length는 최종 결과의 길이를 가리킴
def search(a, length):
    result = []
    result += a[0] # 우선 임의의 나사로 시작

    # 완성될 때까지 무한 반복
    while True : 
        resultfront = result[0] # 맨 앞의 수나사
        resultback = result[-1] # 맨 뒤의 암나사
        # 모든 나사와 비교, 
        # 수나사와 암나사의 크기가 서로 다르기 때문에 같은 것이 또 나와도 무시 가능
        for i in a : 
            if i[0]==resultback : # 암나사와 일치하면 뒤에 연결
                result += i
            elif i[-1]==resultfront: # 수나사와 일치하면 앞에 연결
                result = i+result
        if len(result) == length : # 예상된 길이 (막대의 개수*2)가 되면 리턴
            return result      


T=int(input())

for i in range(T):
    # n : 막대의 개수, a : 2n개, 2개씩 수나사 굵기, 암나사 굵기를 뜻함
    n = int(input())
    a = mysplit(input().split())

    # 어떤 순서로 연결해야 가장 많이 연결?
    print(f'#{i+1} {" ".join(search(a,2*n))}')


# # 선생님 코드
# TC = int(input())
# for tc in range (1, TC+1):
#     N = int(input())
#     arr = list(map(int, input().split()))

#     for i in range(N):
#         found = False
#         for j in range(N):
#             if arr[i * 2] == arr[j * 2 + 1] :
#                 found = True
#                 break
#         if found == False:
#             start_position = i
#             break

#     arr[0], arr[start_position * 2] = arr[start_position * 2], arr[0]
#     arr[1], arr[start_position * 2 + 1] = arr[start_position * 2 + 1], arr[1]

#     for i in range(1, N - 1):
#         for j in range(i, N):
#             if arr[i * 2 - 1] == arr[j * 2]:
#                 arr[i * 2], arr[j * 2] = arr[j * 2], arr[i * 2]
#                 arr[i * 2 + 1], arr[j * 2 + 1] = arr[j * 2 + 1], arr[i * 2 + 1]
#                 break

#     print("#%d "%tc, end=' ')
#     for i in range(N*2):
#         print("%d "%arr[i], end=' ')
#     print()