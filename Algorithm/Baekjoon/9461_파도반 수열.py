import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    n = int(input())-1
    n1 = [1,1,1,2,2,3,4,5]
    if n<8:
        print(n1[n])
    else:
        for i in range(7,n):
            n2 = n1[i-4]+n1[i]
            n1.append(n2)
        print(n2)

'''
최초값이 위와 같이 길 수도 있다.
'''