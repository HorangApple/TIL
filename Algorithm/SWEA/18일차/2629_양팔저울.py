import sys
sys.stdin = open("input.txt","r")

chusCnt=int(input())
chus=list(map(int, input().split()))
marblesCnt=int(input())
marbles=list(map(int, input().split()))

def candi(a,c):
    temp=[False]*40000
    idx=1
    for i in a[1:]:
        if i >0:
            temp[i]=True
    for i in chus:
        if not temp[i]:
            c.append(i)
    return len(c)

def powerSet(a,k,inp,marble):
    global result
    if k==inp:
        return
    else:
        c = []
        ncan=candi(a,c)
        k+=1
        print(c,k)
        l = marble + sum(a)
        r = sum(c)
        # print(l,r)
        if l == r:
            result.append("Y")
            return
        elif l > r:
            return
        for i in range(ncan):
            a[k]=c[i]
            powerSet(a,k,inp,marble)

for i in marbles:
    result=[]
    a=[0]*(chusCnt+1)
    powerSet(a, 0, chusCnt,i)
    for i in result:
        if i =="Y":
            print(i,end=" ")
            break
    else:
        print("N",end=" ")
print()