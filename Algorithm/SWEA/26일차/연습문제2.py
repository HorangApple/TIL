import sys
sys.stdin = open('input.txt','r')

def bfs(v):
    que=[v]
    while len(que)>0:
        v=que.pop(0)
        visited.append(v)
        for i in mp[v]:
            if i not in visited and i not in que:
                que.append(i)
            

inp=list(map(int,"1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7".split()))
mp=[[] for _ in range(8)]
for i in range(len(inp)//2):
    mp[inp[i*2]] += [inp[i*2+1]]
    mp[inp[i*2+1]] += [inp[i*2]]
visited = []
que=[]
bfs(1)
print(visited)