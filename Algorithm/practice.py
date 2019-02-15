import sys
sys.stdin = open("input2.txt","r")

def endsearch(arr):
    count = 1
    endlist=[]
    for i in arr[1:]:
        result = sum(i)
        if result == 0:
            endlist.append(count)
        count+=1
    return endlist

def backsearch(arr,s):
    for i in range(v+1):
        if i not in visited:
            back=arr[i][s]
            if back>0:
                return i
    return False

def terminator (arr,v):
    start=v
    while arr[start] != []:
        v=start
        back = backsearch(arr,v)
        while back :
            back = backsearch(arr,v)
            if back !=False :
                v=back
        arr[v].clear()
        visited.append(v)

TC = 10
for t in range(TC) :
    v,e=map(int,input().split())  
    line=list(map(int,input().split()))
    visited = []
    arr=[[0 for _ in range(v+1)] for _ in range(v+1)]
    for i in range(e) :
        x=line[i*2]
        y=line[i*2+1]
        arr[x][y]=y
    endlist=endsearch(arr)
    for i in endlist:
        terminator(arr,i)
    print(f'#{t+1}',end=" ")
    for i in visited:
        print(f'{i}',end=" ")
    print("")