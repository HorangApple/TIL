tc = int(input())

for i in range(tc) :
    x, y = map(int,input().split())
    firststep=[1]
    sums = [1]
    result=[0]
    value=[0]
    nextstage=[]
    nextsum =[]
    for i in range(y-x):
        # 다음 발판 목록 출력
        for j, k in zip(firststep,sums):
            if j-1 != 0 :
                nextstage += [j-1,j,j+1]
                nextsum += [k+j-1,k+j,k+j+1]
            else :
                nextstage += [j,j+1]
                nextsum += [k+j,k+j+1]
        for x,y in zip(nextstage, nextsum) :
            if x == 1 and y not in result :
                result.append(y)
        firststep=nextstage
        sums =nextsum
        print(nextstage)
        print(sums)
        nextstage=[]
        nextsum =[]

    print(f'{result}')