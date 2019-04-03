import sys
sys.stdin = open('input.txt','r')


dx = [1,0,-1,0]
dy = [0,1,0,-1]

def solution(k,v,n):
    global cnt
    if k==6:
        result.append(n)
    else:
        k+=1
        for i in range(4):
            sy = v[0]+dy[i]
            sx = v[1]+dx[i]
            if -1<sy<4 and -1<sx<4:
                solution(k,[sy,sx],n+inp[sy][sx])

TC = int(input())
for num in range(1,TC+1):
    inp = [list(input().split()) for _ in range(4)]
    result=[]
    for i in range(4):
        for j in range(4):
            solution(0,[i,j],inp[i][j])
    print(f'#{num}',len(set(result)))