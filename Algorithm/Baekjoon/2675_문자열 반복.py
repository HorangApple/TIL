case = int(input())
lists = []
for i in range(case):
    lists.append(input().split())
result = []
for i in lists :
    string = []
    for j in i[1] :
        for k in j:
            string.append(k*int(i[0]))
        if len("".join(string)) == len(i[1])*int(i[0]) :
            result.append("".join(string))
for i in result :
    print(i)