def converter(v):
    cnt=0
    result=0
    for i in v[::-1]:
        if int(i)>0:
            result+=2**cnt
        cnt+=1 
    return result

inp="0000000111100000011000000111100110000110000111100111100111111001100111"
divided = []
for i in range(len(inp)//7):
    divided.append(inp[7*i:7*(i+1)])

for i in divided:
    print(converter(i), end=" ")
print()