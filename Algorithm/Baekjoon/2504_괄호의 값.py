# https://www.acmicpc.net/problem/2504
import sys
sys.stdin = open("input.txt","r")

#----------------------------

def check(i):
    global top
    stack.append(i)
    top+=1
    while True:
        if top==0 and (stack[top]==")"or stack[top]=="]"):
            return 0
        elif top>0 and stack[top]==")" and stack[top-1]=="[":
            return 0
        elif top>0 and stack[top]=="]" and stack[top-1]=="(":
            return 0
        elif top>0 and stack[top]==")" and stack[top-1]=="(":
            stack.pop()
            stack.pop()
            stack.append(2)
            top-=1
        elif top>0 and stack[top]=="]" and stack[top-1]=="[":
            stack.pop()
            stack.pop()
            stack.append(3)
            top-=1
        elif top>0 and (str(stack[top]) not in "[]()") and (str(stack[top-1])  not in "[]()"):
            a=stack.pop()
            b=stack.pop()
            stack.append(a+b)
            top-=1
        elif top>1 and stack[top]=="]" and stack[top-2]=="[" and (str(stack[top-1])  not in "[]()"):
            stack.pop()
            a=stack.pop()
            stack.pop()
            stack.append(a*3)
            top-=2
        elif top>1 and stack[top]==")" and stack[top-2]=="(" and (str(stack[top-1])  not in "[]()"):
            stack.pop()
            a=stack.pop()
            stack.pop()
            stack.append(a*2)
            top-=2
        else:
            return 1

TC=1
for _ in range(TC):
    stack=[]
    top=-1
    for i in input():
        a=check(i)
        if a=='0':
            break
    if a=='0'or len(stack)>1:
        print(0)
    elif len(stack)==1:
        print(stack[0])
#----------------------------
