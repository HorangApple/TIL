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
        soup = json.loads(response)
        countryEx={
            "rate":soup['Rate'],
            "name":i['value']
            }
        counting=counting+1
        print(counting)
    
    
    return render_template('exchange.html',t=countryEx,k=counting)