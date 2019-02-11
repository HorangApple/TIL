# Django

static web을 사용하다가 부족함에 dynamic web을 사용하게 되었다. flask는 경량형 프레임워크이기때문에 한계가 있기 때문에 Django를 사용한다.

프레임워크를 활용하여 웹서비스를 만드는 것은 마치 프렌차이즈를 이용해서 카페를 차리는 것과 같다. 기본적인 구조나 필요한 코드들은 프레임워크가 제공하니 좋은 웹 서비스를 만드는 것에 집중하면 된다.

Django의 기본 구조는 Model, Template, View로 데이터를 관리하는 Model, 사용자가 보는 화면인 Template, 중간 관리자인 View를 의미한다. 특히 View는 MVC 구조에서 Controller에 가까운 역할을 한다.

urls를 받아 해당하는 View가 받는다. 들어오는 모든 요청은 View가 관리하며 요청에 대한 수행을 Model에게 넘어가 수행한다. Model에게 받은 정보를 View가 받아 Template으로 넘겨 사용자가 원하는 정보를 담고 있는 html 파일을 보여준다.

<img src="images/image 001.png"/>

우선 View와 Template을 구현해보자. 



### pyenv - python 버전 관리 툴

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

해당하는 디렉터리에서 아래의 명령어로 python 가상환경을 만들고 진입한다. 여기서는 `intro`라는 폴더에서 진행했다.

```bash
$ pyenv virtualenv 3.6.7 intro-venv
$ pyenv local intro-venv
```



### Django 설치 및 설정

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

*settings.py*

```python
#...
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["django-horangapple.c9users.io"]

#...
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#...
```

위와 같이 c9의 `프로젝트 이름-계정.c9users.io`를 `ALLOWED_HOSTS`의 [] 안에 입력한다. 그리고 `LANGUAGE_CODE = 'en-us'`를 `ko-kr`로, `TIME_ZONE = 'UTC'`를 `Asia/Seoul`로 바꿔준다.

자주 건들게 되는 파일은 `urls.py`과 `settings.py`이다. `manage.py`는 script로 관리하는 파일이다.



### app 제작

이제는 app을 만들어보자.

```bash
$ python manage.py startapp pages
```

`pages`라는 app을 만들어보면 폴더 한 개가 생성된다.

<img src="images/image 003.png"/>

`apps.py`는 잘 안쓰이지만 view를 직접 다루는 `views.py`를 많이 다루게 된다.



*settings.py*

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
    'pages.apps.PagesConfig'
]
#...
```

app을 설치하게 되면 `settings.py`로 가서 `pages.apps.PagesConfig`를 입력한다. `pages.apps.PagesConfig`은 `pages/apps.py`에 있는 class `PagesConfig`을 지칭하는 것이며 pages app에 대한 정보를 제공한다.



*views.py*

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
<h1>쟝고 첫번째 앱</h1>
```

<img src="images/image 005.png"/>

*templates/lotto.html*

```html
<h1>{{ lucky }}</h1>
```

<img src="images/image 004.png"/>

*templates/hello.html*

```html
<h1>안녕! {{ name }}</h1>
```



<img src="images/image 005.png"/>

*urls.py*

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

