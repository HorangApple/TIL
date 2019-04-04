import sys
sys.stdin = open('input.txt','r')

from copy import deepcopy
def go(k,lenght,arr):
    if k==lenght:
        orders.append(arr)
    else:
        k+=1
        for i in range(2):
            go(k,lenght,arr+[i])

def solution():
    global mini
    for order in orders:
        people=deepcopy(save)
        people1=[]
        people2=[]
        time=0
        i=0
        while i<lenght:
            if order[i] ==0:
                people1+=[people[i]]
            else:
                people2+=[people[i]]
            i+=1
        people1=sorted(people1,key=lambda x:x[2])
        people2=sorted(people2,key=lambda x:x[3])
        
        stair1Cnt,stair2Cnt=0,0
        stair1People,stair2People=[],[]
        while len(people1) or len(people2) or len(stair1People) or len(stair2People):
            if mini<time:
                break
            time+=1
            delete=[]
            i=0
            # 첫 번째 계단
            while i<len(people1):
                people1[i][2]-=1
                if people1[i][2]<-1 and stair1Cnt<3:
                    stair1Cnt+=1
                    people1[i][2]=stairs[0][-1]
                    stair1People+=[people1[i]]
                    delete+=[i]
                i+=1
            else:
                for idx in delete[::-1]:
                    people1.pop(idx)
            i=0
            delete=[]
            while i<len(stair1People):
                stair1People[i][2]-=1
                if stair1People[i][2]==0:
                    delete+=[i]
                i+=1
            else:
                for idx in delete[::-1]:
                    stair1People.pop(idx)
                    stair1Cnt-=1

            delete=[]
            i=0
            # 두 번째 계단
            while i<len(people2):
                people2[i][3]-=1
                if people2[i][3]<-1 and stair2Cnt<3:
                    stair2Cnt+=1
                    people2[i][3]=stairs[1][-1]
                    stair2People+=[people2[i]]
                    delete+=[i]
                i+=1
            else:
                for idx in delete[::-1]:
                    people2.pop(idx)
            i=0
            delete=[]
            while i<len(stair2People):
                stair2People[i][3]-=1
                if stair2People[i][3]==0:
                    delete+=[i]
                i+=1
            else:
                for idx in delete[::-1]:
                    stair2People.pop(idx)
                    stair2Cnt-=1
        mini=min(mini,time)


TC = int(input())
for num in range(1,TC+1):
    n = int(input())
    mp=[list(map(int,input().split())) for _ in range(n)]
    stairs = []
    people = []
    orders = []
    mini=9999
    for i in range(n):
        for j in range(n):
            if mp[i][j]==1:
                people.append([i,j])
            elif mp[i][j]>1:
                stairs.append([i,j,mp[i][j]])
    lenght=len(people)
    go(0,lenght,[])
    i=0
    while i<len(people):
        for j in stairs:
            time=abs(people[i][0]-j[0]) + abs(people[i][1]-j[1])
            people[i]+=[time]
        i+=1
    save=deepcopy(people)
    solution()
    print(f'#{num}',mini)