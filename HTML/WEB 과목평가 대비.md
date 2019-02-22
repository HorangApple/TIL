# WEB 과목평가 

HTML과 CSS, Bootstrap은 슬라이드를 최우선순위로 학습
객관식 20문제, 주관식 5문제로 구성되어 있습니다.

## 1. HTML
###  시맨틱 태그

<img src="images/image 002.jpg">

웹을 의미상으로 구분해놓게 해주는 태그를 의미한다.

Web Developer에서 Document outline을 사용하면 구조적으로 얼마나 잘 짰는지 확인할 수 있다. 

SEO : 검색엔진최적화

구글에는 크롤러라는 봇을 이용해 페이지를 수집하는데 잘 짜여진 시멘틱 태그이면 구글에서 검색 될 때 이쁘게 보일 수 있게 된다. 그렇기 때문에 구조적으로 잘 짜는 것이 중요하다. 

###  기초 태그
#### -  금요일 프로젝트
#### -  homework/workshop
#### -  Django, Flask 수업에서 주로 활용하였던 부분





## 2. CSS 
###  상대 단위

em

- 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이즈로 설정하는 크기 단위

rem

- em은 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데 이를 예방하기 위해 HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위

###  선택자 및 우선 순위 (월말평가에도 나옵니다 미리 공부하세요.)

```css
/*후손셀렉터*/
/*문서 구조에서 특정 요소의 자손(자식,손자, 이후에 후손까지)을 선택하는 선택자로 div에서 p를 선택하여 그 이하까지 속성을 적용한다.*/
div p{
    color: crimson;
}
/*자식셀렉터*/
/*특정 요소의 직계 자식만(손자, 후손은 제외) 선택하는 선택자로 오직 p에만 적용되며 그 아래까진 적용되지 않는다.*/

div > p{
    color: crimson;
}
```



###  박스모델

Box model

항상 네모로 생각해야한다. 둥근 모양도 사실 네모를 깎아서 표현했다고 해도 무방하다.

<img src="images/image%20003.png">

margin은 박스 밖의 여백을 지칭한다. 여러 박스와 margin이 겹치게 될텐데 이는 합산하지 않고 margin 값이 큰 것을 기준으로 겹쳐진다.

margin 어트리뷰트는 4개 값을 입력하면 top을 시작으로 시계방향으로 설정되고 2개 값을 입력하면 세로, 가로를 기준으로 적용이되고 값이 하나만 입력되면 4방향으로 같은 값이 적용된다.

```css
margin : 16px 16px 16px 16px /*(top을 시작으로 시계방향으로 설정)*/
margin : 16px 16px /*(세로축, 가로축)*/
margin : 16px /*(한번에 네 군데)*/
```

border는 box의 경계선을 가리킨다. 어트리뷰트의 필수 값은 `dotted`와 같은 style이다. default로 1px로 잡혀있기에 style만큼은 꼭 정해줘야한다. border는 다음과 같이 한 줄로 정의할 수도 있다.

```css
border:2px dotted pink;
```

```css
border-width: 1px 2px 2px 1px;
border-color:pink;
border-style: dashed;
```

padding은 box 내부의 여백을 가리킨다.

###  Display

none은 화면상에 아예 나타나지 않게 한다. `visibility: hidden`같은 경우 태그는 존재해서 드래그하면 공간이 있지만 컨텐츠가 보이지 않으나 `display: none`은 아예 보이지 않는다.

###  Position
###  기초 CSS 문법 (금요일 프로젝트 및 homework/workshop)
#### -  금요일 프로젝트
#### -  homework/workshop



## 3. bootstrap
### utility (슬라이드 중심으로 눈에 익혀두기)

####  - [텍스트](https://getbootstrap.com/docs/4.0/utilities/text/)
####  - [색상](https://getbootstrap.com/docs/4.0/utilities/colors/)
####  - [스페이싱](https://getbootstrap.com/docs/4.0/utilities/spacing/#horizontal-centering)



###  그리드 시스템 (월말평가에도 나옵니다 미리 공부하세요.)

https://www.vikingcodeschool.com/web-design-basics/designing-with-grid-systems

bootstrap의 꽃은 Container이다. Container라는 박스를 활용하여 깔끔하게 배치를 도와준다.

모던 그리드 시스템은 총 격자가 12개를 사용한다. 왜냐하면 약수가 많기 때문에 깔끔하게 떨어뜨리는게 용이하다.

margin은 공간을 밀면서 확장하기 때문에 적당하지 않으면 줄이 넘어버린다.

<img src = "images/image 006.png">

그렇다고 해서 padding으로 줄어도 소용 없는 것이 border 내의 background가 색이 들어가 있기에 실질적으로 줄어들지 않은 것처럼 보인다.

컨텐츠를 보여줄 화면의 크기는 pc화면 기준 1200px을 사용한다. 왜냐하면 모니터 보급률을 따르면 1280px 대가 많이 보급이 되었기 때문이다.

Small(sm) : 540px / Medium(md) : 720px / Large(lg) : 992px / Extra large(xl) : 1200px

좌우 전체를 다 채우고 싶다면 'container-fluid'로 바꿔서 사용한다.

컨텐츠가 너무 많으면 반응형을 안쓰는 것이 낫다.

https://flexboxfroggy.com/#ko

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!--bootstrap file-->
    
	<!--bootstrap end-->
    <title>Document</title>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-sm-3">
                25%
            </div>
            <div class="col-sm-6">
                50%
            </div>
            <div class="col-sm-3">
                25%
            </div>
        </div>
    </div>
