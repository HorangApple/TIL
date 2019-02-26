import sys
sys.stdin = open("input.txt","r")

def solution(n,m,chi):
    pizzaQ=[]
    fireQ=[]
    cnt=0
    for i in range(1,m+1):
        pizzaQ.append([i,chi[i-1]])
    for i in range(n):
        fireQ.append(pizzaQ.pop(0))
    while True:
        for i in range(n):
            if fireQ[i]!=[]:
                fireQ[i][1]//=2
                if fireQ[i][1]==0:
                    if len(pizzaQ):
                        fireQ[i]=pizzaQ.pop(0)
                    else:
                        onePizza=fireQ[i]
                        fireQ[i]=[]
                        cnt+=1
        if cnt==n :
            return onePizza[0]
TC=int(input())
for num in range(1,TC+1):
    n,m=map(int,input().split())
    chi=list(map(int,input().split()))

    print(f'#{num} {solution(n,m,chi)}')