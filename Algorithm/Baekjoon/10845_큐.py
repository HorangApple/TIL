import sys
sys.stdin = open("input.txt","r")

def push(x):
    que.append(x)

def pop():
    if len(que)==0:
        return -1
    return que.pop(0)

def size():
    return len(que)

def empty():
    if len(que)==0:
        return 1
    else:
        return 0

def front():
    if len(que)==0:
        return -1
    return que[0]

def back():
    if len(que)==0:
        return -1
    return que[-1]

que = []
TC=int(input())
for _ in range(TC):
    od=[]
    od=input().split()
    if od[0]=="push":
        push(od[1])
    elif od[0]=="pop":
        print(pop())
    elif od[0]=="size":
        print(size())
    elif od[0]=="empty":
        print(empty())
    elif od[0]=="front":
        print(front())
    elif od[0]=="back":
        print(back())