import sys
sys.stdin = open("input.txt","r")

c = int(input())

def solution (n,m,count,friends):
    pairLists = []
    pairs = []
    sum = []

    # 학생 수가 2일 떄 
    if n == 2:
        return 1 
    # 원소 수가 3개인 부분집합만 추리기
    for i in range(1<<m):
        for j in range(m):
            if i & (1<<j):
                pairs.append(friends[j])
        if len(pairs) == int(n/2) :
            pairLists.append(pairs)
        pairs = []

    # 집합으로 만들어 중복을 제거 한 후 원소 수와 학생 수 비교
    for i in pairLists:
        for j in i :
            sum += j
        if len(set(sum)) == n :
            count +=1
        sum = []
    return count 

for i in range(c):
    # n은 학생수, m은 친구 쌍의 수
    n, m = map(int,input().split())
    inp = list(map(int,input().split()))
    friends = [[inp[2*i],inp[2*i+1]] for i in range(m)]
    count = 0
    print(f'{solution(n,m,count,friends)}')

