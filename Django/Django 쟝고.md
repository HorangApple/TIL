[TOC]

# 1. 시작하기

static web을 사용하다가 부족함에 dynamic web을 사용하게 되었다. flask는 경량형 프레임워크이기때문에 한계가 있기 때문에 Django를 사용한다.

프레임워크를 활용하여 웹서비스를 만드는 것은 마치 프렌차이즈를 이용해서 카페를 차리는 것과 같다. 기본적인 구조나 필요한 코드들은 프레임워크가 제공하니 좋은 웹 서비스를 만드는 것에 집중하면 된다.

Django의 기본 구조는 데이터를 관리하는 `Model`, 사용자가 보는 화면인 `Template`, 중간 관리자인 `View`를 의미한다. 특히 `View`는 MVC 구조에서 Controller에 가까운 역할을 한다.

urls를 받아 해당하는 `View`가 받는다. 들어오는 모든 요청은 `View`가 관리하며 요청에 대한 수행을 `Model`에게 넘어가 수행한다. `Model`에게 받은 정보를 `View`가 받아 `Templates`으로 넘겨 사용자가 원하는 정보를 담고 있는 html 파일을 보여준다.

<img src="images/image 001.png"/>


## 1.1 프로젝트 생성 및 환경 설정

윈도우 환경에서 하기위해서는 PyCharm을 통해 Django 프로젝트를 생성한다.


리눅스 환경에서 작업을 하면 다음과 같은 과정에 따라 프로젝트를 생성한다.

1. 프로젝트 진행할 폴더 생성 [TEST]
2. 해당 폴더로 이동 (cd TEST)
3. 가상 환경 설정
   - pyenv virtualenv 3.6.7 [가상환경 이름]
   - pyenv local [가상환경 이름]
4. `django` 설치
   - `pip install django`

5. Django 프로젝트 test 생성
    - `django-admin stargproject text .`

cf. 3.6.7같이 버전을 나타내는 것을 'semver'라고 한다.


```bash
$ mkdir TEST
$ cd TEST
$ pyenv virtualenv 3.6.7 text-venv
$ pyenv local test-venv
$ pip install django
$ django-admin startproject test .
```

커멘드 창에 위와 같이 입력하면 된다.



## 1.2 pyenv - python 버전 관리 툴

먼저 pyenv를 설치한다. 현업에서는 다양한 python 버전을 고려해야하기 때문에 이를 위한 python 버전관리 툴인 pyenv를 설치해야한다. 현업에서는 항상 python이 최신 버전을 사용하는 것이 아니라 다양한 버전이 사용되기 때문에 f-string의 사용가능 여부 등의 버전마다의 특징을 알고 있어야 한다.

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
$ exec "$SHELL"

$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
$ exec "$SHELL"

$ pyenv install 3.6.7
```

3.6.7 버전을 설치하고나서 이 버전을 사용하고 싶다면 `pyenv global 3.6.7`를 입력하여 버전을 변경할 수있다.

해당하는 디렉터리에서 아래의 명령어로 python 가상환경을 만들고 진입한다. 여기서는 `intro`라는 폴더에서 진행했다. `pyenv local intro-venv`를 입력했기 때문에 해당 디렉터리에 진입하면 자동으로 가상환경으로 들어가게 된다.

```bash
$ pyenv virtualenv 3.6.7 intro-venv
$ pyenv local intro-venv
```



## 1.3 Django 설치 및 설정

3.6.7 버전이기 때문에 pip를 이용하여 django를 설치한다. 참고로 가상환경에서 작동하기 때문에 여러 폴더마다 가상환경을 진입해서 작업하게 된다면 Django도 처음부터 다시 깔아야 한다.

```bash
$ pip install django
```

현재 위치에서 `intro`라는 이름으로 startproject를 만든다.

```bash
$ django-admin startproject intro .
```

<img src="images/image 002.png"/>

이제 `intro`라는 프로젝트 폴더와 python 파일들이 생성된 것을 확인할 수 있다.


설정을 위해 `setting.py`를 열어본다

*intro/settings.py*

```python
#...
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["django-horangapple.c9users.io"]

#...
LANGUAGE_CODE = 'ko-kr'  # default : 'en-us'

