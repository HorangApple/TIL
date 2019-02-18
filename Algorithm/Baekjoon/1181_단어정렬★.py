# https://www.acmicpc.net/problem/1181
import sys
sys.stdin = open("input.txt","r")
## 셀렉팅 정렬, 시간 초과
# def check(wordlist,mini,j):
#     for k in range(len(wordlist[mini])):
#         minifirst=ord(wordlist[mini][k])
#         jfirst=ord(wordlist[j][k])
#         if minifirst>jfirst:
#             return True
#         elif minifirst<jfirst:
#             return False

# TC=int(input())
# wordlist=[]
# for i in range(TC):
#     inp=input()
#     if inp not in wordlist:
#         wordlist.append(inp)
# length=len(wordlist)

# for i in range(0,length-1):
#     mini=i
#     for j in range(i+1,length):
#         if len(wordlist[mini])>len(wordlist[j]) or (len(wordlist[mini])==len(wordlist[j]) and check(wordlist,mini,j)):
#             mini=j
            
#     wordlist[i],wordlist[mini]=wordlist[mini],wordlist[i]

# for i in wordlist:
#     print(i)

# 병합정렬, 통과
def check(wordlist,l,r):
    for k in range(len(l)):
        minifirst=ord(l[k])
        jfirst=ord(r[k])
        if minifirst<jfirst:
            return True
        elif minifirst>jfirst:
            return False

def merge(l,r):
    result=[]
    i=0
    j=0
    while i<len(l) and j<len(r):
        if len(l[i])<len(r[j]) or (len(l[i])==len(r[j]) and check(wordlist,l[i],r[j])):
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
    while i<len(l):
        result.append(l[i])
        i+=1
    while j<len(r):
        result.append(r[j])
        j+=1
    return result

def mergeSort(wordlist):
    if len(wordlist)>1:
        middle=len(wordlist)//2
        left=wordlist[:middle]
        right=wordlist[middle:]
        
        l=mergeSort(left)
        r=mergeSort(right)

        return merge(l,r)
    else :
        return wordlist

TC=int(input())
wordlist=[]

for i in range(TC):
    inp=input()
    if inp not in wordlist:
        wordlist.append(inp)

for i in mergeSort(wordlist):
    print(i)