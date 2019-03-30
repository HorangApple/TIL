import sys
sys.stdin = open("input.txt","r")
'''
def solution(k,total):
    global mini
    if k>12:
        if mini>total:
            mini=total
    else:
        if date[k]>0:
            i=0
            while i<3:
                if i==0:
                    total += date[k]*cost[i]
                    k+=1
                elif i==1:
                    total += cost[i]
                    k+=1
                else :
                    total += cost[i]
                    k+=3
                if total<mini:
                    solution(k,total)
                if i==0:
                    k-=1
                    total -= date[k]*cost[i]
                elif i==1:
                    k-=1
                    total -= cost[i]
                else :
                    k-=3
                    total -= cost[i]
                i+=1
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


# 선생님 코드
T = int(input())
for tc in range(1,T+1):
    day, month, quarter, year = map(int, input().split())
    arr = list(map(int, input().split()))
    MIN = year

    def calc(n, cost): # 월, 이용료
        global MIN
        if n >= 12:
            MIN =  min(MIN,cost)
            return
        
        if arr[n] == 0:
            calc(n+1, cost)
        else:
            calc(n+1, cost + day * arr[n])
            calc(n+1, cost + month)
            calc(n+3, cost + quarter)
            
    calc(0,0)
    print(MIN)
'''

# 선생님 코드보고 수정
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