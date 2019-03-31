# https://www.acmicpc.net/problem/17071
import sys
sys.stdin = open("input.txt","r")
# def sumN(n):
#     return n*(n+1)//2

# from collections import deque
# def solution(n,cnt):
#     global mini,k
#     dong=k+sumN(cnt)
#     if k-n>n:
#         return
#     elif mini>cnt :
#         if n==dong:
#             print(cnt)
#             mini=min(mini,cnt)
#         elif -1<n<500001 and -1<dong<500001:
#             cnt+=1
#             solution(n+1,cnt)
#             solution(n-1,cnt)
#             solution(n*2,cnt)

# n,k=map(int,input().split())
# mini = 0xfffff
# solution(n,0)
# if mini==0xfffff:
#     print(-1)
# else:
#     print(mini)


from collections import deque
def sumN(n):
    return n*(n+1)//2

def solution(n,cnt):
    global mini,d
    que=deque()
    que.append((n,cnt))
    while len(que)>0:
        n,cnt=que.popleft()
        k=d+sumN(cnt)
        if sumN(cnt)>n or cnt>1000:
            continue
        if mini>cnt :
            if n==k:
                mini=min(mini,cnt)
            elif -1<n<500001 and -1<k<500001:
                cnt+=1
                print(cnt)
                que.append((n*2,cnt))
                que.append((n+1,cnt))
                if n>k:
                    que.append((n-1,cnt))

T=int(input())
for _ in range(T):
    n,d=map(int,input().split())
    mini = 0xfffff
    solution(n,0)
    if mini==0xfffff:
        print(-1)
    else:
        print(mini)