import sys
sys.stdin = open("input.txt","r")

c = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]
direction = 0

def detect (i,j,mapInfo,direction):
    x = j+dx[direction]
    y = i+dy[direction]
    dot1 = mapInfo[y][x]
    dot2 = mapInfo[y+1][x+1]
    if dot1 =='.' and dot2 == '.' :
        mapInfo[i][j] = '#'
        dot1 = '#'
        dot2 = '#'
    return mapInfo

def solution(h,w,mapInfo, cnt):
    n = mapInfo.count('.')
    if n%3 != 0 :
        return cnt
    if n == 0 :
        return cnt
    for j in range(w):
        if mapInfo[h-1][j] != '#' and mapInfo [h-1][j] == '.':
            detect(i,j,mapInfo,0)
            
                       
for i in range(c):
    # h는 세로 w는 가로
    h, w = map(int,input().split())
    mapInfo = [list(input().split()) for _ in range(h)]
    cnt = 0
    print(f'{solution(h,w,mapInfo,cnt)}')

