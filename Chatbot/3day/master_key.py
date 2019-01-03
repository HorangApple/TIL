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

for cafe in master_key_list():
    print('{} : {}'.format(cafe["title"],cafe['num']))

print(master_key_info(21))