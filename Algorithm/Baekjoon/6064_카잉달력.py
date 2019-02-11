import sys
sys.stdin = open("input.txt","r")

TC = int(input())

for i in range(TC):
    m,n,x,y = map(int, input().split())
    count = 1
    xC, yC = 1, 1
    save = 0
    gap = m-n
    while xC != x :
        xC+=1
        yC+=1
        if xC > m :
            xC = 1
        if yC > n:
            yC = 1
        count += 1
    save = yC
    
    while yC != y : 
        if gap > 0 :
            yC += (gap%n)
        else :
            yC -= (abs(gap)%n)
        count += m
        if yC > n :
            yC-=n
        elif yC < 1 :
            yC+=n
        if yC == save :
            count = -1
            break
        
    print(count)