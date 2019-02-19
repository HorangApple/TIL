# https://www.acmicpc.net/problem/4948
import sys
sys.stdin = open("input.txt","r")
import time
start_time = time.time() 
#----------------------------
# # 에라토스테네스 체
# while True:
#     a=int(input())
#     if a==0:
#         break
#     b=2*a
#     p=1
#     while True:
#         if b>p**2:
#             p+=1
#         else:
#             break
#     count=0
#     for i in range(a+1,b+1):
#         for j in range(2,p+1):
#             if (i!=j and i%j==0) or i==1:
#                 break
#         else:
#             count+=1    
#     print(count)

# 6n-1,6n+1
def converter(n):
    a6=n//6
    b6=(2*n)//6
    p=1

    if 2*n==2:
        prelist=[2]
    elif 2*n==4:
        prelist=[3]
    else:
        prelist=[]

    while True:
        if 2*n>p**2:
            p+=1
        else:
            break
    for i in range(a6,b6+2):
        val1=i*6-1
        val2=i*6+1
        if val1 > n and val1 <= 2*n:
            prelist.append(val1)
        if val2 <= 2*n and val2 > n:
            prelist.append(val2)
    count=0
    for i in prelist:
        for j in range(2,p+1):
            if (i!=j and i%j==0) or i==1:
                break
        else:
            count+=1
    print(count)
    

while True:
    n=int(input())
    if n!=0:
        converter(n)
    else:
        break
#----------------------------
print(f"--- {float(time.time() - start_time)*1000:0.4f} ms ---")

# pypy3로만 통과, python3은 시간초과