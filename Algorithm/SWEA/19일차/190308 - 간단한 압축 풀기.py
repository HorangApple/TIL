import sys
sys.stdin=open('input.txt','r')

TC=int(input())
for num in range(1,TC+1):
    n=int(input())
    result=""
    for _ in range(n):
        inp=input().split()
        result+=inp[0]*(int(inp[1]))
    start=0
    print("#{}".format(num))
    for i in range(len(result)//10+1):
        print(result[start:10*(i+1)])
        start=10*(i+1)