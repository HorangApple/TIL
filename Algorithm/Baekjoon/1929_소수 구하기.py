# https://www.acmicpc.net/problem/1929
import sys
sys.stdin = open("input.txt","r")
import time
start_time = time.time() 
#----------------------------
# # 에라토스테네스 체
# a, b=map(int,input().split())
# p=1
# while True:
#     if b>p**2:
#         p+=1
#     else:
#         break
# for i in range(a,b+1):
#     for j in range(2,p+1):
#         if (i!=j and i%j==0) or i==1:
#             break
#     else:
#         print(i)     

# 6n-1,6n+1
def converter(a,b):
    a6=a//6
    b6=b//6
    p=1
    if a==3:
        prelist=[3]
    elif a<3:
        prelist=[2,3]
    else :
        prelist=[]

    while True:
        if b>p**2:
            p+=1
        else:
            break
    for i in range(a6,b6+2):
        val1=i*6-1
        val2=i*6+1
        if val1 >= a and val1 <= b:
            prelist.append(val1)
        if val2 <= b and val2 >= a:
            prelist.append(val2)
    for i in prelist:
        for j in range(2,p+1):
            if (i!=j and i%j==0) or i==1:
                break
        else:
            print(i)

a, b=map(int,input().split())
converter(a,b)
#----------------------------
print(f"--- {float(time.time() - start_time)*1000:0.4f} ms ---")

# 백준에서 언어를 pypy3할 때와 python3할 때의 결과가 다르다 
# 속도위주는 PyPy3를 사용하고 메모리위주는 python3를 사용하면 된다.