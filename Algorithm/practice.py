import sys
sys.stdin = open("input.txt","r")

# def count_sort(arr,TC,k):
#    countArr=[0 for _ in range(k+1)]
#    result=[0 for _ in range(TC)]
#    for i in range(TC) :
#       countArr[arr[i]] +=1
#    for i in range(1,k+1):
#       countArr[i]+=countArr[i-1]
#    for i in range(TC):
#       result[countArr[arr[i]]-1]=arr[i]
#       countArr[arr[i]]-=1
#    return result

# TC = int(input())
# arr=[int(input()) for _ in range(TC)]

# for i in count_sort(arr,TC,max(arr)):
#    print(i)




N = int(input())
series = [0] * 10001

for i in range(N):
    a = int(sys.stdin.readline())
    series[a] = series[a] + 1

for b in range(len(series)):
    if series[b] !=0:
        for c in range(series[b]):
            print(b)