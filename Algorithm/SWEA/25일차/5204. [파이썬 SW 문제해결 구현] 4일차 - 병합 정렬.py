import sys
sys.stdin = open('input.txt','r')

# def merge(l,r):
#     i, j = 0, 0
#     lengthL = len(l)
#     lengthR = len(r)
#     result =[0]*(lengthL+lengthR)
#     while i<lengthL and j<lengthR :
#         if l[i]<r[j]:
#             result[i+j]=l[i]
#             i+=1
#         else:
#             result[i+j]=r[j]
#             j+=1
#     if i != lengthL:
#         while i<lengthL:
#             result[i+j]=l[i]
#             i+=1
#     if j != lengthR:
#         while j<lengthR:
#             result[i+j]=r[j]
#             j+=1
#     return result

# def solution(inp):
#     global cnt
#     length=len(inp)
#     if length==1:
#         return inp
#     halfLength = length//2
#     l = solution(inp[:halfLength])
#     r = solution(inp[halfLength:])
#     if l[-1] > r[-1]:
#         cnt+=1
#     return merge(l,r)

# TC = int(input())
# for num in range(1,TC+1):
#     n = int(input())
#     inp = list(map(int, input().split()))
#     cnt=0
#     print(f"#{num}",solution(inp)[n//2], cnt)


def solution(inp):
    global cnt
    length=len(inp)
    if length==1:
        return inp
    elif length==2:
        if inp[0]>inp[1]:
            cnt+=1
            inp[0],inp[1] = inp[1],inp[0]
        return inp
    halfLength = length//2
    l = solution(inp[:halfLength])
    r = solution(inp[halfLength:])
    if l[-1] > r[-1]:
        cnt+=1
    return sorted(l+r)

TC = int(input())
for num in range(1,TC+1):
    n = int(input())
    inp = list(map(int, input().split()))
    cnt=0
    print(f"#{num}",solution(inp)[n//2], cnt)