tc = int(input())

def com (dist) :
    count = 0
    n=0
    if dist == 0:
        return 0
    for i in range(dist) :
        if i**2<dist and dist<(i+1)**2 :
            n=i
            break
        elif i**2 == dist :
            count = 2*i-1
            return count
    count = 2*n-1
    for i in range(0,n+1) :
        for j in range(0,n+1) :
            if dist-n**2-i-j == 0 :
                count+=1
                return count
        count+=2        
        return count
                

for c in range(tc) :
    x, y = map(int,input().split())
    dist=y-x
    print(com(dist))
    
