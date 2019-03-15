# https://www.acmicpc.net/problem/11866
import sys
sys.stdin=open('input.txt','r')

n,m=map(int,input().split())
people=list(range(1,n+1))
result="<"
while True:
    # Queue를 이용해 제거하고자 하는 숫자를 맨 앞에다 배치를 시킨다.
    for i in range(m-1):
        people.append(people.pop(0))
    # 제거하면서 결과에 추가시킨다.
    result+=str(people.pop(0))
    if len(people)!=0:
        result+=", "
    else:
        result+=">"
        break
print(result)

# 일일이 인덱스를 계산하는 것보다 큐를 이용해 뽑아내고자 하는 수를 앞으로 당겨 빼는 것이 간편하다.