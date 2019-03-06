import sys
sys.stdin = open("input.txt","r")

chusCnt=int(input())
chus=list(map(int, input().split()))
marblesCnt=int(input())
marbles=list(map(int, input().split()))

def powerSet(a,k,inp):
    if k==inp:
        print()
    else:
        c=[0,1]
        ncan=2
        k+=1
        for i in range(2):
            a[k]=c[i]
            powerSet(a,k,inp)


a=[0]*(chusCnt+1)