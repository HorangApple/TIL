import sys
sys.stdin = open('input.txt','r')

# Hoare-Partition 알고리즘
def partition1(a,l,r):
    p=a[l]
    i,j = l,r
    while i<j:
        while i<len(a) and a[i] <= p: i+=1
        while j>l and a[j] >= p: j-=1
        if i < j : a[i],a[j] = a[j],a[i]
    
    a[l],a[j] = a[j],a[l]
    return j

# Lomuto partition 알고리즘
def partition2(a,p,r):
    x=a[r]
    i=p-1
    for j in range(p,r):
        if a[j]<=x:
            i+=1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[r] = a[r],a[i+1]
    return i+1

def quick(a,l,r):
    if l<r:
        s=partition1(a,l,r)
        quick(a,l,s-1)
        quick(a,s+1,r)

TC = int(input())
for _ in range(1,TC+1):
    a = list(map(int, input().split()))
    quick(a,0,len(a)-1)
    print(a)
