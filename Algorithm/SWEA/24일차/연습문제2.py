import sys
sys.stdin = open('input.txt','r')

def backtrack(a, k, n): # k는 깊이 inp는 자릿수
    c=[0]*2
    if sum(a)==10:
        for i in a:
            if i>0:
                print(i,end=" ")
        print()
    elif k==n:
        return
    else:
        k+=1
        ncandidates=construct_candidates(a,k,c) # 자리에 올 후보군을 추린다.
        for i in range(ncandidates):
            if c[i]:
                a[k]=inp[k-1]
                if sum(a)>10:
                    continue
            else:
                a[k]=0
            backtrack(a,k,n)
        
            
def construct_candidates(a,k,c):
    c[0]=True
    c[1]=False
    return 2


inp = list(map(int, input().split()))
NMAX=11
a=[0]*NMAX
backtrack(a,0,10)