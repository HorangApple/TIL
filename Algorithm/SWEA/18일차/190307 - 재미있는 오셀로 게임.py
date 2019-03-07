import sys
sys.stdin = open("input.txt","r")

def hansu(p):
    mp[p[1]][p[0]] = p[2]
    # 8방향으로 탐색
    for i in range(8):
        stack = []
        for j in range(1, n+1):
            dx1 = [j, 0, -j, 0, j, -j, j, -j]
            dy1 = [0, j, 0, -j, j, -j, -j, j]
            x1 = p[0] + dx1[i]
            y1 = p[1] + dy1[i]
            if 0 < x1 < n + 1 and 0 < y1 < n + 1 :
                if mp[y1][x1] != 0:
                    if mp[y1][x1] != p[2]:
                        stack.append([x1, y1])
                    elif mp[y1][x1] == p[2]:
                        for k in stack:
                            mp[k[1]][k[0]] = p[2]
                        break
                elif mp[y1][x1] == 0:
                    break

T=int(input())
for num in range(1,T+1):
    n,m=map(int,input().split())
    mp=[[0]*(n+2) for _ in range(n+2)]
    # map 셋팅
    middle=n//2
    mp[middle][middle]=2
    mp[middle+1][middle]=1
    mp[middle+1][middle+1]=2
    mp[middle][middle+1]=1
    blackCnt=0
    whiteCnt=0
    # 돌 놓기
    for i in range(m):
        point=list(map(int,input().split()))
        # print(point)
        hansu(point)
        # for g in mp:
        #     print(g)
        # print()
    # 돌 세기
    for i in mp:
        for j in i:
            if j==1 and j!=0:
                blackCnt+=1
            elif j==2 and j!=0:
                whiteCnt+=1
    print("#{} {} {}".format(num,blackCnt,whiteCnt))

    # 처음으로 오셀로 규칙을 들어봄
    # 1 2 2 1 일 때도 숫자가 바뀐다
    # 디버깅 할 땐 디버깅 하기 편하도록 코드를 짠다