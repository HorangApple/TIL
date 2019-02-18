# https://www.acmicpc.net/problem/2581
import sys
sys.stdin = open("input.txt","r")
import time
start_time = time.time() 
#----------------------------

a=int(input())
b=int(input())
numlist=list(range(a,b+1))
p=1
while True:
    if b>p**2:
        p+=1
    else:
        break
cnt=0
for i in numlist:
    for j in range(2,p+1):
        if (i!=j and i%j==0) or i==1:
            numlist[cnt]=0
            break
    cnt+=1
numSum=sum(numlist)
if numSum==0 or numSum==1:
    print(-1)
else:
    print(numSum)
    for i in numlist:
        if i>0:
            print(i)
            break

#----------------------------
print(f"--- {float(time.time() - start_time)*1000:0.4f} ms ---")

# 1은 소수가 아니니 -1이다.
# 소수는 에라토스테네스 체를 이용해 찾아서 푼다.