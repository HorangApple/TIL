"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

> 입력
1 2

> 출력
3

"""
# 풀이1
a,b = [int(x) for x in input().split()]
print(a+b)

# 풀이2
a,b = map(int, input().split())
print(a+b)

# 풀이3
nums = list(input().split())
a = int(nums[0])
b = int(nums[1])
print(a+b)

# 풀이4
nums = input().split()
total = 0
for i in nums :
    total = total + int(i)
print(total)

# map(사용할 함수명, 리스트/딕셔너리/튜플 중 하나)
# 풀이 4가지 모두 사용된 메모리는 동일하고 작동시간은 비슷하나 풀이4가 제일 늦다.