import sys
sys.stdin = open("test.txt", "r")

n,m = map(int,input().split())
mp = [list(map(int,input().split())) for _ in range(n)]
cameras = []
walls = []
all = 0

for i in range(n):
    for j in range(m):
        if mp[i][j] == 6:
            walls.append([i,j])
        elif mp[i][j] != 0:
            cameras.append([i,j,mp[i][j]])
        elif mp[i][j] == 0:
            all += 1

dy = [0,-1,0,1]
dx = [1,0,-1,0]
watches = [[],[0,4],[0,2,2],[0,1,4],[0,1,2,4],[0,1,2,3,1]]


def sol(cameras,area,cnt):
    global mini
    if len(cameras) == 0:
        if mini > cnt:
            mini = cnt
    else:
        saveCnt = cnt
        cam = cameras[0]
        y = cam[0]
        x = cam[1]
        watch = watches[cam[2]]
        rotate = watch[-1]
        direcs = watch[:-1]
        for i in range(rotate):
            save = []
            roDirecs = list(map(lambda x:(x+i)%4,direcs))
            for direc in roDirecs:
                cy,cx = y,x
                while True:
                    cy += dy[direc]
                    cx += dx[direc]
                    limit = 0<=cy<n and 0<=cx<m
                    if limit and area[cy][cx] !=6:
                        if area[cy][cx] != 0:
                            continue
                        else:
                            area[cy][cx] = '#'
                            cnt -= 1
                            save.append([cy,cx])
                    else:
                        break
            sol(cameras[1:],area,cnt)
            for j in save:
                area[j[0]][j[1]] = 0
            cnt = saveCnt

mini = 99999999999
sol(cameras,mp,all)
print(mini)

# 2차원 배열일지라도 고쳤다가 다시 원상복구해도 작동한다.