import sys
sys.stdin = open("input.txt","r")


TC = int(input())
# 순회하면서 값 추가
def add(number):
    global cnt
    if number<=n:
        add(number * 2)
        nodeLists[number]=cnt
        cnt+=1
        add(number * 2+1)

for num in range(1,TC+1):
    n=int(input())
    cnt=1
    nodeLists=[0]*(n+1)
    add(1)
    print("#{} {} {}".format(num,nodeLists[1],nodeLists[n//2]))

# 리스트를 트리 형식으로 만드는게 아닌
# 숫자를 초기화시키는 순서를 트리를 만드는 것처럼 구현한다.