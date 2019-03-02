import sys
sys.stdin = open("input.txt","r")

class Node:
    def __init__(self, data, link):
        self.data=data
        self.link=link
# 첫 노드 생성
def addtoFirst(data):
    global Head
    Head = Node(data,None)
    return Head
# 추가
def add(pre,data):
    if pre== None:
        print('error')
    else:
        pre.link=Node(data,pre.link)
    return pre.link
# 삽입
def insert(head,m,n):
    global Head
    node=head
    i=0
    # 첫 번째 노드 뒤에 추가하게 될 때
    if m==0:
        nextNode=Head.link
        Head.link=Node(nextNode.data+Head.data,Head.link)
        return m
    # 해당 위치까지 탐색 후 추가
    while node:
        if i==m:
            nextNode=node.link
            # 중간에 삽입할 때
            if nextNode:
                node.link=Node(node.data+nextNode.data,node.link)
            # 맨 끝에 삽입할 때
            else:
                node.link=Node(node.data+Head.data,node.link)
        i+=1
        node=node.link
    return m

def printAll(head,num):
    node=head
    i=0
    result=[]
    while node:
        result.append(str(node.data))
        i+=1
        node=node.link
    print(f'#{num} {" ".join(result[::-1][:10])}')

TC=int(input())
for num in range(1,TC+1):
    n,m,k = map(int,input().split())
    line = list(map(int,input().split()))
    addtoFirst(line[0])
    preNode=Head
    # linkedlist 생성
    for i in line[1:]:
        preNode=add(preNode,i)
    target=m-1 # 삽입하려는 인덱스의 이전 인덱스를 가리킴
    for i in range(1,k+1):
        target=insert(Head,target,n)
        target+=m # m칸 만큼 이동
        n+=1 # 숫자 추가로 길이 +1
        # 만약 가리키는 인덱스가 길이를 넘어서면 mod 연산
        if target>=n:
            target%=n
    printAll(Head,num)