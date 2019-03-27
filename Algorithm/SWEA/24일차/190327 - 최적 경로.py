import sys
sys.stdin = open('input.txt','r')

def search(x,y,visited):
    c = []
    for i in range(n):
        if i not in visited:
            c.append(i)
    return c


def solution(visited,n,k,p,total):
    global MINI
    if n==k:
        lastP = visited[-1]
        total+=(abs(house[0]-point[lastP][0])+abs(house[1]-point[lastP][1]))
        if total<MINI:
            MINI=total
    else:
        k+=1
        candi = search(p[1],p[0],visited)
        for i in candi:
            visited.append(i)
            val=(abs(p[0]-point[i][0])+abs(p[1]-point[i][1]))
            total+=val
            if total<=MINI: 
                solution(visited,n,k,point[i],total)
            total-=val
            visited.pop()

TC = int(input())
for num in range(1,TC+1):
    n = int(input())
    inp=list(map(int,input().split()))
    point=[]
    visited=[]
    total=0
    MINI = 99999
    office, house = [inp[0],inp[1]],[inp[2],inp[3]]
    for i in range(2,n+2):
        point.append([inp[2*i],inp[2*i+1]])
    solution(visited,n,0,office,total)
    print(f'#{num}', MINI)