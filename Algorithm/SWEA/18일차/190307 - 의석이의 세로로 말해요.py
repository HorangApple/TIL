import sys
sys.stdin=open('input.txt','r')
# Aa0aP Af985 Bz1Eh Cz2W3 D1gk D6x

TC=int(input())
for num in range(1,TC+1):
    inp=[input() for i in range(5)]
    length=[]
    print("#{} ".format(num),end="")
    for i in inp:
        length.append(len(i))
    for i in range(max(length)):
        for j in range(5):
            if len(inp[j])>i:
                print(inp[j][i],end="")
    print()