## 20181220

무중단 배포, 항상 서버가 켜져있어야 서비스가 제공이 된다. 이를 위해 heroku를 사용하기도 한다.

#### parameter란?

`https://www.google.com/search?q=뭐시기`처럼 `q` 파라미터 명이고 `뭐시기`는 파라미터 값을 의미한다. 

`request.arg.get()`을 이용하면 `뭐시기` 값을 얻어올 수 있다. 

*app.py*

```python
from flask import Flask,render_template, request
from bs4 import BeautifulSoup as bs
import time
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toon')
def toon():
    print(request.args.get('type'))
    return render_template('toon.html')
    
    
@app.route('/lotto')
def lotto():
    return render_template('lotto.html')
```

*index.html*

```html
<!DOCTYPE html>
<html>
    <head>
        <title>오늘은 배가 많이 고픈 날</title>
    </head>
    <body>
        <a href="/lotto"><button>로또</button></a>
        <a href="/toon?type=naver"><button>네이버웹툰</button></a>
        <a href="/toon?type=daum"><button>다음웹툰</button></a>
    </body>
</html>
```

*toon.html*

```html
<!DOCTYPE html>
<html>
    <head>
        <title>웹툰 모아보기</title>
    </head>
    <body>
        <h2>너님 지금 *** 웹툰 찾는거 맞음?</h2>
    </body>
</html>
```

그래서 각 버튼을 누르면 `?type=뭐시기`의 `뭐시기` 값이 터미널에 출력되는 것을 다음과 같이 확인할 수 있다.

<img src='images/image 006.png'>

<img src='images/image 007.png'>

어제 작성한 네이버 웹툰, 다음 웹툰 크롤링 코드를 갖고 와서 적용해보면

*app.py*

```python
from flask import Flask,render_template, request
from bs4 import BeautifulSoup as bs
import time
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toon')
def toon():
    cat = request.args.get('type')
    # 네이버는 html
    if(cat == 'naver'):
        today = time.strftime("%a").lower()
        url="https://comic.naver.com/webtoon/weekdayList.nhn?week="+today
        response = requests.get(url).text
        soup = bs(response, 'html.parser')
        toons = []
        li = soup.select('.img_list li') #하위를 검색할 때 띄어쓰기를 한 번 해준다.
        for item in li:
            toon={
                "title": item.select_one('dt a').text,#select는 복수개를 찾기 때문에 배열로 보여준다. 정확하게 찾기 위해 select 뒤에 [0]를 입력하거나 select_one을 사용한다.
                "url" : "https://comic.naver.com"+item.select('dt a')[0]["href"],
                "img_url":item.select('.thumb img')[0]["src"]
            }
            toons.append(toon)
    
    # 다음은 json        
    if(cat == 'daum'):
        today = time.strftime("%a").lower()
        #1. 내가 원하는 정보를 얻을 수 있는 주소를 url 변수에 담는다.
        url= 'http://webtoon.daum.net/data/pc/webtoon/list_serialized/'+today
        #2. 해당 url에 요청을 보내 응답을 받아 저장한다.
        response=requests.get(url).text
        #3. 구글신에게 파이썬으로 어떻게 json을 파싱(딕셔너리 형으로 변환)하는지 물어본다.
        #4. 파싱한다.(변환한다)
        document=json.loads(response)
        #5. 내가 원하는 데이터를 꺼내서 조합한다.
        data=document["data"]
        toons=[]
        for toon in data :
          toon={
              "title":toon["title"],
              "img_url" : toon["pcThumbnailImage"]["url"],
              "url" :'http://webtoon.daum.net/webtoon/view/'+toon["nickname"]
          }
          toons.append(toon)
        
    return render_template('toon.html', cat = cat, t=toons)
    
    
@app.route('/lotto')
def lotto():
    return render_template('lotto.html')
```

*toon.html*

```html
<!DOCTYPE html>
<html>
    <head>
        <title>웹툰 모아보기</title>
    </head>
    <body>
        <h2>너님 지금 {{cat}} 웹툰 찾는거 맞음?</h2>
        <h1>{{cat}} Webtoon 모아보기</h1>
        <table>
            <thead>
                <tr>
                    <th>썸네일</th>
                    <th>웹툰 제목</th>
                    <th>웹툰 링크</th>
                </tr>
            </thead>
            <tbody>
        <!-- app.py에서 작성한 웹툰 데이터를 바탕으로
            table의 각 줄에 웹툰 데이터가 1개씩 들어가서
            전체 웹툰들이 출력될 수 있도록 하는 코드 작성 -->
                {% for toon in t %}
                <tr>
                    <td><img src="{{ toon["img_url"] }}"></td>
                    <td>{{ toon['title'] }}</td>
                    <td><a href="{{ toon["url"] }}">웹툰 보러가기</a></td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

    </body>
</html>
```

