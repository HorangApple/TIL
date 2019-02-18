# https://www.acmicpc.net/problem/1427
import sys
sys.stdin = open("input.txt","r")

count=[0]*10
result=""
for i in input():
    count[int(i)]+=1

for i in range(9,-1,-1):
    for _ in range(count[i]):
        result+=str(i)

print(result)