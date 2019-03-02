import sys
sys.stdin = open("input.txt","r")

# 하위 노드가 있는지 탐색
def nextsearch(arr,visited):
    for i in arr:
        if i>0 and i not in visited :
            return i
    return False

# 상위 노드가 있는지 탐색
def backsearch(arr,s,visited):
    for i in range(v+1):
        back=arr[i][s]
        if back>0 and i not in visited :
            return i
    return False

def dfs (arr,v):
    stack = [0]
    visited.append(v)
    while v :
        w=nextsearch(arr[v],visited)
        back = backsearch(arr,w,visited)
        # 상위 노드가 있다면 계속 이어진 맨 위에 있는 노드까지 탐색
        while back :
            back = backsearch(arr,w,visited)
            if back !=False :
                w=back
        # 하위 노드가 있다면 스택에 추가
        if w :
            stack.append(v)
        # 하위 노드가 더 이상 없을 때까지 탐색
        while w:
            # 다음 노드에 이동하면 visited, stack에 추가
            visited.append(w)
            stack.append(w)
            v = w
            # 위, 아래 노드 있는지 탐색
            w = nextsearch(arr[v],visited)
            back = backsearch(arr,w,visited)
            # 탐색하다 상위 노드가 있으면 다시 거꾸로 올라감
            while back :
                back = backsearch(arr,w,visited)
                if back !=False :
                    w=back
        v=stack.pop()

TC = 10
for t in range(TC) :
    v,e=map(int,input().split())  
    line=list(map(int,input().split()))
    s=line[1]
    visited = []
    endlist=[0]*(v+1)
    arr=[[0 for _ in range(v+1)] for _ in range(v+1)]

    # 인접행렬 arr 생성
    for i in range(e) :
        x=line[i*2]
        y=line[i*2+1]
        arr[x][y]=y
        # 테스트 케이스 중 그래프가 두 개 이상으로 나누어진 경우가 있어
        # 최상위 노드만 고르도록 작업을 함 (요소가 0이면 최상위 노드를 나타냄)
        endlist[y]+=1

    print(f'#{t+1} ',end="")
    # 노드 번호를 나타냄
    count=1
    for i in endlist[1:]:
        # 기존에 방문하지 않았던 곳이고 최상위 노드인 것
        if count not in visited and i==0:
            dfs(arr,count)
        count+=1
    for i in visited :
        print(f'{i} ',end="")
    print("")
