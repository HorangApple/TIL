def converter(v):
    cnt=0
    result=0
    for i in v[::-1]:
        if int(i)>0:
            result+=2**cnt
        cnt+=1 
    return result


dic = {
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

inp1="01D06079861D79F99F"
inp=""
for i in inp1:
    inp+=dic[i]

divided = []
for i in range(len(inp)//7):
    divided.append(inp[7*i:7*(i+1)])

for i in divided:
    print(converter(i), end=" ")
print()