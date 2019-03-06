import sys
sys.stdin = open("input.txt","r")

TC=int(input())
for num in range(1,TC+1):
    n=int(input())
    oneline=[1]
    print("#{}".format(num))
    print(oneline[0])
    for i in range(n-1):
        if len(oneline)-1 == 0 :
            oneline+=[1]
            for i in oneline:
                print(str(i),end=" ")
            print()
        else:
            sums=[]
            for j in range(len(oneline)-1):
                sums.append(oneline[j]+oneline[j+1])
            oneline=[1]+sums+[1]
            for i in oneline:
                print(str(i),end=" ")
            print()
