import sys
sys.stdin = open("input.txt","r")

c = int(input())

puzzles = [
    [[0,0],[0,1],[1,0]],
    [[0,0],[1,-1],[1,0]],
    [[0,0],[0,1],[1,1]],
    [[0,0],[1,0],[1,1]]
]
types = [0,1,2,3]
direction = 0

def solution(y,x,mapInfom,typ):
    n = mapInfo.count('.')
    nextX = 0
    if n == 0 :
        return 1

    for xy in puzzles[types[typ]] :
        pieceX = x+xy[1]
        pieceY = y+xy[0]
        nextX += xy[1] if xy[1] > 0 else 0
        if pieceX<h and pieceX>=0 and pieceY<w and pieceY>=0 and mapInfo[pieceY][pieceX]!="#":
            mapInfo[pieceY][pieceX] = "#"
            if x+nextX >= w :
                x = 0
                return solution(y+1,x,mapInfo,0)+solution(y+1,x,mapInfo,1)+solution(y+1,x,mapInfo,2)+solution(y+1,x,mapInfo,3)
            else :
                return solution(y,x+nextX,mapInfo,0)+solution(y,x+nextX,mapInfo,1)+solution(y,x+nextX,mapInfo,2)+solution(y,x+nextX,mapInfo,3)
            

for i in range(c):
    # h는 세로 w는 가로
    h, w = map(int,input().split())
    mapInfo = [[i for i in input()] for _ in range(h)]
    x,y=-1,-1
    for i in mapInfo :
        for j in i :
            if j == '.':
                x=i.index(j)
                y=mapInfo.index(i)
                break
        if x > -1 : break
    cnt = 0
    print(x,y)
    print(f'{solution(y,x,mapInfo,cnt)}')

