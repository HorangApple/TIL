import sys
sys.stdin = open("input.txt","r")

def bitree(inp,tree,n):
    middle = len(inp)//2
    l=inp[:middle]
    r=inp[middle+1:]
    que=[l,r]
    while len(tree)<n+1:
        obj=que.pop(0)
        if len(obj)==1:
            tree.append(obj[0])
            continue
        if obj==[]:
            continue
        middle=len(obj)//2
        tree.append(obj[middle])
        l = obj[:middle]
        r = obj[middle + 1:]
        que.append(l)
        que.append(r)

TC=int(input())
for num in range(1,TC+1):
    n=int(input())
    inp=list(range(1,n+1))
    tree=[0,inp[len(inp)//2]]
    bitree(inp,tree,n)
    print("#{} {} {}".format(num,n//2+1,tree[n//2]))