TIME_ZONE = 'Asia/Seoul' # default : 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#...
```

위와 같이 c9의 `프로젝트 이름-계정.c9users.io`를 `ALLOWED_HOSTS`의 [] 안에 입력한다. 그리고 `LANGUAGE_CODE = 'en-us'`를 `ko-kr`로, `TIME_ZONE = 'UTC'`를 `Asia/Seoul`로 바꿔준다.

자주 건들게 되는 파일은 `urls.py`과 `settings.py`이다. `manage.py`는 script로 관리하는 파일이다.



## 1.4 app 생성

프로젝트 생성이 끝났다면 이제 app을 만들어보자.

```bash
$ python manage.py startapp pages
```

`pages`라는 app을 만들어보면 폴더 한 개가 생성된다.

<img src="images/image 003.png"/>

`apps.py`는 잘 안쓰이지만 view를 직접 다루는 `views.py`를 많이 다루게 된다.



*intro/settings.py*

```python
#...
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages.apps.PagesConfig', # 그냥 'pages'라고 입력해도 된다.
]
#...
```

app을 설치하게 되면 `settings.py`로 가서 `pages.apps.PagesConfig`를 입력한다. `pages.apps.PagesConfig`은 `pages/apps.py`에 있는 class `PagesConfig`을 지칭하는 것이며 pages app에 대한 정보를 제공한다.

','는 trailing comma라고 한다.



*pages/views.py*

```python
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
# @app.route('/')
# def index():
#     return render_template('index.html')
# =>templates/index.html

    
def lotto(request):
    lucky=random.sample(range(1,46),6)
    return render(request, 'lotto.html',{'lucky':lucky})
    
# @app.route('/')
# def lotto():
#     import random
#     lucky = random.sample(range(1,46),6)
#     return render_template('index.html')
    
def hello(request,name):
    return render(request, 'hello.html',{'name':name})
    
# @app.route('/hello/<name>')
# def hello(name):
#     return render_template('hello.html', name=name)
```

flask에서 작성한 `app.py`와 유사하며 `render`는 `render_template`과 유사하다. 마찬가지로 `templates/index.html`와 `templates/lotto.html`를 생성한다.



*templates/index.html*

```html
{% extends 'base.html' %}

{% block body %}
<h1>쟝고 첫번째 앱</h1>
{% endblock %}
```

<img src="images/image 005.png"/>

*templates/lotto.html*

```html
{% extends 'base.html' %}

{% block body %}
<h1>{{ lucky }}</h1>
{% endblock %}
```

<img src="images/image 004.png"/>

*templates/hello.html*

```html
{% extends 'base.html' %}

{% block body %}
<h1>안녕! {{ name }}</h1>
{% endblock %}
```



<img src="images/image 005.png"/>



*templates/base.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>First Django</title>
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```



*intro/urls.py*

```python
#...
from django.contrib import admin
from django.urls import path
from pages import views # package로 불러오기

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('lotto/', views.lotto)
    path('hello/<str:name>/', views.hello)
    # path(요청 받을 url/, 넘겨줄 view)
]
```

요청 받을 url을 작성할 때 항상 '/'로 끝나야한다.

```bash
$ python manage.py runserver $IP:$PORT
```

위 명령어를 통해 서버를 구동 시킬 수 있다. 코드를 수정하는 대로 자동으로 반영이 되는데 DB를 만지거나 settings을 변경했을 때는 서버를 껐다가 다시 켜야한다.



정리하면 새로운 app을 만들 때는 다음과 같은 과정을 거친다.

```
$ python manage.py startapp 앱 이름 -> settings.py의 INSTALLED_APPS에 등록
```

app 내의 기능을 추가할 때는 다음과 같은 과정을 거친다.

```
views.py에서 html파일로 리턴하는 함수 정의 -> urls.py의 urlpatterns에 path 등록 -> templates 폴더에 해당 html파일 생성 및 작성
```

html에 python 변수를 사용하거나 특별한 기능을 사용하게 만드는 template language가 있다. [공식문서](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/)

그런데 보통 views에서 작업을 한 다음에 template에 넘기는 것이 일반적이다.

cf. 랜덤 이쁜 이미지 : https://picsum.photos/


# 2. urls
## 2.1 urls 분리

`intro/urls.py`의 `path`가 많아지면 관리하기가 힘드니 새로운 문지기를 추가해보자.

*intro/urls.py*

```python
from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('pages.urls'))
]
```

*pages/urls.py*

```python
from django.urls import path, include
from pages import views

urlpatterns = [
    path('index/', views.index),
    path('lotto/', views.lotto),
    path('hello/<str:name>/', views.hello),
    path('dinner/', views.dinner),
    path('reverse/<str:word>/',views.reverse),
    path('sqrt/<int:num>/',views.sqrt)
    # path(요청 받을 url/, 넘겨줄 view)
]
```

