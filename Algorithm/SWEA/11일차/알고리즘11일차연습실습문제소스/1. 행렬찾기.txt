import sys
sys.stdin = open("input.txt", 'r')


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

