import sys
sys.stdin = open('test.txt', 'r')

import collections

rings = [collections.deque((map("".join,input()))) for _ in range(4)]
k = int(input())
orders = [list(map(int,input().split())) for _ in range(k)]
def test():
    for i in rings:
        print(i)
    print()

def process(order):
    stack = []
    for i in range(order[0]-1,3):
        if rings[i][2] != rings[i+1][6] :
            stack.append(i+1)
        else:
            break
    change = order[1]
    for i in stack:
        change = -change
        rings[i].rotate(change)

    stack.clear()
    for i in range(order[0]-1,0,-1):
        if rings[i][6] != rings[i-1][2] :
            stack.append(i-1)
        else:
            break
    change = order[1]
    for i in stack:
        change = -change
        rings[i].rotate(change)

    rings[order[0] - 1].rotate(order[1])

def cnt():
    total = 0
    for i in range(4):
        if rings[i][0]=='1':
            total += 2**i
    print(total)
# print("시작")
# test()
for order in orders:
    process(order)
    # print('변환')
    # test()
cnt()