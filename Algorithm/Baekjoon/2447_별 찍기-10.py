import sys
sys.stdin = open("pratice.txt", "r")


def sol(n,stars):
    result = []
    next=n*3
    if next>inp:
        return stars
    for i in range(1,4):
        for star in stars:
            if i%2==0:
                result.append(star+' '*n+star)
            else:
                result.append(star*3)
    return sol(next,result)

inp = int(input())

res = sol(1,['*'])
for i in res:
    print(i)