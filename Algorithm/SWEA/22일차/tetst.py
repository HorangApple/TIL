import sys
sys.stdin = open("input.txt",'r')

dx=[1,0]
dy=[0,-1]

def dfs(v):
    y,x=v
    while True:
        line.append(inp[y][x])
        k=y
        while True:
            inp[k][x]='0'
            if k+1>n or inp[k+1][x]=='0':
                break
            k+=1
        if (y-1<0 or inp[y-1][x]=='0') and (x+1>n or inp[y][x+1]=='0'):
            break
        x+=1
        
        

TC = int(input())
for num in range(1,TC+1):
   
    n,m = map(int,input().split())
    print(f"#{num}", end=" ")
    inp = [list(input()) for _ in range(n)]
    line16=[]
    for y in range(n):
        for x in range(m):
            line=[]
            if inp[y][x]!='0':
                dfs([y,x])
                line16.append(line)
    print(line16)

