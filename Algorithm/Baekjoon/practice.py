num = int(input())
lists = [0]*num
result = []
for i in range(num) :
    lists[i] = input()

for i in lists :
    before = " "
    total = 0
    for j in range(len(i)) :
        if before == i[j] and "X" != i[j] :
            count +=1
            total += count
        elif "O" == i[j]:
            count = 1
            total += count
            before = "O"
        else :
            count = 0
            before = "X"
    result.append(total)

for i in result :
    print(i)