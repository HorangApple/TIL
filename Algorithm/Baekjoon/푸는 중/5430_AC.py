import sys
sys.stdin=open('input.txt','r')

print('#1')
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
        self.lastNode=node
        self.length+=1

    def enqueRear(self,n):
        node=Node(self.lastNode,self.head,n)
        self.lastNode.rear=node
        self.head.front=node
        self.lastNode=node
        self.length+=1
        
    def dequeFront(self):
        if self.length==0 or n==0:
            return 'error'
        node=self.head.front
        f=node.front
        self.head.front=f
        f.rear=self.head
        self.length-=1
        return True
        
    def dequeRear(self):
        if self.length==0 or n==0:
            return False
        node=self.head.rear
        r=node.rear
        self.head.rear=r
        r.front=self.head
        self.length-=1
        return True
    
    def printQue(self):
        start=self.head.rear
        end=self.head
        while start!=end:
            result.append(start.value)
            start=start.rear
    
    def printQueR(self):
        start=self.head.front
        end=self.head
        while start!=end:
            result.append(start.value)
            start=start.front


TC=int(input())
for _ in range(TC):
    order=input()
    n=int(input())
    inp=list(input()[1:-1].split(','))
    result=[]
    que=Que()
    que.enquefirst(inp[0])
    for i in inp[1:]:
        que.enqueRear(i)
        

    mode=1
    for i in order:
        if i=='R':
            mode^=1
        elif i=='D':
            if mode:
                state=que.dequeRear()
            else:
                state=que.dequeFront()

    if not state :
        print('error')
    else:
        if mode:
            que.printQue()
        else:
            que.printQueR()
        print('['+",".join(result)+']')

# 원형 큐를 제대로 구현했는데도 불구하고 어디가 틀렸는지 잘 모르겠다.

# print('#2')
# TC=int(input())
# for _ in range(TC):
#     order=input()
#     n=int(input())
#     inp=list(input()[1:-1].split(','))
#     modeDic={0:-1,1:0}
#     mode=1
#     state=True
#     for i in order:
#         if i=='R':
#             mode^=1
#         elif i=='D' and len(inp)!=0 and inp[0]!='':
#             inp.pop(modeDic[mode])
#         else:
#             print('error')
#             state=False
#             break

#     if state:
#         print('['+",".join(inp if mode==1 else inp[::-1])+']')