import sys
sys.stdin = open("input.txt","r")
# numDict = {'ZRO':0, 'ONE':1, 'TWO':2,'THR':3,
#     'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9} 
# T=int(input())
# for i in range(T):
#     TC, n = input().split()
#     inputList = input().split()
#     result=""
#     print(f'{TC}')
#     numList = [0,0,0,0,0,0,0,0,0,0]
#     numName = list(numDict.keys())
#     for idx in inputList:
#         numList[numDict[idx]] += 1
#     for idx in range(0,10):
#         result += (numName[idx]+" ")*numList[idx]
#     print(result)

numDict = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN'] 
T=int(input())
for i in range(T):
    TC, n = input().split()
    inputList = input().split()
    print(f'{TC}')
    numList = [0,0,0,0,0,0,0,0,0,0]
    for single in inputList:
        numList[numDict.index(single)] += 1
    for idx in range(0,10):
        print((numDict[idx]+" ")*numList[idx],end="")
    print("")