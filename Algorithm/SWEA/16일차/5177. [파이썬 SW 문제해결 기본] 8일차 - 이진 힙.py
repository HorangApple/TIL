import sys
sys.stdin = open("input.txt","r")

def add(number):
    nodeLists[number] = inp.pop(0) # 값 추가
    idx1=number
    idx2=number
    # 추가한 값이 부모보다 작으면 계속해서 자리 바꿈
    while idx1!=0:
        idx1//=2
        if nodeLists[idx1]>nodeLists[idx2]:
            nodeLists[idx1],nodeLists[idx2]=nodeLists[idx2],nodeLists[idx1]
            idx2=idx1

# 거꾸로 돌아가 조상만 골라 합산
def search(n):
    result=[]
    while True:
        if n==0:
            return sum(result)
        if n%2==0:
            n//=2
            result.append(nodeLists[n])
        else:
            n=(n-1)//2
            result.append(nodeLists[n])

TC = int(input())
for num in range(1,TC+1):
    n=int(input())
    inp=list(map(int,input().split()))
    nodeLists=[0]*(n+1)
    for i in range(1,n+1):
        add(i)

    print("#{} {}".format(num,search(n)))