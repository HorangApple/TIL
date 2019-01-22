inp = int(input())

def search(inp):
    n=1
    beforeCom=1
    child =0
    parant = 0
    while True:
        com = int(n*(n+1)/2)
        if com > inp :
            count = n-1
            com = beforeCom
            break
        elif com == inp :
            count = n
            break
        beforeCom = com
        n+=1
    if com%2 == 0:
        
        
    print(com, count)
search(inp)