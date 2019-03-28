import sys
sys.stdin = open('input.txt','r')

def back(k,distance,cnt):
    global mini, charge
    if distance == inp[0]:
        if mini>cnt-1:
            mini = cnt-1
            return
    elif distance > inp[0]:
        return
    else:
        k+=1
        for i in range(distance+1,distance+inp[distance]+1):
            cnt+=1
            if mini>cnt-1:
                back(k,i,cnt)
            cnt-=1

TC = int(input())
for num in range(1,TC+1):
    inp = list(map(int,input().split()))
    busStop = list(range(inp[0]))
    distance = 1
    mini = 99999999999
    charge = 0
    cnt=0
    back(0,distance,cnt)
    print(f"#{num}",mini)