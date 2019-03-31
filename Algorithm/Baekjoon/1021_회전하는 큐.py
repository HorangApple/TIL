import sys
sys.stdin=open('input.txt','r')

## 리스트 큐 구현
# def left():
#     que.append(que.pop(0))

# def right():
#     que.insert(0,que.pop())

# n,m=map(int,input().split())
# inp=list(map(int,input().split()))
# que=list(range(1,n+1))
# start=que[:]

# cnt=0
# for i in inp:
#     while True:
#         if i==que[0]:
#             que.pop(0)
#             break
#         elif que.index(i)>len(que)//2:
#             while i!=que[0]:
#                 right()
#                 cnt+=1
#         else:
#             while i!=que[0]:
#                 left()
#                 cnt+=1
# print(cnt)

# 링크드 리스트 큐 구현
class Node:
    def __init__(self,front,rear,value):
        self.front=front
        self.rear=rear
        self.value=value

class Que:
    def __init__(self):
        self.head=Node(None,None,0)
        self.length=0
    
    def enquefirst(self,n):
        node=Node(self.head,self.head,n)
        self.head.front=node
        self.head.rear=node
        self.length+=1

    def enqueFront(self,n):
        node=Node(self.head,self.head.front,n)
        f=self.head.front
        f.front=node
        self.head.front=node
        self.length+=1

    def enqueRear(self,n):
        node=Node(self.head.rear,self.head,n)
        r=self.head.rear
        r.rear=node
        self.head.rear=node
        self.length+=1
        
    def deque(self):
        node=self.head.front
        r=node.rear
        self.head.front=r
        r.front=self.head
        self.length-=1
        return node.value

    def shiftLeft(self):
        f=self.head.front
        f2=f.rear
        r=self.head.rear

        self.head.front=f2
        f2.front=self.head
        self.head.rear=f
        f.rear=self.head
        r.rear=f
        f.front=r

    def shiftRight(self):
        r=self.head.rear
        r2=r.front
        f=self.head.front
        
        self.head.rear=r2
        r2.rear=self.head
        self.head.front=r
        r.front=self.head
        f.front=r
        r.rear=f

    def searchQue(self,n):
        cnt=0
        start=self.head.front
        end=self.head
        while start!=end:
            if start.value==n:
                return cnt
            cnt+=1
            start=start.rear

    def frontValue(self):
        f=self.head.front
        return f.value

n,m=map(int,input().split())
inp=list(map(int,input().split()))
que=Que()
que.enquefirst(1)
for i in range(2,n+1):
    que.enqueRear(i)

cnt=0
for i in inp:
    if i==que.frontValue():
        que.deque()
    elif que.searchQue(i)>que.length//2:
        while i!=que.frontValue():
            que.shiftRight()
            cnt+=1
        que.deque()
    else:
        while i!=que.frontValue():
            que.shiftLeft()
            cnt+=1
        que.deque()
print(cnt)