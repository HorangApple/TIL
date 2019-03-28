import sys
sys.stdin = open('input.txt','r')


def candidate(a,n,k):
    c=[False]*(n+1)
    for i in a[1:]:
        if i>0:
            c[i]=True
    return c

def solution(a,n,k,total):
    global mini
    if n==k:
        if mini>total:
            mini=total
    else:
        k+=1
        candi = candidate(a,n,k)
        for i in range(1,n+1):
            if not candi[i]:
                a[k]=i
                save = total
                total+=inp[k-1][i-1]
                if mini>total:
                    solution(a,n,k,total)
                total = save
                a[k]=0

TC = int(input())
for num in range(1,TC+1):
    n = int(input())
    inp = [list(map(int,input().split())) for _ in range(n)]
    a=[0]*(n+1)
    total=0
    mini=99999999
    solution(a,n,0,total)
    print(f'#{num} {mini}')