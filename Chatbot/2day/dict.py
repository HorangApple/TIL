"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")
average = (sum(iu_score.values()))/len(iu_score)
print(average)
print("------------")
# 수업 답안
total_score = 0
count = 0
for score in iu_score :
    total_score = total_score + iu_score[score]
    count = count + 1
print(total_score/count)
print("------------")
scores = list(iu_score.values())
print(sum(scores)/len(scores))
    


# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")
print("iu : {}".format(sum(score["iu"].values())/len(score["iu"])))
print("ui : {}".format(sum(score["ui"].values())/len(score["ui"])))
print("------------")

for cl in score :
    tmp = list(score[cl].values())
    print("{}: {}".format(cl,(sum(tmp)/len(tmp))))


# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")
for city in cities :
    print("{} : {:0.2f}".format(city, sum(cities[city])/len(cities[city])))

print("------------")

for city in cities :
    temp=cities[city]
    print("{}의 평균기온: {}".format(city, round(sum(temp)/len(temp), 1)))
# round() 반올림해주는 함수이며 뒤에 숫자를 붙이면 그 수만큼 소숫점 자릿수를 표현한다.

# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")
mini = {
    "서울": min(cities["서울"]),
    "대전": min(cities["대전"]),
    "광주": min(cities["광주"]),
    "부산": min(cities["부산"])
    }
maxi = {
    "서울": max(cities["서울"]),
    "대전": max(cities["대전"]),
    "광주": max(cities["광주"]),
    "부산": max(cities["부산"])
}
print(min(mini)+"이(가) 가장 춥습니다.")
print(max(maxi)+"이(가) 가장 덥습니다.")
print("------------")
# 1. 최저기온, 최고기온을 저장할 수 있는 변수를 선언한다.
minimum = ["도시명",1000]
maximum = ["도시명",-1000]

# 2. 각 도시를 순회하는 반복문을 만든다.
for city in cities :
# 3. 각 도시의 기온 정보를 순회하는 반복문을 만든다.
    for temp in cities[city] :
# 4. 순회하다가 최저기온의 경우에는 현재 저장된 값보다 작은 값이, 
#    최고 기온의 경우에는 현재 저장된 값보다 큰 값이 있는 경우
#    현재 저장되어 있는 값을 바꾼다.
#       최고기온에 해당하는 조건문
        if(maximum[1]<temp):
            maximum[0] = city
            maximum[1] = temp
#       최저기온에 해당하는 조건문
        if(minimum[1]>temp):
            minimum[0] = city
            minimum[1] = temp
            
print("최고기온은 {}의 {}도이며 최저기온은 {}의 {}도 입니다.".format(maximum[0],maximum[1],minimum[0],minimum[1]))

# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")
k=0
for i in cities["서울"]:
    if i==2 :
        print("네")
        k=k+1
if(k==0) :
    print("아뇨")
print("------------")
# 1. cities 변수에서 서울부분만 추출해서 seoul 변수에 저장한다.
seoul = cities["서울"]
# 1-1. flag 라고 하는 변수에 false를 저장한다.
flag = False
# 2. seoul 변수(list)를 순회하며 요소가 2와 같았던 적이 있는지 확인한다.
for i in seoul :
    if i==2 :
# 3. 2도와 같았던 적이 있다면 flag 변수를 true로 바꿔준다.
        flag = True
# 4. flag 변수에 따라 출력문을 작성한다.
if flag==True :
    print("네")
else :
    print("아니요")