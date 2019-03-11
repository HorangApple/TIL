import sys
sys.stdin = open("input.txt","r")

col,row=map(int,input().split())
mp=[list(map(int,input().split())) for _ in range(col)]
def cnt():
    count=0
    for i in range(col):
        for j in range(row):
            if mp[i][j]>0:
                count+=1
    return count

def bfs():
    while True:
        if que:
            point=que.pop(0)
            visited[point[0]][point[1]]=True
            if point[0]+1<col:
                if mp[point[0]+1][point[1]]==0 and [point[0]+1,point[1]] not in que and not visited[point[0]+1][point[1]]:
                    que.append([point[0]+1,point[1]])
                    visited[point[0]+1][point[1]]=True
                elif mp[point[0]+1][point[1]]==1 and [point[0]+1,point[1]] not in delete:
                    delete.append([point[0]+1,point[1]])
            if point[1]+1<row:
                if mp[point[0]][point[1]+1]==0 and [point[0],point[1]+1] not in que and not visited[point[0]][point[1]+1]:
                    que.append([point[0], point[1]+1])
                    visited[point[0]][point[1]+1] = True
                elif mp[point[0]][point[1]+1]==1 and [point[0],point[1]+1] not in delete:
                    delete.append([point[0],point[1]+1])
            if -1<point[0]-1:
                if mp[point[0]-1][point[1]]==0 and [point[0]-1,point[1]] not in que and not visited[point[0]-1][point[1]]:
                    que.append([point[0]-1, point[1]])
                    visited[point[0]-1][point[1]] = True
                elif mp[point[0]-1][point[1]]==1 and [point[0]-1,point[1]] not in delete:
                    delete.append([point[0]-1,point[1]])
            if -1<point[1]-1:
                if mp[point[0]][point[1]-1]==0 and [point[0],point[1]-1] not in que and not visited[point[0]][point[1]-1]:
                    que.append([point[0], point[1]-1])
                    visited[point[0]][point[1]-1] = True
                elif mp[point[0]][point[1]-1]==1 and [point[0],point[1]-1] not in delete:
                    delete.append([point[0],point[1]-1])
        else:
            break

before=cnt()
delCnt=0
while True:
    que = [[0, 0]]
    delete = []
    visited = [[False] * row for _ in range(col)]
    bfs()
    for i in mp:
        print(i)
    print()
    for i in delete:
        mp[i[0]][i[1]]=0
    chiCnt=cnt()
    delCnt+=1
    if chiCnt==0:
        break
    before = chiCnt
print(delCnt)
print(before)