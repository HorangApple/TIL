from flask import Flask, render_template
from bs4 import BeautifulSoup as bs 
import requests
import time

app = Flask(__name__)

@app.route('/index')
def index():
    print("hi")
    print("nice to meet you")
    return """
    <h1>보노보노는 귀엽다!</h1>
    <img src="http://i1.daumcdn.net/cfile297/image/212EAC375901C0F3161A55" />
    <h3>Hello World</h3>
    """
@app.route('/naverToon')#카멜케이스
def naver_toon():#스네이크케이스
    today = time.strftime("%a").lower()
    url="https://comic.naver.com/webtoon/weekdayList.nhn?week="+today
    response = requests.get(url).text
    soup = bs(response, 'html.parser')
    toons = []
    li = soup.select('.img_list li') #하위를 검색할 때 띄어쓰기를 한 번 해준다.
    for item in li:
        toon={
            "title": item.select_one('dt a').text,#select는 복수개를 찾기 때문에 배열로 보여준다. 정확하게 찾기 위해 select 뒤에 [0]를 입력하거나 select_one을 사용한다.
            "url" : item.select('dt a')[0]["href"],
            "img_url":item.select('.thumb img')[0]["src"]
        }
        toons.append(toon)
    return render_template('naverToon.html', t=toons)
    
@app.route('/daum_toon')
def daum_toon():
    return render_template('naverToon.html')