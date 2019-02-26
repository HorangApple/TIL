array = [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]

total = 0
for i in range(len(array)) :
    for j in range(len(array[i])) :
        if j+1 <len(array[i]):
            total += abs(array[i][j]-array[i][j+1])
        if j-1 >= 0:
            total += abs(array[i][j]-array[i][j-1])
        if i+1 <len(array):
            total += abs(array[i][j]-array[i+1][j])
        if i-1 >= 0:
            total += abs(array[i][j]-array[i-1][j])

print(total)


def isWall(x, y) :
    if x<0 or x>=5 : return True
    if y<0 or y>=5 : return True
    return False

def calAbs(y,x) :
    if y-x >0 : return y-x
    if x-y >0 : return x-y
    return 0
