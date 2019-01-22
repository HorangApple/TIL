inp = int(input())
first = [1,2,3,4,5,6]
search=[]
def com (inp):
    n=1
    while True :
        for a in first :
            search.append(1+int((n-1)*(2*a+(n-2)*6)/2))
        if inp <= max(search) and inp >= min(search):
            return n
        search.clear()
        n+=1
print(com(inp))