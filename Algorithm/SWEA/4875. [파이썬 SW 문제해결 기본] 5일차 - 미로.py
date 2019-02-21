import sys
sys.stdin = open("input.txt","r")

TC=int(input())
def search(y,x):
    count=0
    if y+1<length and inp[y+1][x]==0:
        count+=1
    if y-1>-1 and inp[y-1][x]==0:
        count+=1
    if x+1<length and inp[y][x+1]==0:
        count+=1
    if y-1>-1 and inp[y][x-1]==0:
        count+=1
    return count
def go(start):
    re=[]
    fobi=[1,-1]
    y=start[0]
    x=start[1]
    stack=[]
    direc=0
    for i in range(search(y,x)):
        stack.append([y,x])
    while True:
        if y+1<length and (inp[y+1][x] not in fobi) or (y+1<length and inp[y+1][x]==0):
            while y+1<length and inp[y+1][x]!=1:
                inp[y][x]=-1
                y+=1
                if inp[y][x]==3:
                    return 1
                if x+1<length and inp[y][x+1]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
                elif x-1>0 and inp[y][x-1]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
        elif y-1>-1 and (inp[y-1][x] not in fobi) or (y-1>-1 and inp[y-1][x]==0):
            while y-1>-1 and inp[y-1][x]!=1:
                inp[y][x]=-1
                y-=1
                if inp[y][x]==3:
                    return 1
                if x+1<length and inp[y][x+1]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
                elif x-1>0 and inp[y][x-1]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
        elif x+1<length and (inp[y][x+1] not in fobi) or (x+1<length and inp[y][x+1]==0):
            while x+1<length and inp[y][x+1]!=1:
                inp[y][x]=-1
                x+=1
                if inp[y][x]==3:
                    return 1
                if y+1<length and inp[y+1][x]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
                elif y-1>0 and inp[y-1][x]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
        elif x-1>-1 and (inp[y][x-1] not in fobi) or (x-1>-1 and inp[y][x-1]==0):
            while x-1>-1 and inp[y][x-1]!=1:
                inp[y][x]=-1
                x-=1
                if inp[y][x]==3:
                    return 1
                if y+1<length and inp[y+1][x]==0:
                    for i in range(search(y,x)):
                        stack.append([y,x])
                    direc=1
                elif y-1>0 and inp[y-1][x]==0:
                    for i in range(search(y,x)):
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

# TC=int(input())

# for num in range(1,TC+1):
#     length=int(input())
#     inp=[[int(i) for i in input()]for _ in range(length)]
#     start=[]
#     stack=[]
#     for i in range(length):
#         for j in range(length):
#             if inp[i][j]==2:
#                 start=[i,j]
#             if start==True:
#                 break
#         if start==True:
#                 break
    
# 시발것
# 00013
# 01110
# 20000
# 01111
# 00000
# 이 테스트 케이스에서 되질 않았다 이를 해결했더니 통과함