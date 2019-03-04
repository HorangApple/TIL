import sys
sys.stdin = open("input.txt","r")

def search(node):
    global count
    if len(tree[node])>1:
        search(tree[node][1])
        if len(tree[node])>2:
            search(tree[node][2])
        count+=1
    else:
        count+=1

TC=int(input())
for num in range(1,TC+1):
    e,n=map(int,input().split())
    inp=list(map(int,input().split()))
    tree=[[i] for i in range(e+2)]
    for i in range(len(inp)//2):
        tree[inp[2*i]]+=[inp[2*i+1]]
    count=0
    search(n)
    print("#{} {}".format(num,count))