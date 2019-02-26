import sys
sys.stdin = open("input.txt","r")


def converter (arr) :
    color = [[0]*(arr[3]+1) for i in range(arr[2]+1)]
    for y in range(arr[0],arr[2]+1):
        for x in range(arr[1],arr[3]+1) :
            color[y][x] = 1
    return color

def adder (arr) :
    ground = [[0]*(maxX+1) for i in range(maxY+1)]
    for i in arr :
        for y in range(len(i)):
            for x in range(len(i[0])):
                if ground[y][x] == 0:
                    ground[y][x] += i[y][x]
    return ground
                
def selector (red,blue) :
    count=0
    for y in range(len(red)) :
        for x in range(len(red[0])):
            red[y][x] += blue[y][x]
            if red[y][x]>=2:
                count +=1
    return count

T=int(input())

for i in range(T):
    red = []
    blue = []
    redmap=[]
    bluemap=[]
    maxX,maxY=0,0
    N=int(input())
    for j in range(N):
        inp = list(map(int, input().split()))
        if inp[-2] > maxX :
            maxX=inp[-2]
        if inp[-3] > maxY :
            maxY=inp[-3]    
        if inp[-1] ==1 :
            red.append(converter(inp))
        else :
            blue.append(converter(inp))

    redmap=adder(red)
    bluemap=adder(blue)

    print(f'#{i+1} {selector(redmap,bluemap)}')


# 선생님 코드
TC = int(input())
for tc in range (1, TC+1):
    N = int(input())
    m = [[0]*10 for i in range(10)]
    cnt = 0

    for _ in range (0, N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                m[i][j] += color

    for i in range(10):
        for j in range(10):
            if m[i][j] == 3:
                cnt += 1

    print("#%d %d"%(tc, cnt))