이렇게 되면 만약 index 페이지로 가고 싶다면 주소가 `/index`가 아닌  `/home/index`로 접속해야 한다. 물론 `'home/'`부분을 `''`로 만들면 원래 주소대로 사용해도 된다.

## 2.2 urls 별명 짓기

기존에 `'<int:id>/'`처럼 사용한 것을 별도의 별명을 지어 작성한다. 이를 위에서는 아래의 예시와 같이 작성해야한다.

*urls.py*

```python
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
```

`app_name`을 선언하여 url별명에 대한 namespace를 생성한다. 이후 `path`마다 요소로 `name` 값을 넣어 별명을 지정한다.


# 3. templates

## 3.1 templates 폴더

해당 app 폴더 안에 'templates' 폴더를 만들어서 사용한다. `templates`폴더에 있는 html파일들을 한 단계 이상의 하위 폴더 안에 넣어야 한다. 그래야 다른 app의 html과 이름이 겹쳐서 오류가 발생하는 것을 막을 수 있다.

만약 공통으로 사용할 template을 프로젝트 최상위 루트에 templates 폴더를 만들어서 사용하고 싶다면 settings.py에 다음과 같이 경로를 설정해야 한다.

*settings.py*

```python
TEMPLATES = [
    {
        #...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
		#...
    },
]
```

## .2 html 작성

*index.html*

```html
{% extends 'articles/base.html' %}

{% block body %}
<div class="jumbotron text-center">
  <h1 class="display-4">게시판</h1>
  <hr class="my-4">
  <a class="btn btn-primary btn-lg float-right" href="{% url 'articles:new' %}" role="button">글쓰기</a>
</div>
<div class="list-group">
{% for i in data %}
<div>
    <a href="{% url 'articles:detail' i.id %}"class="list-group-item list-group-item-action">{{i.id}}  {{i.title}}</a>
</div>

{% endfor %}
</div>
{% endblock %}
```

위와 같이 html에서 사용할 때는 `"{% url 'articles:new' %}"`처럼 불러올 수 있다. 만약 id값과 같이 전달받아야하는 값이 있다면 `"{% url 'articles:detail' i.id %}"`처럼 뒤에 한 칸 띄우고 값을 이어서 적으면 된다.

`views.py`의 `render`안에 사용할 때는 html 파일을 불러오기위해서 일반적인 파일 경로로 작성해야한다. 반면 `redirect`를 사용할 때는 웹 주소를 넣는 것이므로 이 때는 `'articles:detail'`형식으로 작성하면 된다.

## 3.3 django template 문법

https://docs.djangoproject.com/en/2.1/ref/templates/builtins/

flask에서 사용했던 jinja template과는 비슷하면서도 다르기 때문에 공식문서를 보며 해결한다.

예시로 시간을 다뤄보자.

`models.py`에서 `DateField`로 저장된 값은 html에서 django template로 불러올 때 default로 `mmm. dd, yyyy`형식으로 되어 html의 input의 value에 값을 넣어도 반영이 되지 않는다. 이럴 때는 django template만의 formatting을 이용하여 바꿔야 한다.

```html
<input type="date" class="form-control" max="2019-12-31" name="birthday" value="{{ student.birthday|date:"Y-m-d"  }}"/>
```

# 4. Model & DB
## 4.1 Model 생성

Model을 다뤄보기위해 새로운 프로젝트로 시작한다. `ORM`으로 프로젝트를 생성하였고 `orm`으로 app을 생성하였다.

*articles/models.py*

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    # id는 따로 선언하지 않으면 알아서 primary key로 생성
    title = models.TextField()
    content = models.TextField()
    # shell에서 표시되는 내용 정의, migrate를 한 이후에도 수정해도 됨
    def __repr__(self):
        return f"{self.title}: {self.content}"
    def __str__(self):
        return f"<{self.title}: {self.content}>"
```


```bash
$ python manage.py makemigrations
Migrations for 'articles':
  articles/migrations/0001_initial.py
    - Create model Article
