"""
문제1
다음 소스 코드를 완성하여 1부터 100까지의 숫자를 출력하면서 2의 배수일 때는 'Fizz', 11의 배수일 때는 'Buzz', 2와 11의 공배수일 때는 'FizzBuzz'가 출력되게 만드세요.
"""
for i in range(1,101) :
    if i%2==0 and i%11==0 :
        print(f'{i}, FizzBuzz')
    elif i%2==0 :
        print(f'{i}, Fizz')
    elif i%11==0 :
        print(f'{i}, Buzz')
    else :
        print(f'{i}')

"""
문제2
사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하세요.
"""
values = input()
lists = values.split()
print(max(list(map(int, lists))))

num1 = int(input('input number1 : '))
num2 = int(input('input number2 : '))
num3 = int(input('input number3 : '))

if num1 > num2:
    max_num = num1
else :
    max_num = num2
if max_num > num3 :
    print(max_num)
else :
    max_num = num3
    print(max_num)

"""
문제3
다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터입니다. 각 혈액형 별 학생 수를 딕셔너리형태로 구하세요.
"""
# 풀이1
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
total = {"A":0, "B":0, "O":0, "AB":0}

for i in blood_types :
    if i=='A':
        total['A']+=1
    elif i=='B':
        total['B']+=1
    elif i=='AB':
        total['AB']+=1
    else :
        total['O']+=1
print(total)

# 풀이2
result = {}
for blood_type in blood_types :
    if blood_type in result:
        result[blood_type] += 1
    else :
        result[blood_type] = 1
print(result)

"""
문제4
다음 리스트의 요소값 중에서 중복되는 값만 뽑아서 새로운 리스트로 옮기고 요소의 개수를 출력하세요.

some_lists = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
"""
# 풀이1
some_lists = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
noOverlap = list(set(some_lists))
print(len(noOverlap))
# 풀이2
some_lists = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
lists = []
for some_list in some_lists :
    if some_list not in lists :
        lists.append(some_list)
print(len(lists))

"""
문제5
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 네 과목의 평균 점수가 80점 이상일 때 합격이라고 정했습니다. 
평균 점수에 따라 '합격', '불합격'을 출력하는 프로그램을 만드세요. 단, 점수는 0점부터 100점까지만 입력받을 수 있으며 
범위를 벗어났다면 '잘못된 점수'를 출력하고 합격, 불합격 여부는 출력하지 않아야 합니다.
"""
scores = []
subject = ['국어','영어','수학','과학']
for i in subject :
    score = int(input(f"{i} 점수 입력 : "))
    if score >=0 and score <=100 :
        scores.append(score)
    else :
        print('잘못된 점수')
ave = sum(scores)/4
if ave >= 80 :
    print('합격')
else :
    print('불합격')

kor, eng, math, sci = map(int, input().split())
average = (kor + eng + math + sci) / 4

if 0<=kor <= 100 and 0<= eng <= 100 and 0<= math <= 100 and 0<= sci <= 100:
    if average>= 80:
        print('합격')
    else :
        print('불합격')