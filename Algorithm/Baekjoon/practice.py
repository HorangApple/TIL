def bandname(n):
    first = n[0].upper()
    if n[0]==n[-1]:
        newname = first + n[1:len(n)]+n
    else :
        newname = 'The '+ first + n[1:len(n)]
    return newname

print(bandname("dolphin"))
print(bandname("alaska"))