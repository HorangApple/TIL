import sys
sys.stdin = open('input.txt','r')

def make_set(x):
    p[x]=x

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    p[find_set(y)]=find_set(x)

T=int(input())
for num in range(1,1+T):
    # 7 4
    n,m = map(int,input().split())
    # 2 3 4 5 4 6 7 4
    inp = list(map(int,input().split()))
    p = [0]*(n+1)
    # 하나씩 집합 생성
    for i in range(1,n+1):
        make_set(i)
    # 선 잇기
    for i in range(len(inp)//2):
        union(inp[i*2],inp[i*2+1])
    # 경로 압축
    # p=[0, 1, 2, 2, 7, 4, 4, 7]
    for i in range(1,n+1):
        p[i]=find_set(i)
    # p=[0, 1, 2, 2, 7, 7, 7, 7]
    print(f'#{num}',len(set(p[1:])))
    