결과 화면은 다음과 같다.

<img src='images/image 009.png'>

<img src='images/image 008.png'>



#### 아파트 매매 내역 시스템을 이용해서 내가 원하는 아파트 실거래가 검색하기

<img src='images/image 010.png'>

개발자 도구를 켜고 아파트 정보를 눌러보면 Network 탭에 getDangiInfoDetail...로 시작하는 파일을 볼 수 있다. 여기서 python 으로 요청을 하면 `{"jsonList":null}`이 뜬다.

<img src='images/image 011.png'>

여기에서 Host와 Referer가 있는데 `rt.molit.go.kr`로 접속해야 정보를 볼 수 있는데 그 외의 방법으로 접근하면 정보가 뜨지 않음을 알 수 있다. 그렇기 때문에 정상적으로 인증해서 api를 받는게 아니라면 쿠키를 찾던가 주소 위조를 통해 정보를 받아올 수 있다.

Host와 Referer를 복사해 dictionary 형 변수에 담아 requests에 url과 header를 함께 요청을 보낸다.

*app.py*

```python
.
.
@app.route('/apart')
def apart():
    #1. 내가 원하는 정보를 얻을 수 있는 url을 url변수에 저장한다.
    url = 'http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do?menuGubun=A&p_apt_code=20353906&p_house_cd=1&p_acc_year=2018&areaCode=&priceCode='
    #1-1. request headers에 추가할 정보를 dictionary 형태로 저장한다.
    headers= {
        "Host": "rt.molit.go.kr",
        "Referer": "http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND"
    }
    #2. requests의 get 기능을 이용하여 해당 url에 headers와 함께 요청을 보낸다.
    response = requests.get(url, headers=headers).text
    #3. 응답으로 온 코드의 형태를 살펴본다. (json/xml/html)
    print(response)
    return render_template('apart.html')
.
.
```

다음과 같이 정보가 정상적으로 출력이 된다.

<img src='images/image 012.png>

위치("JIBUN_NAME"),

아파트 이름("BLDG_NM"),

아파트 크기("BLDG_AREA"),

실거래가("SUM_AMT"),

실거래월,실거래일("DEAL_MM","DEAL_DD")

위 5가지를 데이터를 뽑아본다.

```python
.
.
    #3. 응답으로 온 코드의 형태를 살펴본다. (json/xml/html)
    document = json.loads(response)
    aparts=[]
    for d in document["result"]:
        d = {
            "name":d["BLDG_NM"],
            "local":d["JIBUN_NAME"],
            "scale":d["BLDG_AREA"],
            "price":d["SUM_AMT"],
            "date_MM":d["DEAL_MM"],
            "date_DD":d["DEAL_DD"]
        }
        aparts.append(d)
    
    return render_template('apart.html',d = d)
.
.
```



#### Telegram 챗봇 코드 간단 리뷰/ 기본 환경 구성

Telegram의 메세지가 Telegram server에 전달되고 그것이 내 server로 alert하여  국토부나 사람인에서 얻은 정보를 메세지로 보내는 과정을 한다. 하지만 지금 사용하는 내 server가 Cloud9인데 Telegram server로 메세지를 보내는 것이 막혀있다. 그렇기에 강사님이 제공하신 별도의 우회 방법으로 메세지를 보내기로 했다.

Telegram에 @BotFather를 통해 발급받은 키를 대놓고 소스코드에 작성하기엔 위험하므로 환경변수로 설정한다.

```
$ vi ~/.bashrc
```

터미널에 위 명령어를 치고 맨 마지막에 TELEGRAM_TOKEN 을 추가시킨다

```
export TELEGRAM_TOKEN=발급받은 키
```

이후 다음 명령어를 쳐서 터미널에 발급받은 키가 출력되면 설정완료다

```$ source ~/.bashrc
$ source ~/.bashrc
$ echo $TELEGRAM_TOKEN
```

python에서 환경변수를 가져오려면 `import os`를 추가시키고 `os.getenv('TELEGRAM_TOKEN')`으로 키 값을 불러온다.

*telegram.py*

```python
import requests
import json
import os

token=os.getenv('TELEGRAM_TOKEN')
url = 'https://api.telegram.org/bot{}/getUpdates'.format(token)

response = requests.get(url).text
print(response)
```

