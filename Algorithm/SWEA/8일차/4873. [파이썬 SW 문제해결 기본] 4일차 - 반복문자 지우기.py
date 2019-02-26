import sys
sys.stdin = open("input.txt","r")

TC = int(input())

def stack(text):
    stack=[]
    top=-1
    for i in text:
        top+=1
        stack.append(i)
        if top-1>-1 :
            if (stack[top]==stack[top-1]) :
                stack.pop()
                stack.pop()
                top-=2
    return stack


for i in range(TC) :
    n=input()
    print('#{} {}'.format(i+1,len(stack(n))))
