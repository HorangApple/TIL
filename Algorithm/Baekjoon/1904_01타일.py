import sys
sys.stdin = open("input.txt", "r")


inp = int(input())
n1 = 1
n2 = 2
if inp == 1:
    print(n1)
elif inp == 2:
    print(n2)
else:
    i = 2
    while i<inp:
        n3 = (n1+n2)%15746
        n1,n2 = n2,n3
        i+=1
    print(n3)

