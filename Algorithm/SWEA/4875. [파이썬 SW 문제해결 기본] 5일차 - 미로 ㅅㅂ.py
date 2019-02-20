import sys
sys.stdin = open("input.txt","r")

TC=int(input())

def go(start):
    re=[]
    fobi=[1,-1]
    y=start[0]
    x=start[1]
    stack=[[y,x]]
    direc=0
    while True:
        if y+1<length and (inp[y+1][x] not in fobi):
            while y+1<length and inp[y+1][x]!=1:
                inp[y][x]=-1
                y+=1
                if inp[y][x]==3:
                    return 1
                if x+1<length and inp[y][x+1]==0:
                    stack.append([y,x])
                    direc=1
                elif x-1>0 and inp[y][x-1]==0:
                    stack.append([y,x])
                    direc=1
        elif y-1>-1 and (inp[y-1][x] not in fobi):
            while y-1>-1 and inp[y-1][x]!=1:
                inp[y][x]=-1
                y-=1
                if inp[y][x]==3:
                    return 1
                if x+1<length and inp[y][x+1]==0:
                    stack.append([y,x])
                    direc=1
                elif x-1>0 and inp[y][x-1]==0:
                    stack.append([y,x])
                    direc=1
        elif x+1<length and (inp[y][x+1] not in fobi):
            while x+1<length and inp[y][x+1]!=1:
                inp[y][x]=-1
                x+=1
                if inp[y][x]==3:
                    return 1
                if y+1<length and inp[y+1][x]==0:
                    stack.append([y,x])
                    direc=1
                elif y-1>0 and inp[y-1][x]==0:
                    stack.append([y,x])
                    direc=1
        elif x-1>-1 and (inp[y][x-1] not in fobi):
            while x-1>-1 and inp[y][x-1]!=1:
                inp[y][x]=-1
                x-=1
                if inp[y][x]==3:
                    return 1
                if y+1<length and inp[y+1][x]==0:
                    stack.append([y,x])
                    direc=1
                elif y-1>0 and inp[y-1][x]==0:
                    stack.append([y,x])
                    direc=1
        if len(stack)==0:
            return 0
        elif direc!=1:
            re=stack.pop()
            y=re[0]
            x=re[1]
        else:
            direc=0

for num in range(1,TC+1):
    length=int(input())
    inp=[[int(i) for i in input()]for _ in range(length)]
    start=[]
    
    for i in range(length):
        for j in range(length):
            if inp[i][j]==2:
                start=[i,j]
            if start==True:
                break
        if start==True:
                break
    print(f'#{num} {go(start)}')