n = int(input())
lists = []
for i in range(n) :
         lists.append(list(map(int, input().split())))

def realization (n, lists) :
        result = []
        for i in lists :
                average = sum(i[1:len(i)])/(len(i)-1)
                count = 0
                for j in i[1:len(i)] :     
                        if j>average :
                                count += 1
                result.append(round(count/(len(i)-1)*100,3))
        return result
                     

for i in realization(n, lists) :
        print('{:0.3f}%'.format(i))