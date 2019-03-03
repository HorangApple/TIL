# https://www.acmicpc.net/problem/10828
import sys
sys.stdin = open("input.txt","r")

#----------------------------
stack=[]
top=-1
def push(num):
    global top
    stack.append(num)
    top+=1

def pop():
    global top
    if top==-1:
        print(-1)
    else:
        val=stack.pop()
        top-=1
        print(val)

def size():
    print(len(stack))

def empty():
    if stack:
        print(0)
    else:
        print(1)

def top_():
    global top
    if stack:
        print(stack[top])
    else:
        print(-1)

TC=int(input())
for _ in range(TC):
    od=[]
    od=input().split()
    if od[0]=="push":
        push(od[1])
    elif od[0]=="pop":
        pop()
    elif od[0]=="size":
        size()
    elif od[0]=="empty":
        empty()
    elif od[0]=="top":
        top_()
#----------------------------
