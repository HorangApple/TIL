# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&
import sys
sys.stdin=open('input.txt','r')

def process(n):
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
            aSo.append(a)
            bSo.append(b)
        elif cnt>n//2:
            continue

T=int(input())
for num in range(1,T+1):
    n=int(input())
    inp=[list(map(int,input().split())) for _ in range(n)]
    source=list(range(0,n))
    aSo=[]
    bSo=[]
    result=[]
    process(n)
    for aS, bS in zip(aSo,bSo):
        a = 0
        b = 0
        for i in aS:
            for j in aS:
                if i!=j:
                    a+=inp[i][j]
        for i in bS:
            for j in bS:
                if i!=j:
                    b+=inp[i][j]
        result.append(abs(a-b))
    print("#{} {}".format(num,min(result)))

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

