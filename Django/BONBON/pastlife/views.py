from django.shortcuts import render
from faker import Faker
from .models import Job # 동일 패키지이니까 .만 찍으면 된다.
import requests

# Create your views here.
def index(request):
    return render(request, 'pastlife/index.html')
    
def pastlife(request):
    # 1. index에서 넘어온 이름을 받고
    name=request.GET.get('name')
    
    # 만약 해당 이름이 DB에 저장되어 있다면, DB에 저장된 값을 가져온다.
    # 없다면, DB에 추가하고 faker를 통해 fake job을 만들어 DB에 추가하고 해당 값을 job에 저장한다.

    # person=Job.objects.get(name=name) # 없으면 오류 발생
    person=Job.objects.filter(name=name).first() # 없으면 None 반환
    if person:
        job = person.job
    else:
        # 2. faker를 통해 가짜 전생을 생성하여
        fake=Faker('ko_KR')
        job=fake.job()
        new_person=Job(name=name,job=job)
        new_person.save()
    # 3. pl.html에 돌려준다.
    naver_headers = {
            'X-Naver-Client-Id': 'qDz_4_UEwpvxjZ2yz4GM',
            'X-Naver-Client-Secret': 'tDQbI3UVje'
        }
    urlNaver=f"https://openapi.naver.com/v1/search/image?query={job}"
    result=requests.get(urlNaver,headers=naver_headers).json()
    image=result.get('items')[0].get('link')
    
    url=f"http://api.giphy.com/v1/gifs/search?api_key=jrMUSckz300WuQiGP3Fi1JowWH5XV0ft&q={job}&limit=1&lang=ko"
    result=requests.get(url).json()
    gif=result.get('data')[0].get('images').get('original').get('url')
    contents={'name':name,'job':job,'gif':gif,'image':image}
    return render(request,'pastlife/pl.html',contents)