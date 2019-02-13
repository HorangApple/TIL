import sys
sys.stdin = open("input.txt","r")

TC = int(input())

def stack(text):
    stack=[]
    top=-1
    for i in text:
        if i == '(' or i == ')'or i == '{'or i == '}':
            top+=1
            stack.append(i)
            if top-1>-1 :
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
