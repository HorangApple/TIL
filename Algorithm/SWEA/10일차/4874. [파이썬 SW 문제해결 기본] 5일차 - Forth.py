import sys
sys.stdin = open("input.txt","r")

TC=int(input())
# 사칙연산 수행
def calcul(cal,top):
    if len(stack)<2:
        return -1
    b=stack.pop()
    a=stack.pop()
    caldict={'+':a+b,'-':a-b,'/':int(a/b),'*':a*b}
    stack.append(caldict[cal])
    top-=1
    return top

for num in range(1,TC+1):
    inp=input().split()
    stack=[]
    top=-1
    for i in inp[:-1]:
        # 연산자이면 계산 수행
        if i in ['+','-','*','/']:
            top=calcul(i,top)
        # 숫자이면 stack에 저장     
        else:
            stack.append(int(i))
            top+=1
    # 스텍에 계산 결과만 남아 있으면 pop
    if top==0:
        print(f'#{num} {stack.pop()}')
    # 스텍에 1개 이상 남아 있으면 error
    else:
        print(f'#{num} error')