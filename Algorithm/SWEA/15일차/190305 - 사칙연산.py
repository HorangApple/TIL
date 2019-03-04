import sys
sys.stdin = open("input.txt","r")

def search(node):
    length=len(node)
    if length>3:
        search(tree[int(node[2])]) # 왼쪽
        if length>4:
            search(tree[int(node[3])]) # 오른쪽
            b = int(visited.pop())
            a = int(visited.pop())
        if node[1]=='+':
            visited.append(a+b)
        elif node[1]=='-':
            visited.append(a-b)
        elif node[1]=='*':
            visited.append(a*b)
        elif node[1]=='/':
            visited.append(a//b)
    else:
        visited.append(node[1]) # 맨 끝 노드 저장

TC=10
for num in range(1,TC+1):
    length=int(input())
    tree=[[i] for i in range(length+1)]
    visited=[]
    parent=0
    for i in range(length):
        inp=list(input().split())
        tree[int(inp[0])]=tree[int(inp[0])]+inp[1:]+[parent]
        parent=int(inp[0])
    search(tree[1])
    print("#{} {}".format(num,visited[0]))