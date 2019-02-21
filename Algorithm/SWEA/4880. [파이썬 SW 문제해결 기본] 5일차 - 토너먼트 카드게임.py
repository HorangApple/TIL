import sys
sys.stdin = open("input.txt","r")

TC=int(input())

def vs(left,right):
    result=left[0][0]-right[0][0]
    if result==1 or result==-2 :
        return left
    elif result==-1 or result==2:
        return right
    else:
        return left
    
def merge(inp,idx):
    length=len(inp)
    if len(inp)<=1:
        return [inp,idx]
    middle=(length+1)//2
    left=inp[:middle]
    right=inp[middle:]

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