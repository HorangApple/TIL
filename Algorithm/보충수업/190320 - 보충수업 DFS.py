'''
모든 정점이 다 연결된 상태가 아닐 수도 있기에 그 점을 염두해둬야한다.
흐름을 익혀서 코드를 잘 작성할 수 있도록 연습한다.
visited가 없으면 사이클이 존재할시 무한 반복을 할 수 있다.
굳이 visited가 없어도 탐색할 때 stack에 저장되어있는지 확인하는 것으로 대체할 수 있다.
DFS로 최단 경로를 찾으려면 가능한 모든 경로들을 찾아봐야한다. BFS가 최단 경로를 구할 때에 적합하다. 
스택에 미리 채워놓고 돌려서 방문한 곳은 빼는 방법이 있는데 이는 중복이 발생할 수 있다.
'''
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
def dfs(v): # v: 시작점
    stack = [] # 스택
    visited = [False] * (V+1)
    visited[v] = True
    print(v, end=' ')
    stack.append(v)
    while len(stack) > 0: # 빈 스택이 아닐 동안
        # v: 현재 방문 정점
        # v의 방문 하지 않은 인접 정점(w) 하나 찾는다.
        for w in G[v]:
            if not visited[w]:
                visited[w]=True
                print(w, end=' ')
                stack.append(v)
                v = w
                break
        else:
            v = stack.pop()

# 재귀 ver, 방문 순서를 저장, 즉 스택을 사용할 필요가 없어서 간단하다.
def dfs2(v): # v: 현재 방문 정점
    visited[v] = True
    print(v,end=' ')
    # 방문하지 않은 인접 정점을 찾아서 방문
    for w in G[v]:
        if not visited[w]:
            dfs2(w)


# 인접 리스트 구현
V, E = map(int, input().split())
G=[[] for _ in range(V+1)]
for i in range(E):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

dfs(1)