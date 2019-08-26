import sys
sys.stdin = open("pratice.txt", "r")

# fm: 출발지 to: 목적지 by: 잠시 놓을 곳
def sol(n, fm, by, to):
    if n==0:
        return
    sol(n-1, fm, to, by)
    answer.append(f'{fm} {to}')
    sol(n-1, by, fm, to)
    

inp = int(input())
answer=[]
sol(inp,1,2,3)
print(len(answer))
for i in answer:
    print(i)