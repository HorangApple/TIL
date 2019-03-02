# import sys
# sys.stdin = open("input.txt","r")

TC = int(input())

# 20x20,20x10의 조합을 구함, 같은 요소가 있는 조합의 수학 공식 그대로 구현
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
    # 20x20으로 최대한 넣는 것을 시작으로 하나씩 줄어나감
    x=n//20
    cases=[]
    sum=0
    result=0
    while True:
        # 20x20,20x10의 경우의 수를 구함
        y=(n-20*x)//10 
        case=(x,y)
        cases.append(case)
        if x!=0:
            x-=1
        else:
            break
    # 20x20은 10x20를 2개로 쌓은 것과 같으므로 20x20의 수 만큼 2를 곱해야함
    for i in cases[:-1]:
        sum+=int(combi(i))*(2**i[0])
    result=sum+1
    return result

for i in range(TC) :
    n=int(input())
    print('#{} {}'.format(i+1,solution(n)))
