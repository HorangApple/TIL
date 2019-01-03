# 20181221

#### 코드리뷰

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
#key를 숨기기 위해 환경변수 활용, methods는 POST방식으로 응답을 요청한다는 의미한다.
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
    # 아예 받는다라는 개념이 아니고 요청을 보내서 받는다로 requests.get를 이해해야한다.
    return '', 200 #HTTP 상태코드, 정상적으로 접속한 것을 리턴함. set_webhook으로 인한 Alert에 대한 답변

@app.route('/set_webhook') #사실 methods=['GET']으로 default가 되어있다.
def set_webhook(): 
    # Telegram server에서 메세지를 받으면 그때그때마다 등록한 URL로 Alert 해달라고 요청하는 역할
    url = TELEGRAM_URL + '/bot' + TELEGRAM_TOKEN + '/setWebhook' # Telegram의 Bot api
    params = {
        'url':'https://ssafy-training-horangapple.c9users.io/{}'.format(TELEGRAM_TOKEN)
    }
    response = requests.get(url,params=params).text
    return response

```

Postman이라는 것을 이용하면 쉽게 서버에 요청할 수 있는데 이를 이용해서 악용하면 위변조를 할 수 있다. 그렇기 때문에 절대 알아서 안되는 값들은 환경변수를 이용해서 코드를 작성해야한다.

리스트를 하나의 문자열로 만들어주는 것은 `'구분문자'.join(1)`을 이용한다.

https://i.kakao.com/ 카카오톡으로 챗봇을 만들어보자



#### 방탈출 정보를 봇으로 보내보자

마스터키와 서울이스케이프를 바탕으로 만들어본다. 먼저 ''마스터키''를 입력하면 지점 리스트를 출력하는 것을 해보자.



<img src='images/image 001.png'>



*master_key.py*

```python
from bs4 import BeautifulSoup as bs
import requests

def master_key_info(cd):
    url= "http://www.master-key.co.kr/booking/booking_list_new"
    params = {
        'date':'2018-12-21',
        'store' : cd,
        'room' : ''
    }
    response = requests.post(url, params).text #get방식은 주소에 ?로 값이 표현이 되는데 post는 requests의 form data에 담아서 값이 전달된다.
    document = bs(response, 'html.parser')
    ul = document.select('.reserve .escape_view')
    theme_list=[]
    for li in ul:
        title = li.select('p')[0].text
        info = ''
        for col in li.select('.col') :
            info = info + '{} - {}\n'.format(col.select_one('.time').text, col.select_one('.state').text)
        theme = {
            'title' : title,
            'info' : info
        }
        theme_list.append(theme)
    
    return theme_list

def master_key_list():
    url = "http://www.master-key.co.kr/home/office"
    response = requests.get(url).text
    document = bs(response, 'html.parser')
    lis=document.select('.escape_view')
    cafe_list=[]
    for li in lis :
        cafe={
    #       title = li.select_one('p').text    
    #       if(title.endswith('NEW')):
    #            title = title[:-3] 으로 뒤의 NEW를 뺄 수 있다.
    #        
    #        address = li.selct('dd')[0].text
    #        tel = li.selct('dd')[1].text
    #        link = 'http://www.master-key.co.kr'+li.select_one('a')["href"]
            'title': li.select('.escape_text p')[0].text.replace("NEW",""),#select_one이나 select뒤에 [0]을 붙여주면 된다.
            'address':li.select('dd')[0].text, 
            #li.select('dd')를 출력해보면 [<dd><span> ##### </span> </dd>, <dd><span>#####</span></dd>]로 나온다
            'tel':li.select('dd')[1].text,
            'link': 'http://www.master-key.co.kr'+li.select_one('a')['href'],
            'num': li.select_one('a')['href'].replace("/booking/bk_detail?bid=","")
        }
        cafe_list.append(cafe)
    return cafe_list

# 사용자로부터 '마스터키 ***점이라는 메세지를 받으면
# 해당지점에 대한 오늘의 정보를 요청하고 크롤링
# 메시지 (예약정보)를 보내준다.
# 잘 출력하는지 아래처럼 테스트 한다.
for cafe in master_key_list():
    print('{} : {}'.format(cafe["title"],cafe['num']))

print(master_key_info(21))
```

이제 이 코드를 Telegram에서 메세지를 받고 작동할 수 있도록 어제 만들었던 `app.py`를 수정해 완성시키면 다음과 같다.

```python
from flask import Flask, request
from bs4 import BeautifulSoup as bs
import requests
import time
import os

app = Flask(__name__)

TELEGRAM_TOKEN=os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL='https://api.hphk.io/telegram'

