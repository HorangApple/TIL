"""
문제1
문자열 요소로만 이루어진 리스트에서 문자열 길이가 2 이상이고 주어진 문자열의 첫번째와 마지막 문자가 같은 요소를 모아 새로운 리스트를 만들고 해당 리스트 요소의 개수를 구하세요.

samples = ['level', 'asdwe', 's', 'abceda', 'gsdwrtfg'] -> 결과값: 3
"""
samples = ['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']
lists = []
for i in samples :
    if i[0]==i[-1] and len(i)>=2 :
        lists.append(i)
print(len(lists))

"""
문제2
다음 리스트에서 중복된 요소를 제거한 리스트를 출력하세요.

items = [10,20,40,20,10,30,50,60,40,80,50,40,20,30,10]
"""
# 풀이1
items = [10,20,40,20,10,30,50,60,40,80,50,40,20,30,10]
removedItems = list(set(items))
removedItems.sort() # sort 메소드는 return이 없기 때문에 독립적으로 적어야 한다.
print(removedItems)

# 풀이2
items = [10,20,40,20,10,30,50,60,40,80,50,40,20,30,10]
numbers = []
for i in items :
    if i not in numbers :
        numbers.append(i)
print(numbers)

"""
문제3
다음 리스트에서 0번째 4번째 5번째 요소를 지운 새로운 리스트를 생성하세요.

colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
"""
# 풀이1
colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
removeList = []
removeList.append(colors[0])
removeList.append(colors[4])
removeList.append(colors[5])
for i in removeList :
    colors.remove(i)
print(colors)

# 풀이2
colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
fruit = []
for color in colors :
    if colors.index(color) not in (0,4,5) :
        fruit.append(color)
print(fruit)

# 풀이3
colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
fruit = []
for a, color in enumerate(colors) :
    if a not in (0,4,5) :
        fruit.append(color)
print(fruit)

# 풀이4
colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
fruit = []
for a in colors :
    if a not in colors[0] and a not in colors[4] and a not in colors[5] :
        fruit.append(a)
print(fruit)

"""
문제4
세 정수 A, B, C가 입력값으로 주어질 때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하세요.
"""
# 풀이1
num1 = int(input('input number1 : '))
num2 = int(input('input number2 : '))
num3 = int(input('input number3 : '))

if num1 > num2:
    max_num = num1
    second_num = num2
else :
    max_num = num2
    second_num = num1
if max_num > num3 :
    if num3 >second_num :
        second_num = num3
        print(second_num)
    else :
        print(second_num)
else :
    second_num = max_num
    print(second_num)

# 풀이2
a, b, c = map(int, input().split()) # '숫자 숫자 숫자'식으로 입력
if((a>=b and b>=c) or (c>=b and b>=a)):
    print(b)
elif((b>=c and c>=a) or (a>=c and c>=b)) :
     print(c)
else :
     print(a)
"""
문제5
사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하세요. 
각 통화별 환율은 다음과 같습니다. 
(사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정합니다.)

currency = {
    'USD': 1167, 'JPY': 1.096, 'EURO': 1268, 'CNY': 171
}
"""
# 풀이1
currency = {
    'USD': 1167, 'JPY': 1.096, 'EURO': 1268, 'CNY': 171
}

userInput = input("금액과 단위를 입력하시오 : ")
lists = userInput.split()

if lists[1] == '달러' :
    exchange = int(lists[0])*currency['USD']
    print(f'{exchange} 원')
elif lists[1] == '엔' :
    exchange = int(lists[0])*currency['JPY']
    print(f'{exchange:0.1f} 원')
elif lists[1] == '유로' :
    exchange = int(lists[0])*currency['EURO']
    print(f'{exchange} 원')
elif lists[1] == '위안' :
    exchange = int(lists[0])*currency['CNY']
    print(f'{exchange} 원')
else :
    print('잘못된 입력입니다.')

# 풀이2
user_in = input("금액을 입력해주세요: ").split()
amount = user_in[0]
currency = user_in[1]

if currency == '달러':
    ratio = 1167
elif currency == '엔' :
    ratio = 1.096
elif currency == '유로' :
    ratio = 1268
else :
    ratio = 171
print(ratio*int(amount),"원")

# 풀이3
currency = {
    '달러': 1167, '엔': 1.096, '유로': 1268, '위안': 171
}

user_in = input("금액을 입력해주세요: ").split()
amount = user_in[0]
currency = user_in[1]
print(f'{int(user_in[0])*currency[user_in[1]]}원')