이대로 실행하면 다음과 같이 출력된다.

```
$ python telegram.py
{"ok":true,"result":[]}
```

Telegram에서 메세지를 보내고 다시 실행하면 다음과 같이 뜬다.

```
$ python telegram.py
{"ok":true,"result":[{"update_id":344193910,
"message":{"message_id":3,"from":{"id":664837141,"is_bot":false,"first_name":"JongMin","last_name":"Kim","language_code":"ko"},"chat":{"id":664837141,"first_name":"JongMin","last_name":"Kim","type":"private"},"date":1545281597,"text":"hi"}}]}
```

Telegram으로 메세지를 보내면 같은 내용을 답장받는 코드는 다음과 같다.

*telegram.py*

```python
import requests
import json
import os

token=os.getenv('TELEGRAM_TOKEN')
url = 'https://api.hphk.io/telegram/bot{}/getUpdates'.format(token)
#새로 업데이트가 있는지 확인

response = json.loads(requests.get(url).text)

url = 'https://api.hphk.io/telegram/bot{}/sendMessage'.format(token)
chat_id = response["result"][-1]["message"]["from"]["id"]#최신메세지를 받기위해 [-1]로 설정
msg = response["result"][-1]["message"]["text"]

requests.get(url, params = {"chat_id":chat_id, "text":msg})
```

cf. 리눅스 크론탭 : 특정시간에 특정작업을 하고 싶으면 사용한다.

--------갑자기 작동이 안되서 여기서 중지-----

내일 교육을 위해 새로 만들자

HTTP 상태 코드: 404는 없는 페이지를 탐색할 때 나오는 오류이고 5XX는 개발자의 잘못으로 서버에 문제가 있을 때 발생하는 오류이다.

*app.py*

```python
from flask import Flask, request
import requests
import json
import time
import os

app = Flask(__name__)

TELEGRAM_TOKEN=os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL='https://api.hphk.io/telegram'

@app.route('/{}'.format(os.getenv('TELEGRAM_TOKEN')), methods=['POST'])
#methods는 POST방식으로 응답을 요청한다는 의미한다.
def telegram():
    #텔레그램으로부터 요청이 들어올 경우, 해당 요청을 처리하는 코드
    print(request.get_json())
    return '', 200 #HTTP 상태코드, 정상적으로 접속한 것을 리턴함.

@app.route('/set_webhook')
#Telegram server와 연결해주며 한 번 사용하고 사용하지 않는 기능이다.
def set_webhook():
    url = TELEGRAM_URL + '/bot' + TELEGRAM_TOKEN + '/setWebhook'
    params = {
        'url':'https://ssafy-training-horangapple.c9users.io/{}'.format(TELEGRAM_TOKEN)
    }
    response = requests.get(url,params=params).text
    #params는 주소에 ?의 키 값을 여러개를 보낼 때 딕셔너리 형태로 담아 보낸다.
    return response
```

<img src='images/image 013.png'>

<img src='images/image 014.png'>



Telegram에 메세지를 입력하면 다시 보내주게 만드는 코드는 다음과 같다.

*app.py*

```python
from flask import Flask, request
import requests
import json
import time
import os

app = Flask(__name__)

TELEGRAM_TOKEN=os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL='https://api.hphk.io/telegram'

@app.route('/{}'.format(os.getenv('TELEGRAM_TOKEN')), methods=['POST'])
#methods는 POST방식으로 응답을 요청한다는 의미한다.
def telegram():
    #텔레그램으로부터 요청이 들어올 경우, 해당 요청을 처리하는 코드
    req = request.get_json()
    chat_id = req["message"]["from"]["id"]
    if(req["message"]["text"]=="안녕"):
        msg = """첫만남에는 존댓말을 하셔야죠.
'안녕하세요'라고 해보세요."""
    elif(req["message"]["text"]=="안녕하세요") :
        msg = "인사 잘한다 ㅎㅎ"
    url = 'https://api.hphk.io/telegram/bot{}/sendMessage'.format(TELEGRAM_TOKEN)
    requests.get(url, params={"chat_id": chat_id,"text":msg})
    return '', 200 #HTTP 상태코드, 정상적으로 접속한 것을 리턴함.

@app.route('/set_webhook')
def set_webhook():
    url = TELEGRAM_URL + '/bot' + TELEGRAM_TOKEN + '/setWebhook'
    params = {
        'url':'https://ssafy-training-horangapple.c9users.io/{}'.format(TELEGRAM_TOKEN)
    }
    response = requests.get(url,params=params).text
    return response
```

