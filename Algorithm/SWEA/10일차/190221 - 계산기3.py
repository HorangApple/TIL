import sys
sys.stdin = open("input.txt","r")

# 계산 함수
def cal(stack):
    calStack=[]
    for i in stack:
        if i=='+':
            b=calStack.pop()
            a=calStack.pop()
            calStack.append(int(a)+int(b))
        elif i=='*':
            b=calStack.pop()
            a=calStack.pop()
            calStack.append(int(a)*int(b))
        else:
            calStack.append(i)
    return calStack

for num in range(1,11):
    length=int(input())
    stack=[]
    # stack 내의 우선순위(isp)와 외부에서의 우선순위(icp)를 정의함
    isp={'(':0,'+':1,'*':2}
    icp={'(':3,'+':1,'*':2}
    oper=['(',')','+','*']
    operStack=[]
    equation=input()
    for i in equation:
        # i가 연산자이면
        if i in oper:
            # 닫는 괄호면 여는 괄호가 나올 때까지 pop
            if i==')':
                while operStack[-1]!='(':
                    inp=operStack.pop()
                    stack.append(inp)
                operStack.pop()
            # 연산자 스택이 비어있거나 icp가 isp보다 크면 연산자 스택에 추가
            elif len(operStack)==0 or icp[i]>isp[operStack[-1]]:
                operStack.append(i)
            # 그 외의 경우에는 기존에 있는 것을 빼서 숫자가 있는 스택에 추가,
            # 새로 들어온 연산자를 연산자 스택에 추가
            else:
                inp=operStack.pop()
                operStack.append(i)
                stack.append(inp)
        # 연산자가 아닌 숫자면 스택에 추가
        else:
            stack.append(i)
    print(f'#{num} {cal(stack)[0]}')