def master_key_info(cd):
    url= "http://www.master-key.co.kr/booking/booking_list_new"
    params = {
        'date': time.strftime('%Y-%m-%d'), # 오늘 날짜 입력
        'store' : cd,
        'room' : ''
    }
    response = requests.post(url, params).text 
    # get방식은 주소에 ?로 값이 표현이 되는데 post는 requests의 form data에 담아서 값이 전달된다.
    document = bs(response, 'html.parser')
    ul = document.select('.reserve .escape_view')
    theme_list=[]
    for li in ul:
        title = li.select('p')[0].text
        info = ''
        for col in li.select('.col') :
            info = info + '{} - {}\n'.format(col.select_one('.time').text, col.select_one('.state').text)
        theme = {
            'title' : title,
            'info' : info
        }
        theme_list.append(theme)
    
    return theme_list

def master_key_list():
    url = "http://www.master-key.co.kr/home/office"
    response = requests.get(url).text
    document = bs(response, 'html.parser')
    lis=document.select('.escape_view')
    cafe_list=[]
    for li in lis :
        cafe={
            'title': li.select('.escape_text p')[0].text.replace("NEW",""),#select_one이나 select뒤에 [0]을 붙여주면 된다.
            'address':li.select('dd')[0].text, 
            #li.select('dd')를 출력해보면 [<dd><span> ##### </span> </dd>, <dd><span>#####</span></dd>]로 나온다
            'tel':li.select('dd')[1].text,
            'link': 'http://www.master-key.co.kr'+li.select_one('a')['href'],
            'num': li.select_one('a')['href'].replace("/booking/bk_detail?bid=","")
        }
        cafe_list.append(cafe)
    return cafe_list

cafe_list={} # '지점명 : 번호'의 집합인 dictionary
for cafe in master_key_list():
    cafe_list.update({cafe["title"] : int(cafe['num'])})
cafe_list.update({"전체" : -1})

@app.route('/{}'.format(os.getenv('TELEGRAM_TOKEN')), methods=['POST'])
#methods는 POST방식으로 응답을 요청한다는 의미한다.
def telegram():
    #텔레그램으로부터 요청이 들어올 경우, 해당 요청을 처리하는 코드
    req = request.get_json()
    chat_id = req["message"]["from"]["id"]
    text = req["message"]["text"]
    # 마스터키 전체
    # 마스터키 ***점
    if(text.startswith('마스터키')) :
        cafe_name = text.split(' ')[1]
        cd = cafe_list[cafe_name]
        if(cd>0):
            data = master_key_info(cd)
        else :
            data = master_key_list()
            for d in data:
                del d['num'] # 지점 번호를 출력하지 않기 위해 삭제한다.
        msg = []
        for d in data :
            msg.append('\n'.join(d.values()))
        msg = '\n'.join(msg)

    else :
        msg='등록되지 않은 지점입니다.'
        
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

'마스터키 전체'를 입력하면 모든 지점에 대한 정보가 출력된다.

<img src = "images/image 003.png">

'마스터키 ~점'을 입력하면 해당 지점의 예약 상태가 출력된다.

<img src = "images/image 004.png">



cf. 한꺼번에 주석했다, 취소하는 것은 `Ctrl+/` 를 누르면 된다. 서비스를 할 때 어떤 형식으로 만들지 고민을 한다.

이번에 서울 이스케이프를 작업해보면 다음과 같다.

*seoul.py*

```python
import requests
import json
import time

def get_total_info() :
    url = "http://www.seoul-escape.com/reservation/change_date/"
    params = {
        'current_date':'2018/12/21'
    }
    
    response = requests.get(url, params=params).text
    document = json.loads(response)
    cafe_code = {
        '홍대1호점':1,
        '홍대2호점':10,
        '강남1호점':3,
        '강남2호점':11,
        '인천 부평점':4,
        '부산 서면점':5
    }
    total = {}
    game_room_list = document["gameRoomList"] # 기본 틀 잡기
    for cafe in cafe_code :
        total[cafe] = []
        for room in game_room_list:
            if(cafe_code[cafe] == room["branch_id"]) :
                total[cafe].append({"title":room["room_name"], "info" :[]})
    
    print(total)
    book_list = document["bookList"] # 앞에서 만든 틀에 데이터 집어넣기
    for cafe in total :
        print(cafe)
        for book in book_list:
            if(cafe==book["branch"]):
                for theme in total[cafe]:
                    if(theme["title"]==book["room"]) :
                        if(book["booked"]):
                            booked = "예약완료"
                        else:
                            booked = "예약가능"
                        theme["info"].append("{} - {}".format(book["hour"],booked))
    return total
    
def seoul_escape_list() :
    total = get_total_info()
    return total.keys()

def seoul_escape_info(cd) :
    total = get_total_info()
    cafe = total[cd]
    tmp = []
    for theme in cafe :
        tmp.append("{}\n {}".format(theme["title"], '\n'.join(theme["info"])))
    return tmp
```



다음은 Telegram에서도 작동 할 수 있도록 코드를 옮겨 붙여 수정해보자

*app.py*