```

`migrations`폴더에 `0001_initial.py`가 생성되었고 이것을 열어보면 없던 `id`가 생성되어있다.  Django에 DB설계도를 보내는 역할을 수행한다.

`python manage.py sqlmigrate articles 0001`를 입력하면 SQL문으로 어떻게 선언했는지 출력해준다.



```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying articles.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
```

`python manage.py migrate`를 통해 프로젝트 폴더 `ORM`에 `db.sqlite3`를 생성하여 DB를 만든다.



```bash
$ python manage.py shell
Python 3.6.7 (default, Feb 11 2019, 05:36:17) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from articles.models import Article
>>> article = Article(title="Happy",content="Hacking")
>>> article.save()
>>> Articles =Article.objects.all()
>>> Articles[0]
<Article: Article object (1)>
>>> a=Articles[0]
>>> a.title
'Happy'
>>> a.content
'Hacking'
```

`python manage.py shell`로  Django shell을 열고 `model.py`의 `Article` 클래스를 사용할 수 있도록 import 한다. 이후 `article`라는 인스턴스 객체를 만들면서 `title="Happy",content="Hacking"`을 초기화 시킨다.

반면  `python manage.py dbshell`로 SQLite shell을 열수 있어 직접 sql을 입력할 수 있다.

`article.save()`를 하면 이 내용으로 db에 저장이 된다. 내용을 보고 싶다면 `변수=Article.objects.all()`이후의 과정으로 들여다 보면 된다.



```bash
----------등록----------
>>> a = Article(title="하하핫 두번째 글이다.",content="냉무")
# Article.object.create(title="하하핫 두번째 글이다.",content="냉무")와도 같음
>>> a.save()
----------검색----------
>>> a = Article.objects.filter(title="Happy").first() # get과 다르게 filter는 없으면 None 반환
>>> a.title
'Happy'
>>> a.content
'Hacking'
>>> a2 = Article.objects.get(pk=1) # 없으면 오류 발생
>>> a2.title
'Happy'
>>> a2.content
'Hacking'
# 모든 데이터를 검색할 때는 Article.objects.all(), 
# 요소 하나씩 검색할 때는 Article.objects.all()[i].title
----------삭제----------
>>> a2.delete()
(1, {'articles.Article': 1})
>>> len(Article.objects.all())
1

>>> a = Article.objects.get(title="하하핫 두번째 글이다.")
>>> a.title
'하하핫 두번째 글이다.'
>>> a.content
'냉무'
>>> a.delete()
(1, {'articles.Article': 1})
>>> len(Article.objects.all())
0

>>> article = Article(title="이제 곧 수업 끝남", content="좀만 더 화이팅")
>>> article.save()
>>> article = Article(title="hey",content="it's done")
>>> article.save()
>>> articles=Article.objects.all()
>>> articles[0]
이제 곧 수업 끝남: 좀만 더 화이팅
# __repr__를 선언하지 않으면 <Article: Article object (3)>로 출력
>>> articles[0].id
3
>>> articles[0].content
'좀만 더 화이팅'
>>> articles[1].content
"it's done"
----------수정----------
>>> article = Article.objects.get(title="hey")
>>> article.title = "hi"
>>> article.save()
>>> article.title
'hi'
```

위와 같이 CRUD를 할 수 있다.



## 4.2 Model 등록 및 추가 설정

*articles/admin.py*

```python
from django.contrib import admin
from .models import Article
# Register your models here.

admin.site.register(Article)
```

만들었던 model을 `admin.py`를 통해 등록을 한다.



```bash
$ python manage.py createsuperuser
Username (leave blank to use 'ubuntu'): admin
Email address: 
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

<img src="images/image 009.png">

<img src="images/image 008.png">

이제 서버를 켜서 `/admin`으로 접속하면 `python manage.py createsuperuser`으로 등록했던 `Username`과 `Password`를 입력하는 form이 뜬다. 입력하고 접속하면 model, 즉 DB를 관리할 수 있는 페이지가 나온다.



*articles/admin.py*

```python
from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','content')

admin.site.register(Article,ArticleAdmin)
```

<img src="images/image 007.png">

`ArticleAdmin` 클래스를 새로 만들어 `Article`의 column 이름들을 튜플 형식으로 list_display에 입력하면 위와 같이 리스트 형식으로 바뀌게 된다.



*base.html*

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```

직접 만든 css를 추가하고 싶다면 `href`에 `static/css/style.css`로 추가한 상태로 진행해야한다. flask같은 경우 `static/css/style.css`를 추가하면 된다.

migration&migrate는 폴더 위치에 상관없이 `manage.py`로 선언하면 자동으로 DB가 생성된다.



## 4.3 데이터베이스의 관계(테이블 간의 관계)

1:1를 예시로 개인-주민등록증, 남편-부인을 들 수 있고 1:N (has many, belongs to)는 게시글-댓글, 학급-학생 등을 예시로 들 수 있다. M:N은 수강신청(학생-수업)을 예시로 들 수 있다. 물론 아예 관계가 없는 경우도 있다.

보다 편리하게 CLI을 이용하기 위해 django의 extension의 ipython을 설치한다.

```bash
$ pip install django_extensions ipython
```

이후 `settings.py`에 가서 `INSTALLED_APPS`에 `'django_extensions'`를 추가시킨다. 그러면 `python manage.py shell`를 사용할 때 jupyter notebook 같은 인터페이스로 변경된다.

`python manage.py shell_plus`를 입력하면 내가 갖고 있는 모든 환경이 import 되어 shell이 구동된다.

### 1:N 관계

구현하려는 게시글과 댓글은 1:N 관계를 갖고 있기 때문에 테이블로 구현을 한다면  N의 테이블에 1에 대한 정보(primary key)를 담고 있어야한다. 즉, foreign key를 갖고 있어야 한다.

*models.py*

```python
from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.TextField()
    content=models.TextField()
    def __repr__(self):
        return f"{self.title}: {self.content}"
    def __str__(self):
        return f"<{self.title}: {self.content}>"
        