</body>
</html>
```



### 컴포넌트 - 이름만 어떤 것 있다 정도

navbar, modal, card, alert, button, form



## 4. Django (월말평가에도 나옵니다 미리 공부하세요.)
> Model, ORM, CRUD는 시험범위가 아닙니다. 수업시간에 자주 활용했던 문법 중심으로

Django 기초 명령어 ex) 프로젝트 생성 등

```bash
$ mkdir TEST
$ cd TEST
$ pyenv virtualenv 3.6.7 text-venv
$ pyenv local test-venv
$ pip install django
$ django-admin startproject test .
$ python manage.py startapp pages
$ python manage.py runserver $IP:$PORT
```



기초적인 DTL 문법 (truncatewords와 같은 필터 메소드 제외)

```html
{% load static %} 
: base template에서 static 폴더에 있는 외부파일(css 등)을 부를 때 사용
{% extends 'articles/base.html' %}
: base template을 불러옴
{% block body %}~{% endblock %}
: base template 내에서는 block 지정, 그 외의 곳에서는 block 작성
{% for i in 변수명 %}~{% endfor %}
: for문과 동일
{{ 변수명 }}
```



settings.py

```python
#...
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["django-horangapple.c9users.io"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages.apps.PagesConfig'
]

#...
LANGUAGE_CODE = 'ko-kr'  # default : 'en-us'

TIME_ZONE = 'Asia/Seoul' # default : 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#...
```



Form, variable routing 등

urls.py

```python
## bonbon/urls.py
from django.contrib import admin,include
from django.urls import path
from pastlife import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('pastlife/',views.pastlife),
    path('articles/',include('articles.urls')) # url 전달
]

## articles/urls.py
from django.urls import path
from . import views
app_name='articles' # url별명에 대한 namespace 생성
urlpatterns = [
    path('',views.index,name='index'),
    path('new/',views.new,name='new'),
    path('create/',views.create,name='create'),
    path('<int:id>/',views.detail,name='detail'),
    path('<int:id>/edit/',views.edit,name='edit'),
    path('<int:id>/delete/',views.delete,name='delete'),
    path('<int:id>/update/',views.update,name='update'),
]
# 1. /articles -> 모든 글을 보여주는 곳
# 2. /articles/1 -> 글 상세하게 보는 곳
# 3. /articles/new -> 새 글을 작성
# 4. /articles/create -> 새 글을 저장
# 5. /articles/1/edit -> 글을 편집
# 6. /articles/1/update -> 글을 수정
# 7. /articles/1/delete -> 글을 삭제
```



views.py

```python
from django.shortcuts import render,redirect
from .models import Articles,Comment
# Create your views here.
# 1. /articles -> 모든 글을 보여주는 곳
# 2. /articles/1 -> 글 상세하게 보는 곳
# 3. /articles/new -> 새 글을 작성
# 4. /articles/create -> 새 글을 저장
# 5. /articles/1/edit -> 글을 편집
# 6. /articles/1/update -> 글을 수정
# 7. /articles/1/delete -> 글을 삭제

def index(request):
    data=Articles.objects.all()
    print(data)
    return render(request,'articles/index.html',{'data':data})
    
def new(request):
    return render(request,'articles/new.html')
    
def create(request):
    title=request.GET.get('title')
    content=request.GET.get('content')
    data=Articles(title=title,content=content)
    data.save()
    return redirect('articles:detail',data.id)

def detail(request,id):
    article=Articles.objects.filter(id=id).first()
    return render(request,'articles/detail.html',{'article':article})
    
def update(request,id):
    title=request.GET.get('title')
    content=request.GET.get('content')
    data=Articles.objects.filter(id=id).first()
    data.title=title
    data.content=content
    data.save()
    return redirect('articles:index',data.id)

def edit(request,id):
    data=Articles.objects.filter(id=id).first()
    return render(request,'articles/edit.html',{'id':data.id,'title':data.title,'content':data.content})
    
def delete(request,id):
    data=Articles.objects.filter(id=id).first()
    data.delete()
    return redirect('articles:index')
    
def comment(request,id):
    content=request.POST.get('content')
    comment=Comment(content=content,article_id=id)
    comment.save()
    return redirect('articles:detail',id)
```

### form의 POST 전달

html 태그의 `form`의 `action`에 `method="POST"` 를 설정하면 다음과 같은 오류가 뜬다.

<img src="C:/Users/JongMin/Documents/Github/TIL/Django/images/image%20010.png"/>

CSRF(Cross-site Request Forgery)는 사용자가 요청하는 정보를 가로챌 수 있는 취약점 중 하나이다. 사용자와 서버 간에 token을 주고 받는데 이는 서버에서 사용자를 구분짓기위해 존재한다. 그러나 사용자와 서버 중간에 프록시를 이용하여 끼여들어 사용자의 토큰을 가져올 수 있다.

예를 들어 form이 GET 방식으로 되어있다면 url로 파라미터를 보내야하는데 이 주소패턴을 이용하여 제 3자가 마음대로 만들 수 있다. 이를 POST로 막을 수 있다.

오류를 없애기위해선 `{% csrf_token %}`를 `form` 태그 안에 넣고 `view.py`에서 값을 받을 때는 `request.GET.get()`대신 `request.POST.get()`로 받아와야한다.

```html
...
<h3>댓글</h3>
<form action="/articles/{{ article.id }}/comment/" method="POST">
  {% csrf_token %}
  <input type="text" name="content"/>
  <input type="submit" value="Submit"/>
</form>
...
```



<img src="C:/Users/JongMin/Documents/Github/TIL/Django/images/image%20011.png">

그러나 위처럼 주석처리 된 value가 토큰이기 때문에 응답 받은 코드에서 빼내서 토큰을 위변조할 수 있다.

