# 그래프처럼 저장하여 내가 문제를 풀 수 있게 한다.
# 사이클이 없는 방향 그래프 -> 위상정렬 / 순서를 절대적으로 지켜야한다.
# 트리에서 싸이클이 생기면 안된다. 대개 임의의 트리에 간선이 하나 추가되면 발생한다.
# 트리의 특징은 두 정점 간의 가는 방법은 오직 하나 뿐이다.
# 유향 그래프인지 무향 그래프인지 확인하고 인접 행렬, 또는 인접 리스트에 저장을 한다.

# 정점수(V), 간선수(E)
# 간선정보 -> 두 정점으로 표현
# 정점의 식별값 -> 1~V까지

# 인접 리스트 구현
inp=[1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
node=[[] for _ in range(7+1)]
for i in range(len(inp)//2):
    node[inp[2*i]]+=[inp[2*i+1]]
    node[inp[2*i+1]]+=[inp[2*i]]
print(node)
'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''
V, E = map(int,input().split()) # 정점수(V), 간선수(E)
G = [[] for _ in range(V+1)]
for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u) # 무향 그래프

visit = [False]*(V+1)

for i in range(1,V+1):
    print(i,'-->',G[i])

# return Value로 재귀함수를 만드는 것이 메모이제이션 구현할 때도 좋다.