import sys
sys.stdin = open("input.txt","r")

def solution(n,m):
    for _ in range(m):
        save=inp.pop(0) # 빼고
        inp.append(save) # 넣는다
    return inp[0] # 다 돌고 맨 첫 번째 요소를 리턴

TC=int(input())
for num in range(1,TC+1):
    n,m=map(int,input().split())
    inp=list(map(int,input().split()))
    print(f'#{num} {solution(n,m)}')