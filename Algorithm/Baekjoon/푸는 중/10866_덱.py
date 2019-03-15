import sys
sys.stdin=open("input.txt","r")

def push_front(n):
    que.insert(0,n)

def push_back(n):
    que.append(n)

def pop_front():
    if len(que)==0:
        return -1
    else:
        return que.pop(0)

def pop_back():
    if len(que)==0:
        return -1
    else:
        return que.pop()

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
    else:
        return que[0]

def back():
    if len(que)==0:
        return -1
    else:
        return que[-1]

que=[]

TC=int(input())
for _ in range(TC):
    inp=list(input().split())
    if inp[0]=='push_back':
        push_back(int(inp[1]))
    elif inp[0]=='push_front':
        push_front(int(inp[1]))
    elif inp[0]=='front':
        print(front())
    elif inp[0]=='back':
        print(back())
    elif inp[0]=='pop_front':
        print(pop_front())
    elif inp[0]=='pop_back':
        print(pop_back())
    elif inp[0]=='empty':
        print(empty())
    elif inp[0]=='size':
        print(size())