def triangle (n):
    dic = {0:"*", 1:"* *", 2:"*****"}
    
    for i in range(0,n):
        print(" "*(n-i-1)+dic[i%3])

n = int(input())

triangle(n)

