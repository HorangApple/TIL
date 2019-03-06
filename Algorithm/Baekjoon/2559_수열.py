# https://www.acmicpc.net/problem/2559
import sys
sys.stdin = open("input.txt","r")

n,k=map(int,input().split())
inp=list(map(int,input().split()))
result=[sum(inp[0:k])]
for i in range(n-k):
    result.append(result[-1]-inp[i]+inp[i+k])

print(max(result))