<img src='images/image 015.png'>



#### 환율

처음에는 https://ko.valutafx.com 를 바탕으로 크롤링 했다.

*app.py*

```python
from flask import Flask,render_template, request
from bs4 import BeautifulSoup as bs
import time
import requests
import json

app = Flask(__name__)


@app.route('/exchange')
def exchange():
    #어느 사이트든 좋다.
    #크롤링을 통해 가장 많은 환율 정보를 끌어 와라
    url="https://ko.valutafx.com/"
    response = requests.get(url).text
    soup = bs(response, 'html.parser')
    country = soup.select('.hidden option')
    count=[]
    for i in country :
        i={
            "value":i["value"]
        }
        count.append(i)
    counting=0
    countryEx=[]
    for i in count :
        url='https://ko.valutafx.com/LookupRate.aspx?to=KRW&from='+i['value']
        response = requests.get(url).text
        soup = json.loads(response) #json으로 loads 해야 값이 나온다. html로 했더니 안나온다.
        countryEx={
            "rate":soup['Rate'],
            "name":i['value']
            }
        counting=counting+1
        print(counting)
    
    
    return render_template('exchange.html',t=countryEx,k=counting)
```

막상 다 짜고 실행시켜보니 지연시간 초과로 exchange.html는 화면도 못 띄워보고 브라우저에 오류가 떴다.

사이트 요청하는 코드가 반복문 안에 있다보니까 각 나라의 환율을 찾기위해 100번 넘게 요청하기 때문에 값을 받아오는 것이 매우 느렸다. 터미널 창에 출력되는 속도를 보면 한 나라당 1초 꼴이였다. 값을 리스트로 한꺼번에 받는 소스가 있나 찾아봤지만 없어서 어쩔 수 없이 다른 사이트를 찾아보게 되었다.

https://ko.exchange-rates.org/currentRates/A/KRW 인데 여기서 'A'는 북남미, 'P'는 아시아 태평양 등 문자별로 대륙을 나타낸다. 이 점을 변경시키면서 그에 속해있는 나라들의 환율을 뽑아야했다. 그러므로 반복문을 2번 써야했고 다음과 같이 작성 했다.

*app.py*

```python
from flask import Flask,render_template, request
from bs4 import BeautifulSoup as bs
import time
import requests
import json

app = Flask(__name__)
  
@app.route('/exchange')
def exchange():
    #어느 사이트든 좋다.
    #크롤링을 통해 가장 많은 환율 정보를 끌어 와라
    area = ['A','P','E','M','F'] #대륙별 문자
    counting=0
    countries=[]
    for i in area : #대륙
        url='https://ko.exchange-rates.org/currentRates/{}/KRW'.format(i)
        response = requests.get(url).text # str 타입
        soup = bs(response, 'html.parser') 
        #코드는 html로 되어있었다, bs4.BeautifulSoup 타입, 사이트의 html 코드 전체
        ratelists = soup.select('.text-rate strong')
        # class text-rate의 strong 태그에 존재, list 타입, [<strong>값</strong>,..]
        namelists = soup.select('.full a') 
        # class full의 a 태그에 존재, list 타입, [<a href=#>값</a>,..]
        for j in range(len(ratelists)) : #나라
            country={
               "name_unit":namelists[j].text, #<a href=#>값</a>의 '값'만 
               "rate":ratelists[j].text #<strong>값</strong>의 '값'만
            }
            countries.append(country)
            counting=counting+1
    
    return render_template('exchange.html',t=countries,k=counting)
```

*exchange.html*

```html
<!DOCTYPE html>
<html>
    <head>
        <title>환율</title>
    </head>
    <body>
       <table>
            <thead>
                <tr>
                    <th>국가명</th>
                    <th>환율(/1원)</th>
                </tr>
            </thead>
            <tbody>
                {% for country in t %}
                <tr>
                    <td>{{ country['name_unit'].split()[0] }}</td>
                    <td>{{ country["rate"] }} {{country['name_unit'].split()[1]}}</td>
                </tr>
                {% endfor %}
                <td>총 {{ k }} 개</td>
            </tbody>
        </table>
    </body>
</html>
```

html에서도 python의 split함수가 사용이 되는 것이 신기했다. 이걸 사용한 이유는 `country['name_unit']`의 값 자체가 '대한민국 원'처럼 '나라이름 단위'로 되어있어서 쪼개서 써야했다.

결과화면은 다음과 같다.

<img src ='images/image 016.JPEG'>
