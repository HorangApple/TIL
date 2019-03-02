
dx=[0,1]
dy=[1,0]

# 시작 좌표에서 오른쪽 아래의 대각선 끝 좌표를 탐색
def solution(start,n):
    que=[start]
    while que:
        go=que.pop(0)
        # 다음 갈 곳을 탐색하면서 que에 추가
        for i in range(2):
            x=go[1]+dx[i]
            y=go[0]+dy[i]
            # 다음 좌표가 구역 내이고 0이 아니면 0으로 바꾸고 좌표를 que에 추가
            if x<n and y<n and inp[y][x]>0:
                inp[y][x]=0
                if [y,x] not in que:
                    que.append([y,x])
    return go

# 문제의 요구사항대로 버블정렬
def mySort(result):
    for i in range(len(result)):
        for j in range(len(result)-1-i):
            # 넓이
            a=result[j][0]*result[j][1]
            b=result[j+1][0]*result[j+1][1]
            if a > b:
                result[j],result[j+1]=result[j+1],result[j]
            # 넓이가 서로 같으면 세로 길이를 비교해 정렬
            elif a==b:
                if result[j][0]>result[j+1][0]:
                    result[j],result[j+1]=result[j+1],result[j]

TC=int(input())
for num in range(1,TC+1):
    n=int(input())
    inp=[list(map(int,input().split())) for _ in range(n)]
    result=[]
    for i in range(n):
        for j in range(n):
            if inp[i][j]>0:
                start=[i,j]
                # 끝 좌표 탐색
                end=solution(start,n)
                # [세로길이,가로길이] 형식으로 추가
                result.append([end[0]-start[0]+1,end[1]-start[1]+1])
    mySort(result)
    print(f'#{num} {len(result)}',end=" ")
    for i in result:
        print(i[0],i[1],end=" ")
    print("")



# 선생님 코드
def getsubmatrix(i, j):
    xc = i
    while xc < msize and matrix[xc][j] != 0:
        yc = j
        while yc < msize and matrix[xc][yc] != 0:
            matrix[xc][yc] = 0
            yc += 1
        xc += 1

    submatrix.append([xc-i, yc-j])

N = int(input())
for tc in range(1, 11):
    subcnt = 0
    msize = int(input())

    matrix = [[0] * msize for _ in range(msize)]
    submatrix = []

    for i in range(msize):
        matrix[i] = list(map(int, input().split()))

    for i in range(msize) :
        for j in range(msize):
            if matrix[i][j]:
                getsubmatrix(i, j)
                subcnt += 1

    for i in range(subcnt-1):
        minI = i
        for j in range(i+1, subcnt):
            if submatrix[minI][0] * submatrix[minI][1] > submatrix[j][0] * submatrix[j][1]:
                minI = j
            if submatrix[minI][0] * submatrix[minI][1] == submatrix[j][0] * submatrix[j][1]:
                if submatrix[minI][0] > submatrix[j][0]:
                    minI = j
        submatrix[i][0], submatrix[minI][0] = submatrix[minI][0], submatrix[i][0]
        submatrix[i][1], submatrix[minI][1] = submatrix[minI][1], submatrix[i][1]

    # submatrix.sort(key= lambda x:(x[0] * x[1], x[0]))

    print("#%d %d"%(tc, subcnt), end='')
    for a, b in submatrix:
        print(" %d %d"%(a,b), end='')
    print()