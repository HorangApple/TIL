# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&
import sys
sys.stdin=open('input.txt','r')

def process(n):
    global mini
    for i in range(1,(1<<n)):
        a = []
        b = []
        cnt = 0
        for k in range(n):
            if i & (1 << k):
                cnt += 1
        if cnt == n // 2:
            for j in range(n):
                if i & (1 << j):
                    a.append(source[j])
                else:
                    b.append(source[j])
            length=len(a)
            av=0
            bv=0
            for i in range(length):
                for j in range(length):
                    if i!=j:
                        av+=inp[a[i]][a[j]]
                        bv+=inp[b[i]][b[j]]
            value=abs(av-bv)
            if mini>value:
                mini=value
        elif cnt>n//2:
            continue
 
T=int(input())
for num in range(1,T+1):
    n=int(input())
    inp=[list(map(int,input().split())) for _ in range(n)]
    source=list(range(0,n))
    mini=99999
    process(n)
    print("#{} {}".format(num,mini))

# N= 10
# for subset in (1,(1<<N)):
#     cnt=0
#     for i in range(N):
#         if subset & (1<<i):
#             cnt+=1
        
#     if cnt==N//2:
#         a,b=[],[]
#         for i in range(N):
#             if subset & (1<<i):a.append(i)
#             else:b.append(i)
#             print(a,b)

# # 백준
# # 14501 퇴사

# 보윤 코드
T = int(input()) # 테스트케이스
for tc in range(T):
    N = int(input()) # 식재료의 수
    sinerge = []
    for _ in range(N):
        sinerge.append(list(map(int, input().split())))
    Ns = list(range(N))
    
    minvalue = 20000

    
    for i in range(1 << N):
        tempB = []
        tempA = []
        for j in range(N):
            if i & (1 << j):
                tempB.append(Ns[j])
            else: # 0에 해당하는 부분 넣기
                tempA.append(Ns[j])
        # j와 다 비교를 해서 넣었을 때,
        # 개수가 N//2개여야함
        if len(tempB) == N//2:
            tasteA = tasteB = 0
            for i2 in range(N//2):
                for j2 in range(N//2):
                    if i2 == j2:
                        continue
                    tasteA += sinerge[tempA[i2]][tempA[j2]]
                    tasteB += sinerge[tempB[i2]][tempB[j2]]

            if abs(tasteA - tasteB) < minvalue:
                minvalue = abs(tasteA - tasteB)

    print("#%d %d" %(tc+1, minvalue))