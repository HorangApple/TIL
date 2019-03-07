import sys
sys.stdin=open('input.txt','r')

T=int(input())
for num in range(1,T+1):
    n=int(input())
    food=[]
    result=[]
    inp=[list(map(int,input().split())) for _ in range(n)]
    for i in range(n-1):
        source=[]
        for j in range(i,n):
            forbbiden=[]
            if i==j:
                continue
            a=inp[i][j]+inp[j][i]
            for k in range(n-1):
                for g in range(i,n):
                    if k==g:
                        continue
                    if k!=i and g!=j and k!=j and k!=i:
                        b=inp[g][k]+inp[k][g]
                        print(a,b)
                        result.append(abs(a-b))

    print(result)
    mini=999
    for i in result:
        if mini>i:
            mini=i
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
# # 백준https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&
# # 14501 퇴사