import sys
sys.stdin = open("input.txt","r")

inp = int(input())

f0 = 0
f1 = 1
i=0
if inp==1:
  print(1)
else:
  while i<inp-1:
    f2 = f0+f1
    f0 = f1
    f1 = f2
    i+=1

  print(f2)