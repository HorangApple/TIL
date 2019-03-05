import sys
sys.stdin = open("input.txt","r")

row,column=map(int,input().split())
row=list(range(1,row+1))
column=list(range(1,column+1))
pointCnt=int(input())
rowCut=[]
columnCut=[]
for _ in range(pointCnt):
    cut=list(map(int,input().split()))
    if cut[0]==0:
        rowCut.append(cut[1])
    else :
        columnCut.append(cut[1])
rowCut.sort()
columnCut.sort()
rowlength=[]
rowsave=[]
for i in columnCut:
    if rowsave:
        obj=rowlength.pop()
        l=obj[:(i-rowsave[-1])]
        r=obj[(i-rowsave[-1]):]
        rowsave.append(i)
        rowlength.append(l)
        rowlength.append(r)
    else:
        l=row[:i]
        r=row[i:]
        rowsave.append(i)
        rowlength.append(l)
        rowlength.append(r)

columnlength=[]
columnsave=[]
for i in rowCut:
    if columnsave:
        obj=columnlength.pop()
        l=obj[:(i-columnsave[-1])]
        r=obj[(i-columnsave[-1]):]
        columnsave.append(i)
        columnlength.append(l)
        columnlength.append(r)
    else:
        l=column[:i]
        r=column[i:]
        columnsave.append(i)
        columnlength.append(l)
        columnlength.append(r)
result1=[]
result2=[]
for i in rowlength:
    result1.append(len(i))
for i in columnlength:
    result2.append(len(i))
print(max(result1)*max(result2))