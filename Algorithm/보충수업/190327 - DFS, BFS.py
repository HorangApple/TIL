# https://lab.ssafy.com/Jung/aps_study/tree/master/03%EC%9B%94%2025%EC%9D%BC/%EC%B5%9C%EB%8B%A8%EA%B2%BD%EB%A1%9C
# http://problems.kr/
import sys
sys.stdin = open('input.txt','r')
'''
from collections import deque
def BFS(s): # s: 시작점
    D = [0xfffff]*(V+1) # D[s] = 0, 나머지 큰 값, 값 설정하는 것이 중요하다.
    P = [i for i in range(V+1)]
    D[s] = 0
    Q = deque()
    Q.append(s)
    while len(Q):
        u = Q.popleft()
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                Q.append(v)

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for i in range(E):
    u,v,w = map(int, input().split())
    G[u].append((v,w))
    G[v].append((u,w))

BFS(1)


def DFS(s): # s: 시작점
    for v, w in G[u]:
        if D[v] > D[u] + w:
            D[v] = D[u] + w
            P[v] = u
            DFS(v)

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for i in range(E):
    u,v,w = map(int, input().split())
    G[u].append((v,w))
    G[v].append((u,w))

D = [0xfffff]*(V+1) # D[1] = 0, 나머지 큰 값, 값 설정하는 것이 중요하다.
P = [i for i in range(V+1)]
D[1] = 0
DFS(1)
'''
# 문자열은 immutable이라 메모리를 많이 잡아먹는다.


# 동전 교환 문제, 최소 동전 수는?
# 탐욕으로 풀 수 있다는 보장은 없기에 완전탐색으로 풀어야 한다.
# 최적화 문제 -> 완전탐색,완전검색 -> 백트래킹(상태공간트리)
#                                -> 동적계획법(문제간의 관계, 문제 풀다 발견하는 실마리)
# 8 -> 2/4/7 -> 1/0,3/1,3,6/ ->... 식으로 상태공간 트리가 됨 
# f(n) = f(n-6)+1 / f(n-4)+1 / f(n-1)+1
coin = [6,4,1]
sol = [0] * 100
MIN = 0xffffff
def coinChange(k,n):
    global MIN
    if k >= MIN: return
    if n == 0:
        MIN = min(MIN, k)
        print(sol[:k])
        return

    for val in coin :
        if val > n : continue
        sol[k] = val
        coinChange(k+1, n-val)

coinChange(0,8) # 노드의 높이, 거스름돈

# DP 적용
coin = [6,4,1]
sol = [0] * 100

def coinChange(n):
    if n == 0: return 0
    MIN = 0xffffff
    for val in coin :
        if val > n : continue
        ret = coinChange(n-val)
        MIN = min(ret,MIN)
    return MIN+1

coinChange(8) # 노드의 높이, 거스름돈