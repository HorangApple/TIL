# https://www.acmicpc.net/problem/9012
import sys
sys.stdin = open("input.txt","r")

#----------------------------

def check(i):
    global top
    stack.append(i)
    top+=1
    if top>0 and stack[top]==")" and stack[top-1]=="(":
        stack.pop()
        stack.pop()
        top-=2
        

TC=int(input())
for _ in range(TC):
    stack=[]
    top=-1
    for i in input():
        check(i)

    if len(stack)==0:
        print("YES")
    else :
        print("NO")
#----------------------------
