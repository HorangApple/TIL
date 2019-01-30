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
