'''
그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.

0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때, 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.

다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다. 

1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
 
'''
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

def kr():
    a = 0
    for i in range(n+1):
        make_set(i)
    
    for i in inp:
        if find_set(i[0]) != find_set(i[1]):
            a+=i[2]
            union(i[0],i[1])
    return a

def mySort(l,r):
    i,j=0,0
    result=[]
    while i<len(l) and j<len(r):
        if l[i][2]>r[j][2]:
            result.append(r[j])
            j+=1
        else:
            result.append(l[i])
            i+=1
    while i<len(l):
        result.append(l[i])
        i+=1
    while j<len(r):
        result.append(r[j])
        j+=1
    return result

def merge(v):
    if len(v)==1:
        return v
    half=len(v)//2
    l=merge(v[:half])
    r=merge(v[half:])
    return mySort(l,r)

T=int(input())
for num in range(1,1+T):
    n,m = map(int,input().split())
    inp = [list(map(int,input().split())) for _ in range(m)]
    p = [0]*(n+1)
    inp = merge(inp)
    print(f'#{num}',kr())