```python
from flask import Flask, request
from bs4 import BeautifulSoup as bs
import requests
import time
import os
import json

app = Flask(__name__)

TELEGRAM_TOKEN=os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL='https://api.hphk.io/telegram'

def master_key_info(cd):
    url= "http://www.master-key.co.kr/booking/booking_list_new"
    params = {
        'date': time.strftime('%Y-%m-%d'), # 오늘 날짜 입력
        'store' : cd,
        'room' : ''
    }
    response = requests.post(url, params).text 
    # get방식은 주소에 ?로 값이 표현이 되는데 post는 requests의 form data에 담아서 값이 전달된다.
    document = bs(response, 'html.parser')
    ul = document.select('.reserve .escape_view')
    theme_list=[]
    for li in ul:
        title = li.select('p')[0].text
        info = ''
        for col in li.select('.col') :
            info = info + '{} - {}\n'.format(col.select_one('.time').text, col.select_one('.state').text)
        theme = {
            'title' : title,
            'info' : info
        }
        theme_list.append(theme)
    
    return theme_list

def master_key_list():
    url = "http://www.master-key.co.kr/home/office"
    response = requests.get(url).text
    document = bs(response, 'html.parser')
    lis=document.select('.escape_view')
    cafe_list=[]
    for li in lis :
        cafe={
            'title': li.select('.escape_text p')[0].text.replace("NEW",""),#select_one이나 select뒤에 [0]을 붙여주면 된다.
            'address':li.select('dd')[0].text, 
            #li.select('dd')를 출력해보면 [<dd><span> ##### </span> </dd>, <dd><span>#####</span></dd>]로 나온다
            'tel':li.select('dd')[1].text,
            'link': 'http://www.master-key.co.kr'+li.select_one('a')['href'],
            'num': li.select_one('a')['href'].replace("/booking/bk_detail?bid=","")
        }
        cafe_list.append(cafe)
    return cafe_list

cafe_list={} # '지점명 : 번호'의 집합인 dictionary
for cafe in master_key_list():
    cafe_list.update({cafe["title"] : int(cafe['num'])})
cafe_list.update({"전체" : -1})

############################

def get_total_info() :
    url = "http://www.seoul-escape.com/reservation/change_date/"
    params = {
        'current_date':time.strftime('%Y/%m/%d')
    }
    
    response = requests.get(url, params=params).text
    document = json.loads(response)    
    cafe_code = {
        '홍대1호점':1,
        '홍대2호점':10,
        '강남1호점':3,
        '강남2호점':11,
        '인천 부평점':4,
        '부산 서면점':5
    }
    total = {}
    game_room_list = document["gameRoomList"] # 기본 틀 잡기
    for cafe in cafe_code :
        total[cafe] = []
        for room in game_room_list:
            if(cafe_code[cafe] == room["branch_id"]) :
                total[cafe].append({"title":room["room_name"], "info" :[]})
    
    
    book_list = document["bookList"] # 앞에서 만든 틀에 데이터 집어넣기
    for cafe in total :
        for book in book_list:
            if(cafe==book["branch"]):
                for theme in total[cafe]:
                    if(theme["title"]==book["room"]) :
                        if(book["booked"]):
                            booked = "예약완료"
                        else:
                            booked = "예약가능"
                        theme["info"].append("{} - {}".format(book["hour"],booked))
    return total
    
def seoul_escape_list() :
    total = get_total_info()
    return total.keys()

def seoul_escape_info(cd) :
    total = get_total_info()
    cafe = total[cd]
    tmp = []
    for theme in cafe :
        tmp.append("{}\n {}".format(theme["title"], '\n'.join(theme["info"])))
    return tmp

############################

@app.route('/{}'.format(os.getenv('TELEGRAM_TOKEN')), methods=['POST'])
#methods는 POST방식으로 응답을 요청한다는 의미한다.
def telegram():
    #텔레그램으로부터 요청이 들어올 경우, 해당 요청을 처리하는 코드
    req = request.get_json()
    chat_id = req["message"]["from"]["id"]
    text = req["message"]["text"]
    # 마스터키 전체
    # 마스터키 ***점
    if(text.startswith('마스터키')) :
        cafe_name = text.split(' ')[1]
        cd = cafe_list[cafe_name]
        if(cd>0):
            data = master_key_info(cd)
        else :
            data = master_key_list()
            for d in data:
                del d['num']
        msg = []
        for d in data :
            msg.append('\n'.join(d.values()))
        msg = '\n'.join(msg)
        
    elif(text.startswith('서이룸')):
        cafe_name = text.split(' ')
        if(len(cafe_name)>2): # '서이룸 부산 서면점' 처럼 3개인 것
            #python how to join from 2 to 4
            cafe_name = ' '.join(cafe_name[1:3]) 
            #'부산'과 '서면점'을 붙여서 '부산 서면점'으로 만들어줌
            data = seoul_escape_info(cafe_name)            
        else:
            cafe_name = cafe_name[-1]
            if(cafe_name == "전체"):
                data = seoul_escape_list()
            else:
                data = seoul_escape_info(cafe_name)
        msg = '\n'.join(data)                
    else :
        msg='등록되지 않은 지점입니다.'
        
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



