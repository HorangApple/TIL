visited = []
stack = [0]
arr=[[0 for _ in range(7)] for _ in range(7)]
root=[(1,2),(1,3),(2,4),(2,5),(4,6),(5,6),(6,7),(3,7)]
for x,y in root :
    arr[x-1][y-1]=y
    arr[y-1][x-1]=x

def search(arr,visited):
    for i in arr:
        if i not in visited and i>0:
            return i
    else :
        return False

def dfs (arr):
    v=1
    visited.append(v)
    while v :
        w=search(arr[v-1],visited)
        if w :
            stack.append(v)
        while w:
            visited.append(w)
            stack.append(w)
            v=w
            w=search(arr[v-1],visited)
        v=stack.pop()
    return visited

print("{}-{}-{}-{}-{}-{}-{}".format(*dfs(arr)))
