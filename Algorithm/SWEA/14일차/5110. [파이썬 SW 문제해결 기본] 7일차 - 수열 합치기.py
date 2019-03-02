import sys
sys.stdin = open("input.txt","r")

class Node:
    def __init__(self, data, link):
        self.data=data
        self.link=link

def addtoFirst(data):
    head = Node(data,None)
    return head

def add(pre,data):
    if pre== None:
        print('error')
    else:
        pre.link=Node(data,pre.link)
    return pre.link

def insert(head,oneline,i):
    node=head
    while node:
        nextLink=node.link
        if nextLink:
            nextLinkData=nextLink.data

        if oneline.data<heads[0].data:
            lastNodeInfo[i].link=heads[0]
            heads[0]=oneline
            return

        elif node.data<=oneline.data<nextLinkData:
            save=node.link
            node.link=oneline
            lastNodeInfo[i].link=save
            return

        elif nextLink==None and node.data<=oneline.data:
            save=node.link
            node.link=oneline
            lastNodeInfo[i].link=save
            return
        node=node.link
    

def printLink(idx,num,head):
    node=head
    i=0
    while i<=idx:
        if i==idx:
            print(f'#{num} {node.data}')
        i+=1
        node=node.link   

def printAll(hd,num):
    node=hd
    i=0
    result=[]
    while node:
        result.append(str(node.data))
        i+=1
        node=node.link
    print(f'#{num} {" ".join(result[-1:-11:-1])}')

TC=int(input())
for num in range(1,TC+1):
    n,m = map(int,input().split())
    line=[]
    heads=[]
    lastNodeInfo=[]
    for _ in range(m):
        line.append(list(map(int,input().split())))
    
    for oneline in line:
        head=addtoFirst(oneline[0])
        heads.append(head)
        preNode=head
        for i in oneline[1:]:
            preNode=add(preNode,i)
        lastNodeInfo.append(preNode)
    i=1
    while i<len(line): 
        insert(heads[0],heads[i],i)
        i+=1
    printAll(heads[0],num)