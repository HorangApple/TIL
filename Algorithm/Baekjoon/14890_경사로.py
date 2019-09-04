import sys
sys.stdin = open('test.txt', 'r')

n,l = map(int,input().split())
mp = [list(map(int,input().split())) for _ in range(n)]

def check(line):
    global cnt
    i = 0
    while i<n-1:
        # 내리막
        if abs(line[i])-line[i+1] == 1:
            save = abs(line[i+1])
            for _ in range(l):
                i += 1
                if i >=n or abs(line[i]) != save:
                    return
                line[i] = -line[i]


        # 오르막
        elif abs(line[i])-line[i+1] == -1:
            save = abs(line[i])
            i = i-l+1
            for _ in range(l):
                if i<0 or line[i]<0 or line[i] != save:
                    return
                i+=1

        elif abs(line[i])-line[i+1] == 0:
            i+=1
        else:
            return
    else:
        cnt+=1

cnt = 0

for i in mp:
    check(i)

for i in range(n):
    line = []
    for j in mp:
        line.append(abs(j[i]))
    check(line)
    line.clear()

print(cnt)