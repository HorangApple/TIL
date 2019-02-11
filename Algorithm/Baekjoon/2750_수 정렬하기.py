import sys
sys.stdin = open("input.txt","r")

TC = int(input())
numlist = []
for i in range(TC):
   n = int(input())
   numlist.append(n)

for _ in range(TC):
    for i in range(TC-1):
        if numlist[i] > numlist[i+1] :
            numlist[i], numlist[i+1] = numlist[i+1], numlist[i]
for i in numlist:
    print(i)