# https://www.acmicpc.net/problem/1874
import sys
sys.stdin = open("input.txt","r")

#----------------------------
stack=[]
answer=[]
progression=[]
plusCnt=0
minusCnt=0
TC=int(input())
for _ in range(TC):
    progression.append(int(input()))
idx=0
for i in range(1,TC+1):
    stack.append(i)
    answer.append("+")
    plusCnt+=1
    while True:
        if stack and stack[-1]==progression[idx]:
            stack.pop()
            answer.append("-")
            idx+=1
            minusCnt+=1
        else :
            break
if plusCnt==minusCnt:
    for i in answer:
        print(i)
else :
    print("NO")
#----------------------------
