# https://www.acmicpc.net/problem/9020
import sys
sys.stdin = open("input.txt","r")

#----------------------------
import sys
sys.stdin = open("input.txt","r")

#----------------------------
def isPrime(num):
    x=num//2
    for i in range(10):
        x=(x+(num/x))/2
    for i in range(2,int(x)+1):
        if num%i==0:
            return False
    return True

def detect(val):
    half=val//2
    mini=1000000
    miniPrime=[]
    for i in range(2,half+1):
        second=val-i
        if isPrime(i) and isPrime(second):
            gap=second-i
            if mini>gap:
                mini=gap
                miniPrime=[i,second]
    return f"{miniPrime[0]} {miniPrime[1]}"

TC=int(input())
for _ in range(TC):
    val=int(input())
    print(detect(val))
#----------------------------


# 백준에서 언어를 pypy3할 때와 python3할 때의 결과가 다르다 
# 속도위주는 PyPy3를 사용하고 메모리위주는 python3를 사용하면 된다.
# 제곱근을 구하기 위해 math모듈의 sqrt를 사용하면 2972ms, 바빌로니아 법을 이용해서 구현하면 4840ms 걸린다.
# 바빌로니아 법 https://www.codeproject.com/Articles/69941/Best-Square-Root-Method-Algorithm-Function-Precisi