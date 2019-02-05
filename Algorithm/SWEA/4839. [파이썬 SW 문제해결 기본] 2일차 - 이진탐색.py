import sys
sys.stdin = open("input.txt","r")

def search (l,p,inp,count):
    count+=1
    c=(l+p)//2
    if c>inp:
        return search(l,c,inp,count)
    elif c<inp:
        return search(c,p,inp,count)
    else:
        return count


T=int(input())

for i in range(T):
    # p : 전체쪽수, a : A가 찾아야할 쪽수, b : B가 찾아야할 쪽수
    p,a,b = map(int, input().split())
    l=1
    count = 0
    countA = search(l,p,a,count)
    countB = search(l,p,b,count)
    
    if countA > countB :
        result = 'B'
    elif countA < countB :
        result = 'A'
    else :
        result = 0
    print(f'#{i+1} {result}')


# 선생님 코드
def binarySearch(n, key):
    l = 1
    r = n
    cnt = 0

    while 1 :
        mid = int((l + r) / 2)
        cnt += 1

        if mid == key:
            break
        if mid < key:
            l = mid
        else :
            r = mid
    return cnt

TC = int(input())
for tc in range(1, TC+1):
    pages, key1, key2 = map(int, input().split())
    cnta = binarySearch(pages, key1)
    cntb = binarySearch(pages, key2)

    result = '0'
    if cnta < cntb:
        result = 'A'
    elif cnta > cntb:
        result = 'B'

    print('#%d %c'%(tc, result))