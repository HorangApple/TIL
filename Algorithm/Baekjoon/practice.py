def my_sqrt(x) :
    
    a = x -1
    b = x
    while True :
        if a**2>x:
            a = a-1
        else :
            break

    while True :
        new = (a+b)/2
        if a**2 < new**2 and new**2 < x :
            a = new
        else :
            b = new
        if round(a,3) == round(b,3):
            return round(a,3)

print(my_sqrt(3))