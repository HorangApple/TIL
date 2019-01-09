x,y = map(int, input().split())

def dayOut (x,y) :
    lastday31=[1, 3, 5, 7, 8, 10, 12]
    lastday30=[4, 6, 9, 11]
    day=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT','SUN']
    totalDay = 0
    for i in range(1,x) :
        if i in lastday31 :
            totalDay += 31
        elif i in lastday30 :
            totalDay += 30
        else :
            totalDay += 28
    totalDay += y
    return day[totalDay%7-1]

print(dayOut(x,y))