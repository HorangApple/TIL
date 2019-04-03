import sys
sys.stdin = open('input.txt','r')

def solution(k,val,idx):
    global maxi
    if 0<idx<lenght:
        if int(val[idx-1])<max(map(int,list(val[idx:]))):
            return
    if k==n:
        maxi=max(maxi,int(val))
    else:
        k+=1
        if idx<lenght:
            for j in range(idx+1,lenght):
                if val[idx]!=val[j]:
                    save=val
                    val=val[:idx]+val[j]+val[idx+1:j]+val[idx]+val[j+1:]
                    solution(k,val,idx+1)
                    val=save
                else:
                    solution(k,val,idx+1)
            else:
                solution(k-1,val,idx+1)
        else:
            val=val[:-2]+val[-1]+val[-2]
            solution(k,val,idx)

TC = int(input())
for num in range(1,TC+1):
    val,n = map(int,input().split())
    lenght = len(str(val))
    numCnt = len(set(str(val)))
    maxi=0
    solution(0,str(val),0)
    print(f'#{num}',maxi)