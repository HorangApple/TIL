import sys
sys.stdin = open("test.txt", "r")

n = int(input())

lines = [list(map(int,input().split())) for _ in range(n)]
mp = [[0 for _ in range(101)] for _ in range(101)]

dy = [0,-1,0,1]
dx = [1,0,-1,0]

def rotation(x):
    x+=1
    if x == 4:
        x= 0
    return x

def detect():
    result = 0
    for i in range(100):
        for j in range(100):
            if mp[i][j] == 1 and mp[i+1][j] == 1 and mp[i][j+1] == 1 and mp[i+1][j+1] == 1 :
                result +=1
    print(result)

moved = []
for line in lines:
    direction = [line[2]]
    for _ in range(line[3]):
        rotated = list(map(rotation,direction[::-1]))
        direction += rotated
    moved.append(direction)

for p,d in zip(lines,moved):
    mp[p[1]][p[0]]=1
    for i in d:
        p[0] = p[0] + dx[i]
        p[1] = p[1] + dy[i]
        if 0<=p[0]<=100 and 0<=p[1]<=100:
            mp[p[1]][p[0]] = 1

detect()