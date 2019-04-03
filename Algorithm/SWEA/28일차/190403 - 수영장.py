import sys
sys.stdin = open('input.txt','r')

def solution(k,total):
    global mini
    if k>12:
        if mini>total:
            mini=total
    elif total<mini:
        if date[k]>0:
            solution(k+1,total+date[k]*cost[0])
            solution(k+1,total+cost[1])
            solution(k+3,total+cost[2])
        else:
            solution(k+1,total)

TC = int(input())
for num in range(1,TC+1):
    cost = list(map(int, input().split()))
    date = [0]+list(map(int,input().split()))
    total = 0
    mini=cost[-1]
    solution(1,total)
    print(f"#{num}",mini)