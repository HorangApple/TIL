def visit(T):
    visited.append(T)

def pre_traverse(node):
    length=len(node)
    if length!=1:
        visit(node[0])
        if length>1:
            pre_traverse(tree[node[1]])
            if length>2:
                pre_traverse(tree[node[2]])
    else:
        visit(node[0])

tree=[[i] for i in range(14)]
inp=[1,2,1,3,2,4,3,5,3,6,4,7,5,8,5,9,6,10,6,11,7,12,11,13]
visited=[]
for i in range(len(inp)//2):
    tree[inp[2*i]]+=[inp[2*i+1]]

pre_traverse(tree[1])
print(visited)