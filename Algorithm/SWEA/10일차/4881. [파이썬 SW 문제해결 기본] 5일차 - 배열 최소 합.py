import sys
sys.stdin = open("input.txt","r")

# backtracking을 이용한 순열
def backtrack(a,k,inp,result,check):
    c=[0]*(inp+1)
    # 최종 깊이까지 도달, 최소합 도출
    if k==inp:
        total=0
        for i in range(inp):
            total+=mp[i][result[i+1]-1]
            if total>mini[0]:
                break
        else:
            mini[0]=total
    # 최종 깊이가 아니면 진행
    else:
        k+=1
        construct_candidates(a,k,inp,c)
        for i in range(1,inp+1):
            if c[i]>0:
                result[k]=c[i]
                check+=mp[k-1][result[k]-1]
                # 현재의 최소 합보다 합이 더 커지면 가지치기
                if check>mini[0]:
                    check-=mp[k-1][c[i]-1]
                    continue
                # 해당 a[i]는 사용했으니 0으로 초기화
                a[i]=0
                backtrack(a,k,inp,result,check)
                # 다른 후보군을 재귀에 돌리기 위해 다시 원상 복구
                a[i]=c[i]
                check-=mp[k-1][c[i]-1]
# 후보군 생성
def construct_candidates(a,k,inp,c):
    for i in range(1,inp+1):
        # 사용하지 않은 a[i]를 골라 후보군에 추가
        if a[i]>0:
            c[a[i]]=a[i]


tc=int(input())
for num in range(1,tc+1):
    length=int(input())
    mp=[list(map(int,input().split())) for _ in range(length)]
    result=[0]*(length+1)
    a=list(range(length+1)) # 열의 index 사용여부를 나타냄
    mini=[999999999999999999999999999]
    backtrack(a,0,length,result,0)
    print(f'#{num} {mini[0]}')
