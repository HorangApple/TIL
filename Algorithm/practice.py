import sys
sys.stdin = open('input.txt', 'r')

import copy
def archer(k,a):
    if k==3:
        for i in cases:
            if set(i)==set(a):
                return
        cases.append(a)
    else:
        k+=1
        for i in range(m):
            if i not in a:
                archer(k,a+[i])

def serch(case,stage):
    for i in range(n-1-stage,n-1-d-stage,-1):
        for j in range(m):
            if mp[i][j]>0:
                one=[i,j]
                for k in case:
                    one+=[abs(i-n+stage)+abs(j-k)]
                enemy.append(one)

def attack(enemy):
    global killCnt
    archer=[[] for _ in range(3)]
    for i in enemy:
        for j in range(2,5):
            if i[j]<=d:
                if archer[j-2]==[]:
                    archer[j-2]=i
                elif (archer[j-2][1]>i[1] and archer[j-2][j]==i[j]) or archer[j-2][j]>i[j]:
                    archer[j-2]=i

    for i in archer:
        if i!=[] and mp[i[0]][i[1]]>0:
            mp[i[0]][i[1]]=0
            killCnt+=1

# T=int(input())
# for i in range(T):
n,m,d=map(int,input().split())
mp=[list(map(int,input().split())) for _ in range(n)]
save=copy.deepcopy(mp)
cases=[]
archer(0,[])
maxi=0
for case in cases[0:1]:
    mp=copy.deepcopy(save)
    k=0
    killCnt=0
    while k<n:
        if killCnt+(n-k)*3<maxi:
            break
        enemy=[]
        serch(case,k)
        print(enemy)
        attack(enemy)
        # print(k,case)
        # for i in mp:
        #     print(i)
        # print()
        k+=1
    # print(killCnt)
    maxi=max(maxi,killCnt)
print(maxi)