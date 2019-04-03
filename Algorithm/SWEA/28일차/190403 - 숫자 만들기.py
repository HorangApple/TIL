import sys
sys.stdin = open('input.txt','r')

d=['+','-','*','/']

def calc(a,b,cal):
    if cal=='+':
        return a+b
    elif cal=='-':
        return a-b
    elif cal=='*':
        return a*b
    elif cal=='/':
        return int(a/b)

def solution(k,total,cal):
    global mini,maxi
    if k==n:
        result.append(total)
    else:
        k+=1
        for i in range(4):
            if cal[i]==0:
                continue
            cal[i]-=1
            save=total
            total = calc(total,nums[k-1],d[i])
            solution(k,total,cal)
            total=save
            cal[i]+=1

TC = int(input())
for num in range(1,TC+1):
    n = int(input())
    cal = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    result=[]
    solution(1,nums[0],cal)
    print(f'#{num}',max(result)-min(result))