case = int(input())
lists = []
for i in range(case) :
    lists.append(input())

counting= 0


for i in lists :
    before = i[0]
    review = []
    breakout = False
    for j in i:
        if j != before and j in review :
            breakout = True
            break
        else :
            review.append(j)
            before = j
    if breakout == False:
        counting +=1

print(counting)