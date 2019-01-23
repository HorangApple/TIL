"""
수학을 알면 머리가 편하다.
1+2+...n+n-1...+1의 값은 n^2이다.
거리차는 n^2<= y-x <(n+1)^2이고 양변에 n^2을 빼면 우변이 <2n+1로 나온다.
즉, <=2n이다. 이를 이용하여 풀었다.
"""

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
    
