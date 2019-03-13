# deque를 쓰면 빠르게 작동시킬 수 있다.
# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
#python3
#import atexit
# from queue import Queue
# from collections import deque
# from time import time, strftime, localtime
# from datetime import timedelta
# SIZE = 300000
# class myQ:
#     def __init__(self, size):
#         self.arr = [0] * size
#         self.front = -1
#         self.rear = -1
#
#     def push(self, item):
#         self.rear += 1
#         self.arr[self.rear] = item
#
#     def pop(self):
#         self.front += 1
#         return self.arr[self.front]
#
#     def empty(self):
#         return self.front == self.rear
#
# start = 0
#
# def log(s):
#     global start
#     start = time()
#     print('시작 >>>> ', s)
#
# def endlog():
#     line = "=" * 40
#     elapsed = time() - start
#     print("실행 시간: ", elapsed)
#     print('종료 >>>> ')
#     print(line)
#
# log("List 사용")
# Q = []
# for i in range(SIZE):
#     Q.append(i)
#
# while len(Q) > 0:
#     Q.pop(0)
# endlog()
#
# log("queue.Queue 사용")
# Q = Queue()
# for i in range(SIZE):
#     Q.put(i)
#
# while not Q.empty():
#     Q.get()
# endlog()
#
# log("collections.deque 사용")
# Q = deque()
# for i in range(SIZE):
#     Q.append(i)
#
# while len(Q) > 0:
#     Q.popleft()
# endlog()
#
# log("List 인덱싱")
# Q = myQ(SIZE)
# for i in range(SIZE):
#     Q.push(i)
#
# while not Q.empty():
#     Q.pop()
# endlog()

# N-Queen 문제
# 순열 생성
# 백트래킹 - 체계적으로 모든 경우를 나열하는 방법
#         - 최적화 문제(결정)를 해결하는데 사용하기 좋다.
# 상태 공간 트리
# 문제 해결 방법 - 트리 탐색
# 높이(최대:원소의 수)와 경로 정보를 알아야한다.
# 경로는 return을 하던가 전역변수를 쓰던가 해서 현재 상태를 저장시켜놔야한다.

arr='ABC'
for i in range(3):
    for j in range(3):
        if j==i: continue
        for k in range(3):
            if k==i or k==j : continue
            print(arr[i],arr[j],arr[k])
# 재귀함수
# k: 노드의 높이, 지금까지 선택 n: 트리의 높이, 전체 선택 수
order=[0]*3 # 요소들의 인덱스 저장
used=[False]*3
def perm(k,n):
    if k==n:
        # 하나의 순열 생성
        print(order)
        return
    else:
        # 가능한 선택지 계산
        # 이미 한 선택(k개)을 확인
        for i in range(n):
            if used[i]: continue
            order[k]=i
            used[i]=True
            perm(k+1,n)
            used[i]=False

perm(0,3)

# 돌아가는 방식은 같지만 표현은 다르다.
order=[0]*3 # 요소들의 인덱스 저장
def perm(k,n,used):
    if k==n:
        # 하나의 순열 생성
        print(order)
        return
    else:
        # 가능한 선택지 계산
        # 이미 한 선택(k개)을 확인
        for i in range(n):
            if used & (1<<i): continue
            order[k]=i
            perm(k+1,n,used|(1<<i))

perm(0,3,0)

'''
n queen 문제에서 행과 열은 겹치지 않기에 처음에 행만 나열하면 
[1,],[2,],[3,],[4,]로 나열할 수 있으며 경우의 수는 4!로 조사할 수 있다.
대각선 같은 경우에는 행과 열이 절대값으로 같은 경우로 알 수 있다.
'''