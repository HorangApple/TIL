import sys
sys.stdin=open('input.txt','r')

def searchMax():
    maxImp=0
    maxPrint=0
    for i in range(len(importance)):
        if importance[i]>maxImp:
            maxImp=importance[i]
            maxPrint=printList[i]

    return [maxPrint,maxImp]

TC=int(input())
for num in range(1,TC+1):
    n,m = map(int,input().split())
    printList=list(range(n))
    importance=list(map(int,input().split()))
    popObj = searchMax()
    cnt=1
    while True:
        if importance[0]==popObj[1] and printList[0]==popObj[0]:
            if printList[0] == m:
                break
            printList.pop(0)
            importance.pop(0)
            popObj = searchMax()
            cnt+=1
        else:
            printList.append(printList.pop(0))
            importance.append(importance.pop(0))
    print(cnt)