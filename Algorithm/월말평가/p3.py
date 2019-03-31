import sys
sys.stdin = open('p3.txt','r')

dx = [0,1,0,-1]
dy = [1,0,-1,1]


def candidate(a,c):
    temp=[False]*n
    for i in a:
        temp[i]=True
    for i in range(n):
        if not temp[i]:
            c.append(i)

def solution(a,k):
    if k==n:
        cnt=0
        total=0
        for i in a:
            total+=abs(robot[i][0]-snack[cnt][0]) + abs(robot[i][1]-snack[cnt][1])
            cnt+=1
        result.append(total)
    else:
        k+=1
        c=[]
        candidate(a,c)

        for i in c:
            a.append(i)
            solution(a,k)
            a.pop()
            

T = int(input())
for num in range(1,T+1):
    n = int(input())
    snack=[]
    robot=[]
    inp = list(map(int,input().split()))
    for i in range(n):
        snack.append([inp[2*i],inp[2*i+1]])
    inp = list(map(int,input().split()))
    for i in range(n):
        robot.append([inp[2 * i], inp[2 * i + 1]])
    go=[]
    a=[]
    result=[]
    solution(a,0)
    print(f"#{num}",min(result))