import sys
sys.stdin = open('input.txt','r')

def solution(v):
    global total
    que=[[v,0]]
    invited = []
    while len(que)>0:
        v,cnt=que.pop(0)
        if cnt==2:
            total = len(invited)-1
            continue
        cnt+=1
        for i in mp[v]:
            if i not in invited:
                invited.append(i)
                que.append([i,cnt])

            

TC=int(input())
for num in range(1,TC+1):
    n,m = map(int,input().split())
    mp = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        mp[a]+=[b]
        mp[b]+=[a]
    total = 0
    if len(mp[1])== 0 :
        print(f'#{num}',total)
    else:
        solution(1)
        print(f'#{num}',total)