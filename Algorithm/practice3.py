import sys
sys.stdin = open("input2.txt","r")

def nextsearch(arr,visited):
    for i in arr:
        if i not in visited and i>0:
            return i
    return False

def backsearch(arr,s,visited):
    for i in range(len(arr[s])):
        back=arr[i][s]
        if back>0 and i not in visited :
            return i
    else:
        return False

def dfs (arr,v):
    back = backsearch(arr,v,visited)
    while back :
        back = backsearch(arr,v,visited)
        if back !=v and back !=False :
            v=back
    visited.append(v)
    while v :
        w=nextsearch(arr[v],visited)
        back = backsearch(arr,v,visited)
        if back != False :
            w=back
        elif w :
            stack.append(v)
        while w:
            back = backsearch(arr,v,visited)
            if back != False :
                back = backsearch(arr,v,visited)
                while back :
                    back = backsearch(arr,v,visited)
                    if back !=v and back !=False :
                        v=back
                break
            visited.append(w)
            stack.append(w)
            v=w
            w=nextsearch(arr[v],visited)
        v=stack.pop()
    return visited

TC = 1
for t in range(TC) :
    v,e=map(int,input().split())  
    line=list(map(int,input().split()))
    s=line[3]
    visited = []
    stack = [0]
    arr=[[0 for _ in range(v+1)] for _ in range(v+1)]
    for i in range(len(line)//2) :
        x=line[i*2]
        y=line[i*2+1]
        arr[x][y]=y
    print(f'#{t+1} ',end="")
    count=0
    for i in dfs(arr,s) :
        print(f'{i} ',end="")
        count+=1
    print("")
    print(count)