num = int(input())
count = 0

def gapgap (num):
    num = [int(x) for x in str(num)]
    if len(num)<3 :
        return 1
    else:
        i = 0
        while i < len(num)-2 :
            gap = num[i+1]-num[i]
            if num[i+1]+gap != num[i+2] :
                return 0
            i+=1
        return 1

for n in range(1,num+1):
    count+=gapgap(n)

print(count)