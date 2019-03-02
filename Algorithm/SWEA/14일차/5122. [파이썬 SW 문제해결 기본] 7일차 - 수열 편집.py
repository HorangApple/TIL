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
    # 추가
    if od[0]=='I':
        # 맨 앞의 노드일 경우
        if od[1]=='0':
            Head=Node(od[2],Head)
            return
        # 그 이후의 노드일 경우
        while i<=int(od[1]):
            if i==int(od[1])-1:
                node.link=Node(od[2],node.link)
            i+=1
            node=node.link
    # 삭제
    elif od[0]=='D':
        # 맨 앞의 노드일 경우
        if od[1]=='0':
            Head=Head.link
            return
        # 그 이후의 노드일 경우
        while i<=int(od[1]):
            if i==int(od[1])-1:
                targetNode=node.link
                node.link=targetNode.link
                targetNode.link=None
            i+=1
            node=node.link
    # 해당 인덱스의 data 수정
    elif od[0]=='C':
        # 맨 앞의 노드일 경우
        if od[1]=='0':
            Head.data=od[2]
            return
        # 그 이후의 노드일 경우
        while i<=int(od[1]):
            if i==int(od[1]):
                node.data=od[2]
            i+=1
            node=node.link

def printLink(head,idx,num):
    node=head
    i=0
    while i<=idx:
        if i==idx:
            print(f'#{num} {node.data}')
        i+=1
        if node==None:
            print(f'#{num} {-1}')
            return
        node=node.link   

TC=int(input())
for num in range(1,TC+1):
    n,m,l = map(int,input().split())
    line = list(map(int,input().split()))
    order=[]
    for _ in range(m):
        order.append(input().split())
    addtoFirst(line[0])
    preNode=Head
    for i in line[1:]:
        preNode=add(preNode,i)
    # 편집 수행
    for i in order:
        insert(Head,i)

    printLink(Head,l,num)