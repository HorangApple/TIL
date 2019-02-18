# https://www.acmicpc.net/problem/2108
import sys
sys.stdin = open("input.txt","r")
import random
# random.randrange(-4000,4000)

import sys
# 음수 반올림이 까다로웠다
def sansul(valuelist):
    total=0
    count=0
    for i in valuelist:
        total+=i
        count+=1
    div=total/count
    mok=total//count
    point=div-mok
    if div>0 and point>=0.5 :
        result=div-point+1
    elif div<0 and 1-point>=0.5:
        result=div-point
    else:
        result=div
    result=int(result)
    return result

def middle(valuelist):
    if len(valuelist)==1:
        return valuelist[0]
    sort=sorted(valuelist)
    return sort[TC//2]

# 4개의 함수 중 가장 시간이 많이 걸리는 함수
def manyCount(valuelist):
    sort=[0]*8002
    maxvalue=0
    maxlist=[]
    for i in valuelist:
        sort[i+4000]+=1
        if maxvalue<sort[i+4000]:
            maxvalue=sort[i+4000]
            maxlist.clear()
            maxlist.append(i)
        elif maxvalue==sort[i+4000]:
            maxlist.append(i)
    if len(maxlist)>1 :
        return sorted(maxlist)[1]
    else :
        return maxlist[0]

def valueRange(valuelist):
    return max(valuelist)-min(valuelist)

TC = int(input())
# TC = 500000
valuelist=[]
for t in range(TC) :
    valuelist.append(int(sys.stdin.readline()))
    # valuelist.append(random.randrange(-4000,4000))
print(sansul(valuelist))
print(middle(valuelist))
print(manyCount(valuelist))
print(valueRange(valuelist))