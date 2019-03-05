import sys
sys.stdin = open("input.txt","r")

def nodeSum(idx):
    # 기저 조건
    if idx>n:
        return 0
    # node의 내용이 0이 아닐 때
    if nodeLists[idx]!=0:
        return nodeLists[idx]
    # node의 내용이 0일 때
    else:
        a=nodeSum(2*idx)
        b=nodeSum(2*idx+1)
        nodeLists[idx]=a+b
        return nodeLists[idx]
TC = int(input())
for num in range(1,TC+1):
    n,m,l=list(map(int,input().split()))
    nodeLists=[0]*(n+1)
    result=[]
    for i in range(m):
        leafNode=list(map(int,input().split()))
        nodeLists[leafNode[0]]=leafNode[1]
    nodeSum(1)
    print("#{} {}".format(num,nodeLists[l]))