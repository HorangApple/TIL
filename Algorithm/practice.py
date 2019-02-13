import sys
sys.stdin = open("input.txt","r")

n, k = map(int,input().split())
stack=[]
visited=[]
cal=[-1,1,2]

def nextposition(arr,visited):
    for i in arr:
        if i not in visited and i>0:
            return i
    else :
        return False


def dfs(n,k):
    x=n
    count = 0
    while x != k :
        if k-x>x:
            x*=2
            count+=1
        else : 
            x+=1
            count+=1
        if x>k:
            x-=1
            count+=1
    return count
print(dfs(n,k))