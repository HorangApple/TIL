import sys
sys.stdin = open("input.txt","r")

def backtrack(a,k,inp):
    c=[0]*4
    if k==inp:
        for i in range(1,k+1):
            print(a[i],end=" ")
        print()
        pass
    else:
        k+=1
        ncandidates=construct_candidates(a,k,inp,c)
        for i in range(ncandidates):
            a[k]=c[i]
            backtrack(a,k,inp)
def construct_candidates(a,k,inp,c):
    in_perm=[False]*100
    for i in range(1,k):
        in_perm[a[i]]=True
    ncandidates=0
    for i in range(1,inp+1):
        if in_perm[i]==False:
            c[ncandidates]=i
            ncandidates+=i
    return ncandidates


tc=int(input())
for num in range(1,tc+1):
    length=int(input())
    mp=[list(map(int,input().split())) for _ in range(length)]
    forbi=[]
    a=[0]*4
    backtrack(a,0,2)

