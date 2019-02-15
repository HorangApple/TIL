import sys
sys.stdin = open("input2.txt","r")

def nextsearch(arr,visited):
    for i in arr:
        if i>0 and i not in visited :
            return i
    return False

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
        while back :
            back = backsearch(arr,w,visited)
            if back !=False :
                w=back
        if w :
            stack.append(v)
        while w:
            visited.append(w)
            stack.append(w)
            v = w
            w = nextsearch(arr[v],visited)
            back = backsearch(arr,w,visited)
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
    for i in range(e) :
        x=line[i*2]
        y=line[i*2+1]
        arr[x][y]=y
        endlist[y]+=1

    print(f'#{t+1} ',end="")
    count=1
    for i in endlist[1:]:
        if count not in visited and i==0:
            dfs(arr,count)
        count+=1
    for i in visited :
        print(f'{i} ',end="")
    print("")