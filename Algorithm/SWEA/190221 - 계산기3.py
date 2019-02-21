import sys
sys.stdin = open("input.txt","r")

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
    isp={'(':0,'+':1,'*':2}
    icp={'(':3,'+':1,'*':2}
    oper=['(',')','+','*']
    operStack=[]
    equation=input()
    for i in equation:
        if i in oper:
            if i==')':
                while operStack[-1]!='(':
                    inp=operStack.pop()
                    stack.append(inp)
                operStack.pop()
            elif len(operStack)==0 or icp[i]>isp[operStack[-1]]:
                operStack.append(i)
            else:
                inp=operStack.pop()
                operStack.append(i)
                stack.append(inp)
        else:
            stack.append(i)
    print(f'#{num} {cal(stack)[0]}')