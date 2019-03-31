import sys
sys.stdin = open('p2.txt','r')

def mySum():
    for i in range(1<<6):
        one=[]
        for j in range(6):
            if i &1<<j:
                one.append(j)
        if len(one)==3:
            sumCase.append(one)

def solution(m):
    for i in range(1<<m):
        one=[]
        for j in range(1,m+1):
            if i&1<<j:
                one.append(j)
        if len(one)==2 and one not in case:
            case.append(one)

T = int(input())
for num in range(1,T+1):
    n, m = map(int,input().split())
    inp = [list(map(int,input().split())) for _ in range(n)]
    case=[]
    sumCase=[]
    solution(m)
    mySum()
    result=[]
    for i in range(1,n):
        for j in case:
            a1,a2,a3,a4,a5,a6=0,0,0,0,0,0
            for k in range(i):
                a1+=sum(inp[k][:j[0]])
                a2+=sum(inp[k][j[0]:j[1]])
                a3+=sum(inp[k][j[1]:])
            for q in range(k+1,n):
                a4+=sum(inp[q][:j[0]])
                a5+=sum(inp[q][j[0]:j[1]])
                a6+=sum(inp[q][j[1]:])
            six=[a1,a2,a3,a4,a5,a6]
            for one in sumCase:
                result.append(abs(six[one[0]]-six[one[1]])+abs(six[one[0]]-six[one[2]])+abs(six[one[1]]-six[one[2]]))
    print(f'#{num}',max(result))