import sys
sys.stdin = open('input.txt','r')

def converter(inp):
    value = float(inp)
    cnt = 0
    result=[]
    while cnt < 13:
        if value==0:
            return "".join(result)
        double=value*2
        result.append(str(double)[0])
        if double>=1:
            value=double-1
        else:
            value=double
        cnt+=1
    else:
        return "overflow"

TC = int(input())
for num in range(1, TC+1):
    inp = input()
    
    print(f"#{num} {converter(inp)}")
