import sys
sys.stdin = open('input.txt','r')

def candidate(a,n,k):
    c=[False]*(n+1)
    for i in a[1:]:
        if i>0:
            c[i]=True
    return c

def solution(a,n,k,total):
    global MAX
    if n==k:
        if MAX<total:
            MAX=total
    else:
        k+=1
        candi = candidate(a,n,k)
        for i in range(1,n+1):
            if not candi[i]:
                a[k]=i
                save = total
                total*=inp[k-1][i-1]/100
                if MAX<total:
                    solution(a,n,k,total)
                total = save
                a[k]=0

TC = int(input())
for num in range(1,TC+1):
    n = int(input())
    inp = [list(map(float,input().split())) for _ in range(n)]
    a=[0]*(n+1)
    total=1
    MAX=-1
    solution(a,n,0,total)
    print(f'#{num} {round(MAX*100,6):0.6f}')

    # input의 중간에 0이 있으면 모든 계산이 무용지물이므로 맨 앞으로 당겨서 먼저 계산하도록 처리한다.


# 보윤이 코드
def findProb(curprob, n): # n번째 사람
    global N, maxvalue
    if curprob == 0:
        return # 그런 경우는 버려도 될 듯
    if n == N: # 0, 1, 2면 3이 되는 순간 출력하기
        if maxvalue < curprob:
            maxvalue = curprob
        return
    for i in range(N):
        if used[i]: continue
        arr[n] = i # 그 사람이 이 일을 선택하고
        used[i] = True
        if curprob*0.01*(jobs[n][i]) >= maxvalue: # 이미 작으면 다음에는 더 작아질 수 밖에 없다.
            findProb(curprob*0.01*(jobs[n][i]), n+1) # 내 다음 사람을 넘겨줌...
        used[i] = False
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    jobs = []
    for _ in range(N):
        jobs.append(list(map(int, input().split())))
    arr = [0]*N # 각각 몇 번째 일 하는지 저장
    used = [False]*N # 순열이 사용되었는지 알아야함
    maxvalue = 0
    for start in range(N): # 몇 번째 일인지 돌면서
        arr[0] = start
        used[start]=True
        findProb(jobs[0][start]*0.01, 1) # 0번째 사람부터 시작
        used[start]=False
 
    print("#%d %.6f" %(tc, round(maxvalue*100, 6)))