class Comment(models.Model):
    content=models.TextField()
    # CASCADE는 글이 삭제되면 같이 삭제 되는 필수 옵션
    article=models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
```

임의의 데이터를 넣고 shell_plus에서 다뤄보자

```bash
In [4]: Articles.objects.all()  
Out[4]: <QuerySet [<18번글, 제목: 아아하항>, <19번글, 시불쟝/: 흐흫ㅎ극흑...>]>

In [5]: article1=Articles.objects.get(pk=18)                                                  

In [6]: comment=Comment(content="첫번째 댓글",article=article1)                               

In [7]: comment      
Out[7]: <첫번째 댓글>

In [8]: comment.save()                                                                        

In [9]: Comment.objects.first()      
Out[9]: <첫번째 댓글>

In [10]: Comment.objects.first().content       
Out[10]: '첫번째 댓글'

In [11]: Comment.objects.first().article       
Out[11]: <18번글, 제목: 아아하항>

In [12]: Comment.objects.first().article.content                   
Out[12]: '아아하항'

In [13]: Articles.objects.first().comment_set.all()                                    
Out[13]: <QuerySet [<첫번째 댓글>]>

In [16]: comment=Comment(content="두번째 글의 첫번째 댓글",article_id=19)                     

In [17]: comment.save()                                                                       

In [18]: Comment.objects.all()[1]                                                       
Out[18]: <두번째 글의 첫번째 댓글>

In [19]: Comment.objects.all()[1].article                                               
Out[19]: <19번글, 시불쟝/: 흐흫ㅎ극흑...>

In [20]: Comment.objects.all()[1].article_id                                           
Out[20]: 19
```

id 값을 넣는 방법은 두 가지가 있다. 하나는 객체를 찾아와 넣어서 django가 알아서 id를 입력해주는 것과 `ForeignKey의 이름_id`를 입력해주는 방법이 있다. 전자는 django가 자동으로 만들어준 것이다.

만약 `models.py`의 ForeignKey의 옵션으로 `related_name`를 추가시켰다면 `ForeignKey의 이름_id` 아닌 `related_name`로 정의된 이름으로 사용해도 된다.

```bash
In [2]: Articles.objects.first().comments                                               
Out[2]: <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager at 0x7f8e5414b6d8>

In [3]: Articles.objects.first().comments.all()
    # Articles.objects.first().comment_set.all()과 동일
Out[3]: <QuerySet [<첫번째 댓글>]>
```

`article=Articles.objects.first()`이고 DTL에서 사용할 때는 괄호를 뗀 `article.comments.all`으로 사용해야한다.

`Articles`입장에서 검색을 할 때 django가 자동으로 `Articles`에도 `Comment`의 정보를 입력해주지 않았다면 다음과 같이 일일이 입력해야한다.

```python
Articles.objects.get(pk=Comment.objects.first().article_id)
```

반면 `Comment`입장에서는 이렇게 입력할 수 있다.

```python
Comment.objects.filter(article_id=Articles.objects.first().id)   
```

### N:M DB
1:N과 다르게 두 테이블을 N:M 관계를 나타내기 위한 별도의 테이블을 만들어야 한다. 다음과 같이 두 테이블을 ForeignKey로 받은 테이블을 만든다.

*models.py*

```python
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
      return self.name
    
class Lecture(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
      return self.name
  
class Enrollment(models.Model):
    # 저장되는 것은 객체가 저장됨
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture,on_delete=models.CASCADE)
    
    def __str__(self):
      return "{}가 {}을(를) 수강 중입니다.".format(self.student.name,self.lecture.name)
