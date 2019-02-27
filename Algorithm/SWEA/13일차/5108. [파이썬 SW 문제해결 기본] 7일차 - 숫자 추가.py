import sys
sys.stdin = open("input.txt","r")

class Node:
    def __init__(self, data, link):
        self.data=data
        self.link=link

def addtoFirst(data):
    global Head
    Head = Node(data,None)
    return Head

def add(pre,data):
    if pre== None:
        print('error')
    else:
        pre.link=Node(data,pre.link)
    return pre.link

def insert(head,od):
    global Head
    node=head
    i=0
    if od[0]==0:
        Head=Node(od[1],Head)
        return
    while i<=od[0]:
        if i==od[0]-1:
            node.link=Node(od[1],node.link)
        i+=1
        node=node.link

def printLink(head,idx,num):
    node=head
    i=0
    while i<=idx:
        if i==idx:
            print(f'#{num} {node.data}')
        i+=1
        node=node.link   

def printAll(head):
    node=head
    i=0
    while node:
        print(f'{node.data}',end=" ")
        i+=1
        node=node.link

TC=int(input())
for num in range(1,TC+1):
    n,m,l = map(int,input().split())
    line = list(map(int,input().split()))
    order=[]
    for _ in range(m):
        order.append(list(map(int,input().split())))
    addtoFirst(line[0])
    preNode=Head
    for i in line[1:]:
        preNode=add(preNode,i)
    for i in order:
        insert(Head,i)
    printLink(Head,l,num)