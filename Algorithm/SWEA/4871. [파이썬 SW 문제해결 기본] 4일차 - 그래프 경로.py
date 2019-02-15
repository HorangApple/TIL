import sys
sys.stdin = open("input.txt","r")

def search(arr,visited):
    for i in arr:
        if i not in visited and i>0:
            return i
    else :
        return False

def dfs (arr,s,g):
    v=s
    visited.append(v)
    while v :
        w=search(arr[v-1],visited)
        if w==g:
            return 1
        if w :
            stack.append(v)
        while w:
            visited.append(w)
            stack.append(w)
            v=w
            w=search(arr[v-1],visited)
            if w==g:
                return 1
        v=stack.pop()
    return 0

TC = int(input())
for i in range(TC) :
    v,e=map(int,input().split())
    lines=[]
    for _ in range(e):
        line=list(map(int,input().split()))
        lines.append(line)
    s,g=map(int,input().split())

    visited = []
    stack = [0]
    arr=[[0 for _ in range(v)] for _ in range(v)]
    for x,y in lines :
        arr[x-1][y-1]=y
 

    print(f'#{i+1} {dfs(arr,s,g)}')