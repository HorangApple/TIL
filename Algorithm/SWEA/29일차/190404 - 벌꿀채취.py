import sys
sys.stdin = open('input.txt','r')


def go(n):
    result=[]
    for i in range(1,1<<n):
        one=[]
        for j in range(n):
            if i & 1<<j:
                one.append(j)
        result+=[one]
    return result

def solution(y1,x1,end1):
    global maxi
    for y2 in range(n):
        for x2 in range(n):
            end2=x2+m-1
            if end2>=n:
                break
            if y1==y2 and (x2 in list(range(x1,end1+1)) or end2 in list(range(x1,end1+1))):
                continue
           
            maxi1,maxi2=0,0
            one1=mp[y1][x1:end1+1]
            for i in johap:
                total=0
                result=0
                for j in i:
                    total+=one1[j]
                    if total>c:
                        break
                    result+=one1[j]*one1[j]
                else:
                    maxi1=max(maxi1,result)
            one2=mp[y2][x2:end2+1]
            for i in johap:
                total=0
                result=0
                for j in i:
                    total+=one2[j]
                    if total>c:
                        break
                    result+=one2[j]*one2[j]
                else:
                    maxi2=max(maxi2,result)
            maxi=max(maxi,maxi1+maxi2)

TC = int(input())
for num in range(1,TC+1):
    n,m,c= map(int,input().split()) # m: 벌통 선택 수, c: 최대 꿀 수확
    mp=[list(map(int,input().split())) for _ in range(n)]
    maxi=-1
    johap=go(m)

    for y1 in range(n):
        for x1 in range(n):
            end1=x1+m-1
            if end1>=n:
                break
            solution(y1,x1,end1)
    print(f'#{num}',maxi)