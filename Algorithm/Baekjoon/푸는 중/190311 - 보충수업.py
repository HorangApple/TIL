# 재귀 호출
# 반복 구조 동일한 계산 작업을 수행
# DFS, 트리 순회
# 백트래킹 - 상태 공간 트리, 상태 공간 그래프
# 분할 정복
# 재귀적 DP(재귀+메모이제이션)

# 반복으로 처음에는 구현하기가 어려우니 먼저 재귀로 푼다.
# 반복으로 푸는 것은 순서에 맞게 잘 작성해야한다. 

# 문제간의 관계를 이용해서 해결할 때
# 작은 문제의 해를 구해서 좀 더 큰 문제의 해를 구하는 방법

# 정형화해서 식을 나타낸 것이 점화식
# Dynamic programming

# 반복
# 재귀호출의 종료조건을 먼저 선언해야한다
# 넘어오는 매개변수를 이용해서 종료조건(기저)을 작성해야한다.
# 매개변수 - 문제를 식별하는 값, 문제의 크기를 나타내는 값
for i in range(3):
    print("hello")

cnt=0
def printHello(i,n):
    global cnt
    if i==n:
        print(path)
        paths.append(path[:])
        cnt+=1
        return
    # 함수호출:2 높이:3이면 cnt는 2^3으로 출력
    # 이진 트리 형태로 작동된다.
    path[i]=1
    printHello(i+1,n)
    path[i]=0
    printHello(i+1,n)
#--------------------
paths=[]
path=[0]*3
printHello(0,3)
print('cnt= ',cnt)
print(paths)

# 아래와 같이 for 문이 반복되는 상황이면 재귀로 바꾸는게 좋다
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i,j,k)
