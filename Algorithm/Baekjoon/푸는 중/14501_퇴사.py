import sys
sys.stdin=open("input.txt","r")

def bi():
    for i in range(1,(1<<n)):
        part=[]
        for j in range(n):
            if i&(1<<j):
                part.append(j)
        if part!=[]:
            total=0
            days=0
            for k in part:
                if days==0:
                    days+=k
                if days==k:
                    total+=inp[days][1]
                    save=inp[days][1]
                    days+=inp[days][0]
                    if days>n+1:
                        total-=save
                        result.append(total)
                    else:
                        result.append(total)

n=int(input())

inp=[[] for _ in range(n)]
for j in range(n):
    inp[j]+=list(map(int,input().split()))
result=[]
bi()
print(result)
print(max(result))