import sys
sys.stdin = open("input.txt","r")

for num in range(1,11):
    length=int(input())
    nsMap=[input() for _ in range(length)]
    count=0
    # i는 가로
    for i in range(length):
        before=0
        # j는 세로
        for j in range(length):
            # 1을 만나면 만난 것을 before에 기억했다가
            if nsMap[j][2*i]=='1':
                before=1
            # 1을 만난 상태에서 2를 만나면 count에 추가
            # 이후 before를 다시 0으로 초기화
            elif nsMap[j][2*i]=='2' and before==1:
                before=0
                count+=1
    print(f'#{num} {count}')