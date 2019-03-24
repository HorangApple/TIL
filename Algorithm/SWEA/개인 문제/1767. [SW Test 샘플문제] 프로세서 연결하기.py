# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf&
import sys
sys.stdin = open('input.txt','r')

dx = [0,1,0,-1,0]
dy = [1,0,-1,0,0]


def dfs(v,lines,cntCore):
    y=allCore[v][0]
    x=allCore[v][1]
    for i in range(5):
        line=[]
        sy=y+dy[i]
        sx=x+dx[i]
        while -1<sy<n and -1<sx<n and i!=4:
            if mp[sy][sx]!=1 and [sy,sx] not in lines:
                line.append([sy,sx])
            else:
                break
            sy+=dy[i]
            sx+=dx[i]
        else:
            if i!=4:
                cntCore+=1
            cntLines=lines+line
            if v+1<len(allCore):
                dfs(v+1,cntLines,cntCore)
            else:
                a=len(cntLines)
                answerCnt.append(cntCore)
                answer.append(a)
            if i!=4:
                cntCore-=1
    

TC = int(input())
for num in range(1,TC+1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    allCore=[]
    lines=[]
    answer=[]
    answerCnt=[]
    cntCore=0
    for y in range(1,n-1):
        for x in range(1,n-1):
            if mp[y][x]==1:
                allCore.append([y,x])
    dfs(0,lines,cntCore)
    maxi=0
    cnt=0
    for i in answerCnt:
        if maxi<i:
            idx=[]
            maxi=i
            idx.append(cnt)
        elif maxi==i:
            idx.append(cnt)
        cnt+=1

    mini=99999999999999
    result=0
    for i in idx:
        if mini>answer[i]:
            mini=answer[i]
    print(f"#{num}",mini)