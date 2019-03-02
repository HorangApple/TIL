import sys
sys.stdin = open("input.txt","r")

TC = int(input())

def stack(text):
    stack=[]
    top=-1
    for i in text:
        # 괄호만 stack에 저장
        if i == '(' or i == ')'or i == '{'or i == '}':
            top+=1
            stack.append(i)
            if top-1>-1 :
                # 괄호 짝이 맞으면 stack을 두 번 pop
                if (stack[top]==")" and stack[top-1]=="(") or (stack[top]=="}" and stack[top-1]=="{") :
                    stack.pop()
                    stack.pop()
                    top-=2
    if top==-1 :
        return 1
    else :
        return 0


for i in range(TC) :
    n=input()
    print('#{} {}'.format(i+1,stack(n)))
