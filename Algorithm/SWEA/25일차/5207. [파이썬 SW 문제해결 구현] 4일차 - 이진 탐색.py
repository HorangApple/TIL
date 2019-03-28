import sys
sys.stdin = open('input.txt','r')

def search(v,l,r,arr):
    global cnt, mode
    while True:
        m=(l+r)//2
        if arr[m] == v:
            cnt+=1
            return
        if v>arr[m]:
            if mode>1:
                return
            l=m+1
            mode=2
        elif v<arr[m]:
            if mode<-1:
                return
            r=m-1
            mode=-2
        elif v==arr[m]:
            cnt+=1
            return

TC = int(input())
for num in range(1,TC+1):
    n,m = map(int,input().split())
    arrN = sorted(list(map(int,input().split())))
    arrM = sorted(list(map(int,input().split())))
    cnt=0
    lengthN = len(arrN)

    for i in arrM:
        mode=0
        search(i,0,lengthN-1,arrN)
    print(f'#{num}',cnt)


