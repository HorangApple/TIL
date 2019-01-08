"""
문제1
아래 코드의 출력 결과를 예상해보세요.
"""
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")

# 답 : 3
#      5
"""
문제2
투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 
해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 
아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하세요.

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
"""
#여기에 코드를 작성하세요.
name = input("투자 종목을 입력하시오 : ")
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

if name in warn_investment_list :
    print('투자 경고 종목입니다.')
else :
    print('투자 경고 종목이 아닙니다.')

"""
문제3
다음 코드의 결과값을 예측해보세요.
"""
a = "Life is too short, you need python"

if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print('need')
else:
    print('none')

#답 : shirt

"""
문제4
다음 리스트에서 10 이상인 수를 전부 더해서 출력하세요.

exNumber = [43, 2, 6, 34, 12, 32, 7, 9, 81, 51]
"""
exNumber = [43, 2, 6, 34, 12, 32, 7, 9, 81, 51]
print(sum([x for x in exNumber if x >=10]))

"""
문제5
A 기업의 입사 시험은 필기 시험 점수가 80점 이상이면서 
코딩 시험을 통과해야 합격이라고 정했습니다. (코딩 시험 통과 여부는 True, False로 구분) 
사용자로부터 필기시험 점수를 입력받아 '합격' 혹은 '불합격' 여부를 판단하는 코드를 작성하세요.
"""
score = int(input("필기점수를 입력하시오 : "))
codingResult = bool(input("코딩 시험 통과 여부 : "))
if score >= 80 and codingResult :
    print("합격")
else :
    print("불합격")