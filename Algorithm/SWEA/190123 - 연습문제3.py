array = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
result = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
sortList = list(range(1,26))

allList = []
for i in array :
    allList += i

for i in range(len(allList)-1, 0, -1):
    for j in range(0,i):
        if allList[j] > allList[j+1]:
            allList[j], allList[j+1] = allList[j+1], allList[j]
            
sortList = allList[:]
numcount=0        
for i in range(5) :
    if i % 2 ==0:
        for j in range(i//2,5-i//2) :
            result[i//2][j]=sortList[numcount]
            numcount+=1
        else:
            numcount-=1
        for k in range(i//2,5-i//2):
            result[k][4-i//2]=sortList[numcount]
            numcount+=1     
    else:
        for j in range(3-i//2,-1+i//2,-1) :
            result[4-i//2][j]=sortList[numcount]
            numcount+=1
        else:
            numcount-=1
        for k in range(4-i//2,i//2,-1):
            result[k][0+i//2]=sortList[numcount]
            numcount+=1

for i in result :
    print(i)

# # 선생님 코드
# ary = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]

# x, y = 0,0
# dx = [0,1,0,-1]
# dy=[1,0,-1,0]
# dir_stat = 0
# for i in range(25) :
#     cur_min = sel_min()
#     sorted_ary[x][y] = cur_min
#     x+=dx[dir_stat]
#     y+=dy[dir_stat]
