inp = int(input())

def search(inp):
    n=1
    result = []
    lists = []
    while True:
        for i in range(1,n+1):
            lists.append(i)
        if n%2 !=0 :
            lists.reverse()
        result += lists
        if len(result) >= inp :
            return f'{result[inp-1]}/{n+1-result[inp-1]}'
        lists.clear()
        n+=1

print(search(inp))