```

예시를 위해 shell_plus로 아래처럼 데이터를 넣었다.

```bash
>>> jm = Student.objects.get(name="김종민")                                               
>>> jm
<Student: 김종민>
>>> algo = Lecture.objects.get(name="알고리즘")
>>> Enrollment.objects.create(student_id=1, lecture_id=1)
<Enrollment: 김종민가 알고리즘을(를) 수강 중입니다.>
>>> Enrollment.objects.create(student_id=1, lecture_id=2)
<Enrollment: 김종민가 자료구조을(를) 수강 중입니다.
>>> Enrollment.objects.all()
<QuerySet [<Enrollment: 김종민가 알고리즘을(를) 수강 중입니다.>, <Enrollment: 김종민가 자료구 조을(를) 수강 중입니다.>]>

# 수강한 과목 전체 조회
>>> jm.enrollment_set.all()
<QuerySet [<Enrollment: 김종민가 알고리즘을(를) 수강 중입니다.>, <Enrollment: 김종민가 자료구 조을(를) 수강 중입니다.>]>
```
위와 같이 직접 별도의 테이블을 만들어도 되지만 Django를 이용하면 따로 테이블을 만들 필요가 없다.

*model.py*

```python
#...
from faker import Faker

fake = Faker('ko_kr')

class Client(models.Model):
    name = models.CharField(max_length=746)
    
    @classmethod
    def dummy(cls, n):
        for i in range(n):
          # Clinent.objects.create()와 동일
          # faker 패키지 설치 후 작성
          cls.objects.create(name=fake.name())
    
    def __str__(self):
        return self.name
    
class Resort(models.Model):
    name = models.CharField(max_length=746)
    # Client를 가리킴, ManyToManyField는 어디에다 만들어도 상관이 없다.
    clients = models.ManyToManyField(Client, related_name = "resorts")
    
    def __str__(self):
        return self.name
```

models.ManyToManyField을 사용하고 migrate하면 알아서 table을 3개 만들어준다. models.ManyToManyField은 어느 테이블에 넣었는지 상관 없다.

다음은 더미 데이터를 넣고 다뤄본다.

```bash
>>> Client.dummy(23)
>>> Client.objects.all()
<QuerySet [<Client: 이민수>, <Client: 김예준>, <Client: 이영미>, <Client: 차도윤>, <Client: 안지훈>, <Client: 김지영>, <Client: 김현주>, <Client: 전정희>, <Client: 박준호>, <Client: 이민석>, <Client: 이보람>, <Client: 우승현>, <Client: 김경희>, <Client: 서민서>, <Client: 강정희>, <Client: 강은영>, <Client: 문순옥>, <Client: 김윤서>, <Client: 장성진>, <Client: 김은정>, '...(remaining elements truncated)...']>
>>> Resort.objects.create(name="보라보라 보라카이")
<Resort: 보라보라 보라카이>
>>> Resort.objects.create(name="현대 블룸비스타")
<Resort: 현대 블룸비스타>
>>> Resort.objects.create(name="한화 콘도 양평")
<Resort: 한화 콘도 양평>
>>> bora = Resort.objects.first()
>>> bora
<Resort: 보라보라 보라카이>

>>> bora.clients
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7fc28cc99fd0>

>>> bora.clients.all()
<QuerySet []>

# 더미데이터 추가
>>> for client in Client.objects.all():
...     bora.clients.add(client)
... 
>>> bora.clients.all()
<QuerySet [<Client: 이민수>, <Client: 김예준>, <Client: 이영미>, <Client: 차도윤>, <Client: 안지훈>, <Client: 김지영>, <Client: 김현주>, <Client: 전정희>, <Client: 박준호>, <Client: 이민석>, <Client: 이보람>, <Client: 우승현>, <Client: 김경희>, <Client: 서민서>, <Client: 강정희>, <Client: 강은영>, <Client: 문순옥>, <Client: 김윤서>, <Client: 장성진>, <Client: 김은정>, '...(remaining elements truncated)...']>

# related_name 추가 전
>>> one = Client.objects.last()
>>> one.resort_set.all()
<QuerySet [<Resort: 보라보라 보라카이>]>

