caseNum = int(input())
lists=[]

for i in range(caseNum):
    lists.append(list(map(int, input().split())))

def ter(lists):
    d = (lists[0]-lists[3])**2+(lists[1]-lists[4])**2
    minus =(lists[2]-lists[5])**2
    plus = (lists[2]+lists[5])**2
    if d == 0 and minus == 0 :
        return -1  
    elif d == plus or d == minus :
        return 1
    elif d < plus and d > minus :
        return 2 
    elif d > plus or minus> d or d==0:
        return 0

for i in lists :
    print(ter(i))