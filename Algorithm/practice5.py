import sys
sys.stdin = open("input.txt","r")

def solution(start,length):
    que=[start]
    visited=[False]*length
    deepList=[[0]]*100
    while que:
        go,deep=que.pop(0)
        visited[go]=True
        nextNod=[]
        for i in mp[go]:
            if i>0 and not visited[i] and i not in que:
                que.append([i,deep+1])
                nextNod.append(i)
        if 0==len(nextNod):
            deepList[deep+1]+=[go]
    return deepList          

TC=10
for num in range(1,TC+1):
    length,start=map(int,input().split())
    inp=list(map(int,input().split()))
    mp=[[0]*length for _ in range(length)]
    for i in range(len(inp)//2):
        mp[inp[2*i]][inp[2*i+1]]=inp[2*i+1]

    print(f'#{num} {solution([start,0],length)[-1]}')