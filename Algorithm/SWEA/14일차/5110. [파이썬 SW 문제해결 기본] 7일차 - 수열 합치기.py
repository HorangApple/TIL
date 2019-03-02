import sys
sys.stdin = open("input.txt","r")

class Node:
    def __init__(self, data, link):
        self.data=data
        self.link=link

# 첫 노드 생성
def addtoFirst(data):
    head = Node(data,None)
    return head

# 추가
def add(pre,data):
    if pre== None:
        print('error')
    else:
        pre.link=Node(data,pre.link)
    return pre.link

# 삽입
def insert(head,oneline,i):
    node=head
    while node:
        # 다음 노드 탐색
        nextLink=node.link
        if nextLink:
            nextLinkData=nextLink.data
        # data가 맨 앞의 노드의 data보다 작을 경우
        if oneline.data<heads[0].data:
            lastNodeInfo[i].link=heads[0] # 해당 수열의 마지막에 노드를 이어붙임
            heads[0]=oneline
            return
        # 맨 앞의 노드의 data와 다음 노드의 data보다 작을 경우
        elif node.data<=oneline.data<nextLinkData:
            save=node.link
            node.link=oneline
            lastNodeInfo[i].link=save # 해당 수열의 마지막에 뒷 부분 노드를 이어붙임
            return
        # 다음 노드가 없는 경우
        elif nextLink==None and node.data<=oneline.data:
            save=node.link
            node.link=oneline
            lastNodeInfo[i].link=save # 해당 수열의 마지막에 None을 입력
            return
        node=node.link

# 모든 노드의 data를 리스트로 만들어 역순으로 출력    
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
    # 각 수열 마다 linkedlist 생성 및 마지막 노드만 모은 리스트 생성
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