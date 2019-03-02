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
            # 같은 문자가 2개 연속으로 쌓여 있으면 2번 pop
            if (stack[top]==stack[top-1]) :
                stack.pop()
                stack.pop()
                top-=2
    return stack


for i in range(TC) :
    n=input()
    print('#{} {}'.format(i+1,len(stack(n))))
