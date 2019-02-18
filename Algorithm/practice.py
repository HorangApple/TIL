# https://www.acmicpc.net/problem/1929
import sys
sys.stdin = open("input.txt","r")
import time
start_time = time.time() 
#----------------------------

a, b=map(int,input().split())
p=1
while True:
    if b>p**2:
        p+=1
    else:
        break
cnt=0
for i in range(a,b+1):
    for j in range(2,p+1):
        if (i!=j and i%j==0) or i==1:
            break
    else:
        print(i)     
    cnt+=1

#----------------------------
print(f"--- {float(time.time() - start_time)*1000:0.4f} ms ---")