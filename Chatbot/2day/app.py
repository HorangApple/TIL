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


    
@app.route('/exchange')
def exchange():
    #어느 사이트든 좋다.
    #크롤링을 통해 가장 많은 환율 정보를 끌어 와라
    area = ['A','P','E','M','F']
    counting=0
    countries=[]
    for i in area :
        url='https://ko.exchange-rates.org/currentRates/{}/KRW'.format(i)
        response = requests.get(url).text
        soup = bs(response, 'html.parser')
        ratelists = soup.select('.text-rate strong')
        namelists = soup.select('.full a')
        print(namelists)
        for j in range(len(ratelists)) :
            country={
               "name_unit":namelists[j].text,
               "rate":ratelists[j].text
            }
            #print(type(country))
            #print(type(country['name_unit']))
            countries.append(country)
            counting=counting+1
    
    return render_template('exchange.html',t=countries,k=counting)
    
@app.route('/lotto')
def lotto():
    return render_template('lotto.html')