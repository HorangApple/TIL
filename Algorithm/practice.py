# https://www.acmicpc.net/problem/1929
import sys
sys.stdin = open("input.txt","r")
import time
start_time = time.time() 
#----------------------------
def detect(half):
    if half==2:
        return "2 2"
    elif half==3:
        return "3 3"
    elif half==4:
        return "3 5"
    elif half==5:
        return "5 5"
    elif half==6:
        return "5 7"
    else:
        if half%6==1 or half%6==5 :
            return f"{half} {half}"
        elif (half+1)%6==1 or (half+1)%6==5 :
            return f"{half-1} {half+1}"
        else:
            return f"{half-3} {half+3}"

TC=int(input())
for _ in range(TC):
    val=int(input())
    half=val//2
    print(detect(half))
#----------------------------
print(f"--- {float(time.time() - start_time)*1000:0.4f} ms ---")

# 백준에서 언어를 pypy3할 때와 python3할 때의 결과가 다르다 
# 속도위주는 PyPy3를 사용하고 메모리위주는 python3를 사용하면 된다.