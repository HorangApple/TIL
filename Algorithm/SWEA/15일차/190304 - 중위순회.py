import sys
sys.stdin = open("input.txt","r")

def search(node):
    length=len(node)
    if length>2:
        search(tree[int(node[2])])
        visited.append(node[1])
        if length>3:
            search(tree[int(node[3])])
    else:
        visited.append(node[1])

TC=10
for num in range(1,TC+1):
    length=int(input())
    tree=[[str(i)] for i in range(length+1)]
    visited=[]
    for i in range(length):
        inp=list(input().split())
        tree[int(inp[0])]+=inp[1:]
    search(tree[1])
    print("#{} {}".format(num,"".join(visited)))