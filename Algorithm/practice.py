import sys
sys.stdin = open("input.txt","r")

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

TC = int(input())
arr = [0 for _ in range(2000001)]

for _ in range(TC):
   idx = int(input())
   arr[idx+1000000] = idx
count = 0
for i in arr[1:] :
   if i != 0:
      print(i)
      count+=1
   if count == TC :
      break