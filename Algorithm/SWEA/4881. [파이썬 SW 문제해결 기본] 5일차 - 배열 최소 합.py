import sys
sys.stdin = open("input.txt","r")

def backtrack(a,k,inp,result,check):
    c=[0]*(inp+1)
    if k==inp:
        total=0
        for i in range(inp):
            total+=mp[i][result[i+1]-1]
            if total>mini[0]:
                break
        else:
            mini[0]=total
    else:
        k+=1
        construct_candidates(a,k,inp,c)
        for i in range(1,inp+1):
            if c[i]>0:
                result[k]=c[i]
                check+=mp[k-1][result[k]-1]
                if check>mini[0]:
                    check-=mp[k-1][c[i]-1]
                    continue
                a[i]=0
                backtrack(a,k,inp,result,check)
                a[i]=c[i]
                check-=mp[k-1][c[i]-1]
def construct_candidates(a,k,inp,c):
    for i in range(1,inp+1):
        if a[i]>0:
            c[a[i]]=a[i]


tc=int(input())
for num in range(1,tc+1):
    length=int(input())
    mp=[list(map(int,input().split())) for _ in range(length)]
    result=[0]*(length+1)
    a=list(range(length+1))
    mini=[999999999999999999999999999]
    backtrack(a,0,length,result,0)
    print(f'#{num} {mini[0]}')
