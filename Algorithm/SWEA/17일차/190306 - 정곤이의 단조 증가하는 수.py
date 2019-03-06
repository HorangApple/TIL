import sys
sys.stdin = open("input.txt","r")

T=int(input())
for num in range(1,T+1):
    n=int(input())
    a=list(map(int,input().split()))
    result=[]
    obj=[]
    for i in range(n):
        for j in a[i+1:]:
            obj.append(a[i]*j)
    for i in obj:
        before=str(i)[0]
        for j in str(i)[1:]:
            if int(before)>int(j):
                break
            before=j
        else:
            result.append(i)

    if len(result)==0 or max(result)<10:
        print("#{} {}".format(num,-1))
    else :
        print("#{} {}".format(num, max(result)))