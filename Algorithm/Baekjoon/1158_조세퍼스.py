# https://www.acmicpc.net/problem/1158
import sys
sys.stdin=open('input.txt','r')

# pop(0)의 경우 가장 앞의 요소를 pop하는 대신에 전체 리스트를 전부 왼쪽으로 이동(shift)시키는 작업이 동반되는 O(N)의 작업
# 그렇기에 되도록이면 pop을 사용하지 않고 직접 구현하는 것이 좋음.
class CircleQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.queue= [0] * (n + 1)

    def isEmpty(self):  # 공백상태
        return self.front == self.rear

    def isFull(self):  # 포화상태
        return (self.rear + 1) % len(self.queue) == self.front

    def enQueue(self,item):  # 삽입
        if self.isFull():
            print("Queue_Full")
        else:
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = item

    def deQueue(self):  # 삭제
        if self.isEmpty(): print("Queue_Empty")
        else:
            self.front = (self.front + 1) % len(self.queue)
            return self.queue[self.front]

n,m=map(int,input().split())
q=CircleQueue()
people=list(range(1,n+1))
for i in people:
    q.enQueue(i)
result="<"
idx=m-1
while True:
    # Queue를 이용해 제거하고자 하는 숫자를 맨 앞에다 배치를 시킨다.
    for i in range(m - 1):
        q.enQueue(q.deQueue())
    # 제거하면서 결과에 추가시킨다.
    result += str(q.deQueue())
    if not q.isEmpty():
        result += ", "
    else:
        result += ">"
        break

print(result)
