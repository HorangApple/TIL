N,X = map(int, input().split())
lists = list(input().split())
result = []
for i in lists :
    if int(i)<X :
        result.append(i)

print(" ".join(result))