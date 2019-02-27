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

def insert(head,m,n,lastNode):
    global Head
    node=head
    if m>=n:
        m=m%n-1
    i=0
    if m==0:
        nextNode=Head.link
        Head.link=Node(nextNode.data+Head.data,Head.link)
        return
    while i<=m:
        if i==m-1:
            nextNode=node.link
            if nextNode:
                node.link=Node(node.data+nextNode.data,node.link)
            else:
                node.link=Node(node.data+Head.data,node.link)
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

def printAll(head,num):
    node=head
    i=0
    result=[]
    while node:
        result.append(str(node.data))
        i+=1
        node=node.link
    print(f'#{num} {" ".join(result[::-1])}')

TC=int(input())
for num in range(1,TC+1):
    n,m,k = map(int,input().split())
    line = list(map(int,input().split()))
    addtoFirst(line[0])
    preNode=Head
    for i in line[1:]:
        preNode=add(preNode,i)
    lastNode=preNode
    for i in range(1,k+1):
        target=m*i
        n+=1
        insert(Head,target,n,lastNode)
    printAll(Head,num)