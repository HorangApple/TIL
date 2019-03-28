import sys
sys.stdin = open('input.txt','r')

def solution (l,r):
    global ans
    middle = (l+r)//2 
    if l==r:
        ans = middle
        return
    people = 0
    for i in range(n):
        people+=middle//t[i]
    if people<m:
        solution(middle+1,r)
    elif people>=m :
        solution(l,middle)


TC = int(input())
for num in range(1,TC+1):
    n,m = map(int,input().split())
    t = [int(input()) for _ in range(n)]
    maxi = min(t)*m
    ans = 0
    solution (0,maxi)
    print(f"#{num}",ans)

# 다른 것을 기준으로 이진탐색을 할 수 있다.