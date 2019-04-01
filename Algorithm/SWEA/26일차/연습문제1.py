import sys
sys.stdin = open('input.txt','r')

def dfs(v):
    visited.append(v)
    for i in mp[v]:
        if i not in visited:
            dfs(i)

def dfs2(v):
    stack=[]
    stack.append(v)
    while len(stack)>0:
        v=stack.pop()
        if v not in visited:
            visited.append(v)
            for i in mp[v]:
                if i not in visited:
                    stack.append(i)
                    break
            

inp=list(map(int,"1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7".split()))
mp=[[] for _ in range(8)]
for i in range(len(inp)//2):
    mp[inp[i*2]] += [inp[i*2+1]]
    mp[inp[i*2+1]] += [inp[i*2]]
visited = []
dfs2(1)
print(visited)