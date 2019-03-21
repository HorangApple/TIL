import sys
sys.stdin = open('input.txt','r')

def chanage2to10(value):
    cnt=0
    result=0
    length=len(value)
    while cnt<length:
        tmp=length-1-cnt
        if value[tmp] !="0":
            result+=int(value[tmp])*(2**cnt)
        cnt+=1
    return result


def change10toN(value, n):
    result=[]
    while value:
        result.append(str(value%n))
        value//=n
    return "".join(result[::-1])


TC = int(input())
for num in range(1, TC+1):
    bi = input()
    tri = input()
    change=[]
    # 2진수에서 한 자리를 바꾸고 
    for i in range(len(bi)):
        change=bi[:i]+str(int(bi[i])^1)+bi[i+1:]
        biToTen = chanage2to10(change)
        biToTri = change10toN(biToTen,3)
        if len(biToTri) != len(tri):
            continue
        cnt=0
        for j in range(len(tri)):
            if biToTri[j]!=tri[j]:
                continue
            cnt+=1
        if cnt==len(tri)-1:
            print(f"#{num} {biToTen}")
            break