import sys
sys.stdin = open("input.txt","r")

TC=int(input())

def vs(left,right):
    result=left[0][0]-right[0][0]
    if result==1 or result==-2 : # 왼쪽 승
        return left
    elif result==-1 or result==2: # 오른쪽 승
        return right
    else: # 비길 때 왼쪽
        return left

# 합병정렬 사용    
def merge(inp,idx):
    length=len(inp)
    if len(inp)<=1:
        # [가위바위보, 선수번호] 형식으로 리턴
        return [inp,idx]
    middle=(length+1)//2
    # 가위바위보
    left=inp[:middle]
    right=inp[middle:]

    # 선수 번호도 같이 합병정렬
    leftidx=idx[:middle]
    rightidx=idx[middle:]

    left=merge(left,leftidx)
    right=merge(right,rightidx)
    return vs(left,right)

for num in range(1,TC+1):
    length=int(input())
    inp=list(map(int,input().split()))
    idx=list(range(1,length+1))
    result=merge(inp,idx)
    
    print(f'#{num} {result[1][0]}')

# 문제에서 i번부터 j번이라고 나와있는데 이 때문에 i+j가 length가 아닌 여기에 +1을 해야 같다
# 실제 length에 1을 더하냐 마냐에 따라 답이 달라진다.

# 선생님 풀이
def solve(s, e):
    if s == e:  return s
    else:
        win1 = solve(s, (s + e) // 2) # index 값만 전달
        win2 = solve((s + e) // 2 + 1, e)

        if card[win1] == card[win2]:
            return win1
        else:
            if card[win1] == 1:
                if card[win2] == 2:     return win2     # 가위 vs 바위
                else :                  return win1     # 가위 vs 보
            elif card[win1] == 2 :
                if card[win2] == 1:     return win1     # 바위 vs 가위
                else :                  return win2     # 바위 vs 보
            elif card[win1] == 3 :
                if card[win2] == 1:     return win2     # 보 vs 가위
                else :                  return win1     # 보 vs 바위

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = [0] + list(map(int, input().split())) # 카드를 별도로 저장
    print('#%d'%tc, solve(1, N))