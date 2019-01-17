def triangle (n):
    i = 1
    while i<=n :
        if i%3 == 0:
            print(" "*(n-i)+"*****"*)
        elif (i-2)%3 == 0 :
            print(" "*(n-i)+"* *")
        else :    
            print(" "*(n-i)+"*")
        i+=1

triangle(6)