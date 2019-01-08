"""
문제1
다음 과목별 평균 점수를 구하세요. (국어:80 영어:90, 수학:100)
"""
score = {'국어':80, '영어':90, '수학':100}
total = 0
for i in list(score.values()) :
    total = total +i
print(total/len(score))

"""
문제2
주어진 리스트의 자연수들이 각각 홀수인지 짝수인지 판별하는 코드를 작성하세요. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers :
    result = '홀수' if i % 2 != 0 else '짝수'
    print(result)

"""
문제3
1부터 1000까지의 자연수 중 
5의 배수에 해당되는 자연수들의 총합을 구하는 코드를 작성하세요.
"""
total = 0
for i in range(1,1001):
    if (i%5==0):
        total+=i
    else :
        continue
print(total)

"""
문제4
for와 range 함수를 이용하여 2~9단까지 구구단을 출력하는 코드를 작성하세요.
"""
for i in range(2,10) :
    for j in range(1,10) :
        print(f'{i}*{j}={i*j}')
    print("")

"""
문제5
1부터 100까지 자연수를 각각 제곱해 더한 값인 '제곱의 합'과 
1부터 100을 먼저 더한 다음에 그 결과를 제곱한 '합의 제곱'의 
차이를 구하는 코드를 작성하세요.
"""
powTotal = 0
Total = 0
for i in range(1,101):
    powTotal +=  i**2
    Total += i
print(abs(Total**2-powTotal))