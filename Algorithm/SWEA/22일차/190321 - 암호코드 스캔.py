import sys
sys.stdin = open("input.txt",'r')

HexToBi = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}

def invert16to2():
    total=0
    values=[]
    for i in line16:
        result=""
        length = len(i)
        endPoint=length-1
        while endPoint>0:
            if i[endPoint]!='0':
                break
            endPoint-=1

        cnt=endPoint
        while cnt>-1:
            result=HexToBi[i[cnt]]+result
            cnt-=1

        mul=1
        k=len(result)
        value=[]
        while k>0:
            dic ={
                '000'*mul+'11'*mul+'0'*mul+'1'*mul:'0',
                '00'*mul+'11'*mul+'00'*mul+'1'*mul:'1',
                '00'*mul+'1'*mul+'00'*mul+'11'*mul:'2',
                '0'*mul+'1111'*mul+'0'*mul+'1'*mul:'3',
                '0'*mul+'1'*mul+'000'*mul+'11'*mul:'4',
                '0'*mul+'11'*mul+'000'*mul+'1'*mul:'5',
                '0'*mul+'1'*mul+'0'*mul+'1111'*mul:'6',
                '0'*mul+'111'*mul+'0'*mul+'11'*mul:'7',
                '0'*mul+'11'*mul+'0'*mul+'111'*mul:'8',
                '000'*mul+'1'*mul+'0'*mul+'11'*mul:'9',
            }
            if result[k-7*mul:k] in dic:
                value.append(int(dic[result[k-7*mul:k]]))
                k-=7*mul
                if len(value)==8 and value not in values:
                    if num==20:
                        print(i)
                        print(value)
                    values.append(value)
                    value=[]
                    mul=1
                    break
                elif len(value)==8 and value in values:
                    value=[]
                    mul=1
                continue
            elif result[k-1] =='1' and result[k-7*mul:k] not in dic:
                if mul*7>k:
                    mul=0
                mul+=1
                continue
            k-=1

    for i in values:
        total+=detect(i)
    print(total, len(values), len(line16))


def detect(value):
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
    print(f"#{num}", end=" ")
    inp = [input() for _ in range(n)]
    line16 = []
    line2 = []
    
    for i in inp:
        try:
            if int(i)==0:
                continue
        except:
            if i not in line16:
                line16.append(i)
            continue
    invert16to2()