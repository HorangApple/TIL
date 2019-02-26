import sys
sys.stdin = open("input.txt","r")

TC=int(input())
def calcul(cal,top):
    if len(stack)<2:
        return -1
    b=stack.pop()
    a=stack.pop()
    caldict={'+':a+b,'-':a-b,'/':int(a/b),'*':a*b}
    stack.append(caldict[cal])
    top-=1
    return top

for num in range(1,TC+1):
    inp=input().split()
    stack=[]
    top=-1
    for i in inp[:-1]:
        if i in ['+','-','*','/']:
            top=calcul(i,top)     
        else:
            stack.append(int(i))
            top+=1
    if top==0:
        print(f'#{num} {stack.pop()}')
    else:
        print(f'#{num} error')