# related_name 추가 후
>>> one.resorts.all()
<QuerySet [<Resort: 보라보라 보라카이>]>
>>> one.resorts.add(Resort.objects.last())
>>> one.resorts.all()
<QuerySet [<Resort: 보라보라 보라카이>, <Resort: 한화 콘도 양평>]>
```

어느 테이블 상관없이 1:N을 다루었을 때처럼 `.'테이블의 소문자이름_set'`을 통해 다른 테이블에 접근할 수 있다.

DB에 column을 새로 추가시키려면 default 문제로 `db.sqlite3`와 `XXXX_initial.py`를 삭제하고 다시 만드는 것이 쉽다. 테이블을 추가로 만들어서 삭제하지 않게 할 수 있으나 성능이 떨어진다.

# 4. form
## 4.1 form의 POST 전달

html 태그의 `form`의 `action`에 `method="POST"` 를 설정하면 다음과 같은 오류가 뜬다.

<img src="images/image 010.png"/>

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

<img src="images/image 011.png">

그러나 위처럼 주석처리 된 value가 토큰이기 때문에 응답 받은 코드에서 빼내서 토큰을 위변조할 수 있다.

## 4.2 Django의 forms 사용
별도의 `form.py`를 만들어 Django의 forms을 활용해본다.

```python
from django import forms
from .models import Post,Comment

class PostModelForm(forms.ModelForm):
    # field 설정
    content = forms.CharField(
        label="content",
        widget=forms.Textarea(attrs={
        'rows' : 5,
        'cols' : 50,
        'placeholder' : '지금 뭘 하고 계신가요?',
    }))
    
    class Meta:
        # 정보를 저장할 model 설정
        model = Post
        # '__all__'은 모델이 갖고있는 모든 것을 가져옴
        # input을 만들 칼럼 값을 list로 만들어 넣어줌.
        fields = ['content','image']
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
```
이렇게 만든 form class를 템플릿에 다음과 같이 적용한다.

*views.py*
```python
#...
def create(request):
    # 만약, POST 요청이 오면
    if request.method == 'POST':
        # 글을 작성하기.
        form = PostModelForm(request.POST,request.FILES)
        if form.is_valid():
            # 검증 후 user 정보를 얻는다.
            post = form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('posts:list')
        
    # GET 요청이 오면
    else:
        # post를 작성하는 폼을 가져와 template에서 보여줌.
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request,'post/create.html', context)
```

*create.html*
```html
{% extends 'base.html' %}

{% load bootstrap4 %}

{% block body %}
<h1>새로운 Post 작성하기</h1>
<!--파일을 넘길 땐 enctype 값을 넣어야한다.-->
<form method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {% bootstrap_form form %}
  {% buttons %}
    <button type="submit" class="btn btn-primary">업로드</button>
  {% endbuttons %}
</form>
{% endblock %}
```

## 4.3 로그인 관련 폼
Django에서 따로 라이브러리로 제공하기 때문에 별도로 form.py를 만들 필요가 없다.

```python
# 회원가입 폼과 로그인 폼
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
  # 폼을 보낼 때
  form = UserCreationForm()
  form = AuthenticationForm()
  # 요청을 받아올 때
  form = UserCreationForm(request.POST)
  form = AuthenticationForm(request, request.POST)

# login 실행
from django.contrib.auth import login as auth_login
  # 로그인 할 때
  auth_login(request,form.get_user())

# logout 실행
from django.contrib.auth import logout as auth_logout
  # 로그아웃 할 때
  auth_logout(request)

# 사용자 model
from django.contrib.auth import get_user_model
  # 해당 정보에 대한 객체를 가져올 때
  profile = get_object_or_404(get_user_model(),username=username)
```

## 4.4 파일 업로드

*settings.py*
```python
# ...
# 접미사
MEDIA_URL = '/media/'

# 실제 경로
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
```

*(app이 아닌 최상위 루트의) urls.py*
```python
# ...
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

템플릿에서는 form 태그의 속성에 `enctype="multipart/form-data"`을 추가시킨다. 파일은 설정한 'media'폴더에 저장이 되며 이렇게 저장된 이미지를 템플릿에서 활용하려면 `"{{ post.image.url }}"`처럼 `.url`를 붙여 사용한다.

# crud 연습

https://github.com/joke2k/faker

Faker 패키지는 임의의 데이터를 만들어서 입력해준다.

*pastlife/views.py*

```python
from django.shortcuts import render
from faker import Faker
from .models import Job # 동일 패키지이니까 .만 찍으면 된다.
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
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
            'X-Naver-Client-Id': '키값',
            'X-Naver-Client-Secret': '키값'
        }
    urlNaver=f"https://openapi.naver.com/v1/search/image?query={job}"
    result=requests.get(urlNaver,headers=naver_headers).json()
    image=result.get('items')[0].get('link')
    
    url=f"http://api.giphy.com/v1/gifs/search?api_key=키값&q={job}&limit=1&lang=ko"
    result=requests.get(url).json()
    gif=result.get('data')[0].get('images').get('original').get('url')
    contents={'name':name,'job':job,'gif':gif,'image':image}
    return render(request,'pl.html',contents)
```

*pastlife/models.py*

