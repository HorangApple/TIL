inp = int(input())
first = [1,2,3,4,5,6]
search=[]
def com (inp):
    n=1
    startnum = 1
    while True :
        for a in first :
            search.append(1+int((n-1)*(2*a+(n-2)*6)/2))
        endnum = search[-1]
        if inp <= endnum and inp >= startnum:
            return n
        startnum = endnum
        search.clear()
        n+=1
print(com(inp))