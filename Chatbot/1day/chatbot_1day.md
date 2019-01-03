# 점심메뉴

```python
import random

menu = ["순남시레기","멀티캠퍼스 20층", "양자강", "마라탕", "강남목장","시골집"]
menu_detail={"순남시레기":"시레기국, 보쌈", "멀티캠퍼스 20층" : "오늘의 메뉴",
             "양자강": "차돌짬뽕","강남목장":"뚝배기 불고기","시골집":"쌈밥정식"}

#하와와와 () brackets
#하와와 {} curly bracket
#하와 [] squre brackets
#하 <> angle brackets

lunch = random.choice(menu)
print(lunch+"에서는 "+ menu_detail[lunch]+"이(가) 먹을만 합니다.")
```



# 미세먼지

```python
import requests
from bs4 import BeautifulSoup

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EC%84%9C%EC%9A%B8&ServiceKey={}&ver=1.3&pageNo=3'.format(key)
response = requests.get(url).text
soup = BeautifulSoup(response, 'xml') #xml으로 받았으니 xml으로 설정
print(soup('item')) #item으로 검색
gn = soup('item')[7]
location = gn.stationName.text
time = gn.dataTime.text
dust = int(gn.pm10Value.text)


print('{0} 기준: 서울시 {1}의 미세먼지 농도는 {2} 입니다.'.format(time, location, dust))
if(dust>100):
  dustText="매우 나쁨"
elif(dust>80):
  dustText="나쁨"
elif(dust>60) :
  dustText="보통"
else :
  dustText="좋음"
print("오늘의 미세먼지 농도는 {0}입니다.".format(dustText))
```



# 먹보

```python
dish=["삼겹살","꽃등심","파스타","뚝배기 불고기","폭찹"]

# 1. for문을 이용해서 dish에 담겨있는 모든 음식을 먹는 코드를 작성

for i in dish :
  print("{0}을 먹었다! 힘이 솟아난다!".format(i))
i=0
print()
# 2. while문을 이용해서 dish에 담겨있는 모든 음식을 두번씩 먹는 코드 작성
while i<2 :
  for j in dish :
      print("{0}을 먹었다! 힘이 솟아난다!".format(j))
  i=i+1
```



# 날씨

```python
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID="+key
print(url)

data = requests.get(url).json()
# requests => 기능 뭉탱이
# .get =>requests가 가진 기능 중 하나를 사용해서 또 하나의 기능 뭉탱이를 뱉어낸다.
# .json => 위에서 나온 기능 뭉탱이의 기능 중 하나를 사용해서 또 하나의 기능 뭉탱이를 뱉어낸다.
print(data["weather"][0]['description'])
# 메소드 체이닝
weather = data['weather'][0]['description']
temp = float(data['main']['temp'])-273.15
temp_min = float(data['main']['temp_min'])-273.15
temp_max = float(data['main']['temp_max'])-273.15
wind_speed = data['wind']['speed']
wind_deg = data['wind']['deg']
print("""서울의 바람은 {} m/s이며, 방향은 {}도 입니다.""".format(wind_speed, wind_deg))


print("""서울의 오늘 날씨는 [{}] 이며, 섭씨 {:.1f}도 입니다.
최저/최고 온도는 {:.1f}/{:.1f}도 입니다.
""".format(weather, temp, temp_min, temp_max)
)
```



# Lotto

``` python
import requests
import random
from bs4 import BeautifulSoup as bs

url = 'https://m.dhlottery.co.kr/common.do?method=main'
response = requests.get(url).text
soup = bs(response, 'html.parser') #html 검색은 html.parser를 이용한다.
document = soup.select('.prizeresult')[0] # id 검색은 앞에 #을 붙이고 class 검색은 앞에 .을 붙인다.
numbers = document.select('span') #id도 class도 아니기에 그냥 입력해서 검색
ns = []
for number in numbers:
  ns.append(int(number.text)) #number.text가 문자열이기 때문에 int로 형변환

lotto=[]
lotto = random.sample(list(range(1,46)), 6)

print("지난주 로또는 {}입니다.".format(sorted(ns)))
print("이번주 로또는 {}입니다.".format(sorted(lotto)))

count = 0

for i in lotto : #python check array has value
  if i in ns :
      count=count+1
      
print("일치 갯수는 {}입니다.".format(count))
```



# 네이버 웹툰

1. 네이버 웹툰을 가져올 수 있는 주소를 파악하고 url 변수에 저장한다.
2. 해당 주소로 요청을 보내 정보를 가져온다
3. 받은 정보를 bs를 이용해 검색하기 좋게 만든다.
4. 네이버 웹툰 페이지로 가서 제목, 웹툰 리스트, 썸네일 주소가 어디에 있는지 파악한다.
5. 3번에서 저장한 문서를 이용해 4번에서 파악한 정보의 위치를 뽑아내는 코드를 작성한다.
6. 출력한다.

```python
import requests
import time
from bs4 import BeautifulSoup as bs
 
today = time.strftime("%a").lower() #오늘 날짜 세 글자
#1. 네이버 웹툰을 가져올 수 있는 주소를 파악하고 url 변수에 저장한다.
url="https://comic.naver.com/webtoon/weekdayList.nhn?week="+today
#2. 해당 주소로 요청을 보내 정보를 가져온다
response = requests.get(url).text
#3. 받은 정보를 bs를 이용해 검색하기 좋게 만든다.
soup = bs(response, 'html.parser')
#4. 네이버 웹툰 페이지로 가서, 오늘자 리스트페이지가 어디에 있는지 파악한다.
toons = []
li = soup.select('.img_list li') #하위를 검색할 때 띄어쓰기를 한 번 해준다.
for item in li:
  toon={
    "title": item.select_one('dt a').text,#select는 복수개를 찾기 때문에 배열로 보여준다. 정확하게 찾기 위해 select 뒤에 [0]를 입력하거나 select_one을 사용한다.
    "url" : item.select('dt a')[0]["href"],
    "img_url":item.select('.thumb img')[0]["src"]
  }
#5. 3번에서 저장한 문서를 이용해 4번에서 파악한 정보의 위치를 뽑아내는 코드를 작성한다.
  toons.append(toon)
#6. 출력한다.
print(toons)

```



# 다음 웹툰

1. 내가 원하는 정보를 얻을 수 있는 주소를 url 변수에 담는다.
2. 해당 url에 요청을 보내 응답을 받아 저장한다.
3. 구글신에게 파이썬으로 어떻게 json을 파싱(딕셔너리 형으로 변환)하는지 물어본다.
4. 파싱한다.(변환한다)
5. 내가 원하는 데이터를 꺼내서 조합한다.

```python
import requests
import time
import json
from bs4 import BeautifulSoup as bs

today = time.strftime("%a").lower()
#1. 내가 원하는 정보를 얻을 수 있는 주소를 url 변수에 담는다.
url= 'http://webtoon.daum.net/data/pc/webtoon/list_serialized/'+today #개발자모드의 네트워크 탭에서 찾아 주소값을 입력한다.
#2. 해당 url에 요청을 보내 응답을 받아 저장한다.
response=requests.get(url).text
#3. 구글신에게 파이썬으로 어떻게 json을 파싱(딕셔너리 형으로 변환)하는지 물어본다.
#4. 파싱한다.(변환한다)
document=json.loads(response)
#5. 내가 원하는 데이터를 꺼내서 조합한다.
data=document["data"]
toons=[]
for toon in data :
  print(toon["title"])
  print(toon["pcThumbnailImage"]["url"])
  print('http://webtoon.daum.net/webtoon/view/'+toon["nickname"])
  
print(data)
```



