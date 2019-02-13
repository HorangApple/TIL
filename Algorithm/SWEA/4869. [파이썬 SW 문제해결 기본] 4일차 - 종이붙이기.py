import sys
sys.stdin = open("input.txt","r")

TC = int(input())

def combi(case):
    x,y=case
    result1=1
    result2=1
    result3=1
    for i in range(1,x+y+1):
        result1*=i
    for i in range(1,y+1):
        result2*=i
    for i in range(1,x+1):
        result3*=i
    result=result1/(result2*result3)
    return result

def solution (n):
    x=n//20
    cases=[]
    sum=0
    result=0
    while True:
        y=(n-20*x)//10 
        case=(x,y)
        cases.append(case)
        if x!=0:
            x-=1
        else:
            break
    for i in cases[:-1]:
        sum+=int(combi(i))*(2**i[0])
    result=sum+1
    return result

for i in range(TC) :
    n=int(input())
    print('#{} {}'.format(i+1,solution(n)))
