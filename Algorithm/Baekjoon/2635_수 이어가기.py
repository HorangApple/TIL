import sys
sys.stdin = open("input.txt","r")

def solution(n,result):
    global maxLength
    result.append(n)
    for i in range(1,n+1):
        result.append(i)
        a=result[-2]-result[-1]
        while a>=0:
            result.append(a)
            a = result[-2]-result[-1]
        if len(result)>maxLength:
            maxLength=len(result)
            maxList=result
        result=[n]
    return maxList

n=int(input())
maxLength=0
maxList=[]
result=[]
maxList=solution(n,result)
print(maxLength)
for i in maxList:
    print(str(i),end=" ")
print()