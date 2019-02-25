import sys
sys.stdin = open("input.txt","r")

def solution(start):
    que=[start]
    visited=[False]*8
    result=[]
    while que:
        go=que.pop(0)
        visited[go]=True
        result.append(str(go))
        for i in mp[go]:
            if i>0 and not visited[i] and i not in que:
                que.append(i)
    return result
        
inp=list(map(int,input().split()))
mp=[[0]*8 for _ in range(8)]
for i in range(len(inp)//2):
    mp[inp[2*i]][inp[2*i+1]]=inp[2*i+1]

print("-".join(solution(1)))