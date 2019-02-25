import sys
sys.stdin = open("input.txt","r")

def solution(start,length):
    que=[start]
    visited=[False]*length
    deepList=[[] for _ in range(50)]
    while que:
        go,deep=que.pop(0)
        nextNod=[]
        for i in mp[go]:
            if i>0 and not visited[i] and i not in que:
                que.append([i,deep+1])
                nextNod.append(i)
        if 0==len(nextNod) and not visited[go] :
            deepList[deep+1].append(go)
        visited[go]=True
    return deepList          

TC=10
for num in range(1,TC+1):
    length,start=map(int,input().split())
    inp=list(map(int,input().split()))
    mp=[[0]*length for _ in range(length)]
    for i in range(len(inp)//2):
        mp[inp[2*i]][inp[2*i+1]]=inp[2*i+1]
    result=solution([start,0],length)
    for i in range(49,-1,-1):
        if result[i]!=[]:
            result=result[i]
            break
    print(f'#{num} {max(result)}')