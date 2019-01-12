def triangle(n):
    mixedColor = {8:'R',4:'B',2:'G',6:'G',3:'R',5:'B'}
    nColor = {'R':4, 'B':2, 'G':1}
    for i in range(len(n)-1) :
        n=[mixedColor[nColor[n[j]]+nColor[n[j+1]]] for j in range(len(n)-1) ]
    return n[0]

print(triangle('RRR'))
print(triangle('RG'))
print(triangle('RRRGGGBBBBBB'))
print(triangle('RRGBRGBB'))