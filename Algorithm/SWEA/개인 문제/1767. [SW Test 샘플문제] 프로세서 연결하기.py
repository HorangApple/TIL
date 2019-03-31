# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf&
import sys
sys.stdin = open('input.txt','r')

dx = [0,1,0,-1,0]
dy = [1,0,-1,0,0]

# 십자 방향으로 다른 코어가 길을 막고 있는지 조사
def search(v):
    direction=[0,1,2,3,4]
    for i in sideCore+allCore:
        if i==v:
            continue
        if v[0]==i[0] or v[1]==i[1]:
            if v[0]-i[0]==0:
                if v[1]-i[1]>0:
                    direction[3]=-1
                else:
                    direction[1]=-1
            if v[1]-i[1]==0:
                if v[0]-i[0]>0:
                    direction[2]=-1
                else:
                    direction[0]=-1
    return direction

def solution(k,arr,cnt):
    global Maxcore,Minlines
    # 시간 단축의 핵심, 이후에 진행해도 최대치를 못넘으면 생략한다.
    if allCoreCnt-k+cnt<Maxcore:
        return
    if k < allCoreCnt:
        v=allCore[k]
        for i in search(v):
            if i==-1:
                continue
            sx=v[1]+dx[i]
            sy=v[0]+dy[i]
            line=[]
            while -1<sx<n and -1<sy<n and i!=4:
                if [sy,sx] not in arr:
                    line+=[[sy,sx]]
                    sx=sx+dx[i]
                    sy=sy+dy[i]
                else:
                    break
            else:
                if i!=4:
                    cnt+=1
                solution(k+1,arr+line,cnt)
                if i!=4:
                    cnt-=1
    else:
        if Maxcore<cnt:
            Maxcore=cnt
            Minlines=0xffffff
        elif Maxcore==cnt:
            Minlines=min(Minlines,len(arr))

TC = int(input())
for num in range(1,TC+1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    allCore=[]
    sideCore=[]
    allCoreCnt=0
    Maxcore=0
    Minlines=0xffffff
    for y in range(0,n):
        for x in range(0,n):
            if (x==0 or y==0 or x==n-1 or y==n-1) and mp[y][x]==1:
                sideCore+=[[y,x]]
            else:
                if mp[y][x]==1:
                    allCore+=[[y,x]]
                    allCoreCnt+=1
    solution(0,[],0)
    print(f'#{num}',Minlines)


import sys

sys.stdin = open("sampleA_input.txt")


# 세환이 코드
# DFS를 활용한 백트래킹
# 칩마다 전선 연결 여부로 판단
def connect(k, cores, length):
    # print("I AM : ", k, cores, length)
    global cores_num, max_cores, min_length, N
    # 완전탐색 종료 후 결과 갱신 시도
    if k == cores_num:
        # 코어 개수가 같으면 길이 비교
        if cores == max_cores:
            if length < min_length:
                min_length = length
        # 코어 개수가 더 많으면 무조건 갱신
        elif cores > max_cores:
            max_cores = cores
            min_length = length
        return
    # 코어 최대값 도달 가능성 확인
    if cores + cores_num - k >= max_cores:
        # 최대 코어가 같으면서 길이가 이미 최소치를 넘으면 탈락
        if cores + cores_num - k == max_cores and length > min_length:
            return
        # 만약 가장자리 core 라면 전선 없이 통과
        if core_info[k][0] == 0 or core_info[k][0] == N-1 or core_info[k][1] == 0 or core_info[k][1] == N-1:
            connect(k+1, cores+1, length)
            # print("{} if free!!".format(k))
        else:
            # 전선 둘 수 있는 방향 체크
            direction = line_check(k)
            # print("{} can go : {}".format(k, direction))
            # 전선을 위로 연결
            if direction[0]:
                core_info[k][2] = 1
                connect(k+1, cores+1, length + core_info[k][0])
                core_info[k][2] = 0
            # 전선을 아래로 연걸
            if direction[1]:
                core_info[k][3] = 1
                connect(k+1, cores+1, length + N - core_info[k][0] - 1)
                core_info[k][3] = 0
            # 전선을 오른쪽으로 연결
            if direction[2]:
                core_info[k][4] = 1
                connect(k+1, cores+1, length + N - core_info[k][1] - 1)
                core_info[k][4] = 0
            # 전선을 왼쪽으로 연걸
            if direction[3]:
                core_info[k][5] = 1
                connect(k+1, cores+1, length + core_info[k][1])
                core_info[k][5] = 0
            # 전선 연결안하고 다음으로
            connect(k+1, cores, length)


def line_check(k):
    row, col = core_info[k][0], core_info[k][1]
    # 전선 연결 가능성. 위 아 오 왼.
    # info : [row, col, up, down, right, left]
    direction = [True, True, True, True]
    cnt = 4

    # 가능성 확인
    for info in core_info:
        # 위쪽 가능성
        if direction[0]:
            if info[1] == col and info[0] < row:
                direction[0] = False
                cnt -= 1
            if info[4] == 1:
                if info[0] < row and info[1] < col:
                    direction[0] = False
                    cnt -= 1
            if info[5] == 1:
                if info[0] < row and info[1] > col:
                    direction[0] = False
                    cnt -= 1
        # 아래쪽 가능성
        if direction[1]:
            if info[1] == col and info[0] > row:
                direction[1] = False
                cnt -= 1
            if info[4] == 1:
                if info[0] > row and info[1] < col:
                    direction[1] = False
                    cnt -= 1
            if info[5] == 1:
                if info[0] > row and info[1] > col:
                    direction[1] = False
                    cnt -= 1
        # 오른쪽 가능성
        if direction[2]:
            if info[0] == row and info[1] > col:
                direction[2] = False
                cnt -= 1
            if info[2] == 1:
                if info[0] > row and info[1] > col:
                    direction[2] = False
                    cnt -= 1
            if info[3] == 1:
                if info[0] < row and info[1] > col:
                    direction[2] = False
                    cnt -= 1
        # 왼쪽 가능성
        if direction[3]:
            if info[0] == row and info[1] < col:
                direction[3] = False
                cnt -= 1
            if info[2] == 1:
                if info[0] > row and info[1] < col:
                    direction[3] = False
                    cnt -= 1
            if info[3] == 1:
                if info[0] < row and info[1] < col:
                    direction[3] = False
                    cnt -= 1
        # 갈 곳 없으면 중단
        if cnt == 0:
            break
    return direction


testcase = int(input())

for tc in range(1, testcase + 1):
    N = int(input())
    chip = []
    for _ in range(N):
        chip.append(input().split())

    # for _ in range(N):
    #     print(chip[_])

    # chip에서 1의 위치 기록하기
    core_info = []
    for r in range(N):
        for c in range(N):
            if chip[r][c] == '1':
                core_info.append([r, c, 0, 0, 0, 0])
    cores_num = len(core_info)

    # 답변용 변수 초기화
    max_cores = 0
    min_length = 99999

    # 완전탐색 시작
    connect(0, 0, 0)

    # 답 출력
    print("#{} {}".format(tc, min_length))
