import sys
sys.stdin = open("input.txt","r")

def solution(n,m,chi):
    pizzaQ=[] # 피자 큐
    fireQ=[] # 화덕 큐
    cnt=0 # 조리 완료된 피자 수
    # 입력 받은 값들로 피자번호, 치즈 순으로 리스트 만들어 채워 놓는다
    for i in range(1,m+1):
        pizzaQ.append([i,chi[i-1]])
    # 화덕 수 만큼 피자 초기 셋팅을 한다
    for i in range(n):
        fireQ.append(pizzaQ.pop(0))
    # ★화덕
    while True:
        # 화덕 크기만큼 회전한다
        for i in range(n):
            if fireQ[i]!=[]:
                # 치즈 녹이기
                fireQ[i][1]//=2
                # 치즈가 다 녹으면
                if fireQ[i][1]==0:
                    # 남은 피자에서 채우거나
                    if len(pizzaQ):
                        fireQ[i]=pizzaQ.pop(0)
                    # 남은 피자가 없으면 []로 채운다    
                    else:
                        onePizza=fireQ[i]
                        fireQ[i]=[]
                        cnt+=1
        # 가지고 있는 피자들이 다 나가면 마지막 피자의 번호를 리턴한다           
        if cnt==n :
            return onePizza[0]
TC=int(input())
for num in range(1,TC+1):
    n,m=map(int,input().split())
    chi=list(map(int,input().split()))

    print(f'#{num} {solution(n,m,chi)}')