```python
from django.db import models

# Create your models here.
class Job(models.Model):
    name=models.TextField()
    job=models.TextField()
    
    def __repr__(self): # Job.objects.all() 일 때의 출력
        return f"{self.name}: {self.job}"
    def __str__(self):	# print()에 사용 될 때의 출력
        return f"<{self.name}: {self.job}>"
```

*bonbon/urls.py*

```python
from django.contrib import admin,include
from django.urls import path
from pastlife import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('pastlife/',views.pastlife),
    path('articles/',include('articles.urls')) # url 전달
]
```

*pastlife/templates/pastlife/index.html*

```html
{% extends 'base.html' %}

{% block body %}
<h1>전생앱</h1>
<p>전생을 알려드립니다.</p>
<form action='/pastlife/'>
    <input type="text" name="name"/>
    <input type="submit" value="Submit"/>
</form>
{% endblock %}
```



*pastlife/templates/pastlife/pl.html*

```html
{% extends 'base.html' %}

{% block body %}
<h1>{{ name }}님의 전생은 {{ job }}입니다.</h1>
{% endblock %}
```



*articles/views.py*

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



*articles/urls.py*

```python
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



*articles/model.py*

```python
from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.TextField()
    content=models.TextField()
    def __repr__(self):
        return f"<{self.id}번글, {self.title}: {self.content}>"
    def __str__(self):
        return f"<{self.title}: {self.content}>"
        
class Comment(models.Model):
    content=models.TextField()
    article=models.ForeignKey(Articles, on_delete=models.CASCADE, related_name="comments")
    def __repr__(self):
        return f"<{self.content}>"
```



*articles/templates/articles/detail.html*

```html
{% extends 'articles/base.html' %}

{% block body %}
<div class="jumbotron text-center">
  <h1 class="display-4">{{ article.title }}</h1>
  <p></p>
  <hr class="my-4">
  <div class='float-right'>
    <a class='btn btn-primary'role="button" href="{% url 'articles:index' %}">뒤로가기</a>
    <a class='btn btn-primary'role="button" href="{% url 'articles:edit' article.id %}">수정</a>
    <a class='btn btn-danger'role="button" href="{% url 'articles:delete' article.id %}">삭제</a> 
  </div>
</div>
<p>{{ content }}</p>
<hr>
<h3>댓글</h3>
<form action="/articles/{{ article.id }}/comment/" method="POST">
  {% csrf_token %}
  <input type="text" name="content"/>
  <input type="submit" value="Submit"/>
</form>
{% for comment in article.comments.all %}
  <p>{{ comment.content }}</p>
{% endfor  %}

{% endblock %}
```



*articles/templates/articles/edit.html*

```html
{% extends 'articles/base.html' %}

{% block body %}
<div class="jumbotron text-center">
  <h1 class="display-4">글 수정</h1>
  <p></p>
  <hr class="my-4">
</div>

<form action="/articles/{{ id }}/update/">
  <div class="form-group">
    <label>제목</label>
    <input type="text" class="form-control" name="title" value={{ title }} />
  </div>
  <div class="form-group">
    <label>내용</label>
    <textarea class="form-control" name="content" rows='5'>{{ content }}</textarea>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
{% endblock %}
```



*articles/templates/articles/index.html*

```html
{% extends 'articles/base.html' %}

{% block body %}
<div class="jumbotron text-center">
  <h1 class="display-4">게시판</h1>
  <hr class="my-4">
  <a class="btn btn-primary btn-lg float-right" href="{% url 'articles:new' %}" role="button">글쓰기</a>
</div>
<div class="list-group">
{% for i in data %}
<div>
    <a href="{% url 'articles:detail' i.id %}"class="list-group-item list-group-item-action">{{i.id}}  {{i.title}}</a>
</div>

{% endfor %}
</div>
{% endblock %}
```



*articles/templates/articles/new.html*

```html
{% extends 'articles/base.html' %}

{% block body %}
<div class="jumbotron text-center">
  <h1 class="display-4">글쓰기</h1>
  <p></p>
  <hr class="my-4">
</div>

<form action="{% 'articles:create' %}">
  <div class="form-group">
    <label>제목</label>
    <input type="text" class="form-control" name="title"/>
  </div>
  <div class="form-group">
    <label>내용</label>
    <textarea class="form-control" name="content" rows='5'></textarea>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>

{% endblock %}
```

settings.py의 TEMPLATES에서 'DIRS': [os.path.join(BASE_DIR, 'templates')] 를 입력하여 templates 경로를 설정할 수 있다. '공통 템플릿 폴더'