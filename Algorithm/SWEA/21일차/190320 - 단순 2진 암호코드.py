import sys
sys.stdin = open("input.txt",'r')

dic2 ={
    '0001101':'0',
    '0011001':'1',
    '0010011':'2',
    '0111101':'3',
    '0100011':'4',
    '0110001':'5',
    '0101111':'6',
    '0111011':'7',
    '0110111':'8',
    '0001011':'9',
}

def detect ():
    a=0
    b=0
    for i in range(len(value)//2):
        a+=value[2*i]
        b+=value[2*i+1]
    result = b*3+a
    
    if result%10 == 0:
        return sum(value)
    else:
        return 0

TC = int(input())
for num in range(1,TC+1):
    n,m = map(int,input().split())
    inp = [input() for _ in range(n)]
    for i in inp:
        k=len(i)
        value=[]
        while k>0:
            if int(i)==0:
                break 
            elif i[k-7:k] in dic2:
                value.append(int(dic2[i[k-7:k]]))
                k-=7
                continue    
            k-=1
        else:
            break
    print(f"#{num} {detect()}")