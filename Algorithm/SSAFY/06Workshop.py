# 풀이 1
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

#풀이 2
def my_sqrt(n) :
    x, y = 0, n
    answer = 0
    
    while abs(answer**2-n)>0.0001:
        answer = (x+y) /2
        if answer ** 2 < n :
            x = answer
        else :
            y = answer
    return answer

print(my_sqrt(5))

#풀이 3
def my_sqrt(n):
    mini, maxi = 0,1
    while 1:
        if n == maxi **2 :
            return maxi
        elif mini ** 2 < n < maxi ** 2 :
            guess = (mini + maxi) / 2
        
            if round(mini, 5) == round(maxi, 5) :
                return round(guess, 5)
            elif guess ** 2 > n :
                maxi = guess
            else :
                mini = guess
        else:
            mini += 1
            maxi += 1

print(my_sqrt(5))