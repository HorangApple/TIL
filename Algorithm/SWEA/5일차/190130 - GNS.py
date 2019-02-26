import sys
sys.stdin = open("input.txt","r")
# 딕셔너리 활용
numDict = {'ZRO':0, 'ONE':1, 'TWO':2,'THR':3,
    'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9} 
T=int(input())
for i in range(T):
    TC, n = input().split()
    inputList = input().split()
    result=""
    print(f'{TC}')
    numList = [0,0,0,0,0,0,0,0,0,0]
    numName = list(numDict.keys())
    for idx in inputList:
        numList[numDict[idx]] += 1
    for idx in range(0,10):
        result += (numName[idx]+" ")*numList[idx]
    print(result)

# 리스트 활용
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

# 선생님 코드

# import sys
# sys.stdin = open("input.txt", "r")

numidx = [[0] * 100 for _ in range(100)]
numidx[ord('Z')][ord('R')] = 0
numidx[ord('O')][ord('N')] = 1
numidx[ord('T')][ord('W')] = 2
numidx[ord('T')][ord('H')] = 3
numidx[ord('F')][ord('O')] = 4
numidx[ord('F')][ord('I')] = 5
numidx[ord('S')][ord('I')] = 6
numidx[ord('S')][ord('V')] = 7
numidx[ord('E')][ord('G')] = 8
numidx[ord('N')][ord('I')] = 9

p = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]

TC = int(input())

for tc in range(1, TC + 1):

    temp = input()
    nums = input().split()

    cnt = [0] * 10

    for num in nums:
        cnt[numidx[ord(num[0])][ord(num[1])]] += 1

    ans = ''
    for i in range(10):
        ans += p[i] * cnt[i]
    print("#%d "%tc, ans)