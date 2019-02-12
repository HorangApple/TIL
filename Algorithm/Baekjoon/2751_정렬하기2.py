import sys
sys.stdin = open("input.txt","r")
## 병합정렬
# def merge_sort (arr):
#    if len(arr)<=1:
#       return arr
#    midIdx=len(arr)//2
#    left,right =[],[]
#    left = arr[:midIdx]
#    right = arr[midIdx:]
#    left = merge_sort(left)
#    right = merge_sort(right)
#    return merge(left, right)

# def merge (left, right):
#    result = []
#    while len(left) > 0 or len(right) > 0:
#       if len(left) > 0 and len(right) > 0:
#          if left[0] <= right[0]:
#                result.append(left[0])
#                left = left[1:]
#          else:
#                result.append(right[0])
#                right = right[1:]
#       elif len(left) > 0:
#          result.append(left[0])
#          left = left[1:]
#       elif len(right) > 0:
#          result.append(right[0])
#          right = right[1:]
#    return result

# TC = int(input())
# arr=[0 for _ in range(TC)]
# for i in range(TC):
#    arr[i]=int(input())

# for i in merge_sort(arr):
#    print(i)

# 무식하게 풀기
TC = int(input())
arr = [0 for _ in range(2000002)]

for _ in range(TC):
   idx = int(input())
   if idx != 0 :
      arr[idx+1000000] = idx
   else :
      arr[1000000] = 1
count = 0
for i in range(len(arr)) :
   if i == 1000000 and arr[i] == 1 :
      print(0)
   elif arr[i] != 0 :
      print(arr[i])
      count+=1
   if count == TC :
      break