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

def get_total_info() :
    url = "http://www.seoul-escape.com/reservation/change_date/"
    params = {
        'current_date':time.strftime('%Y/%m/%d')
    }
    
    response = requests.get(url, params=params).text
    document = json.loads(response)
    # area = ['홍대1호점','홍대2호점','강남1호점','강남2호점','인천 부평점','부산 서면점']
    
    # lists=[]
    
    # for i in area :
    #     for j in range(len(document['bookList'])):
    #         if(document['bookList'][j]['branch']==i) :
    #             li={
    #                 'area' : i,
    #                 'time' : document['bookList'][j]['hour'],
    #                 'room' : document['bookList'][j]['room'],
    #                 'reservation' : document['bookList'][j]['booked'] #예약완료이면 true
    #             }
    #             lists.append(li)
            
    # print(lists[0]['area'])
    
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
        if(len(cafe_name)>2):
            #python how to join from 2 to 4
            cafe_name = ' '.join(cafe_name[1:3])
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
