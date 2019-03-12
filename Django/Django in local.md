# 윈도우에서 Django 사용하기

## 190311 Article 생성

윈도우 환경에서 Django를 다루기 위해 PyCharm을 통해 Django 프로젝트를 생성한다.

Pycharm을 설치할 때 플러그 인으로 `.ignore`를 설치해준다.

<img src="images/image 014.png">

프로젝트를 생성하면 `templates`폴더가 있는데 이는 기존에 html을 담았던 그것과는 다르다. 사용을 안하니 삭제하고 git 버전관리를 하지 않기위해 프로젝트 최상단에 `.gitignore`를 만든다.

*.gitignore*

```
# 가상환경 파일/디렉토리
venv/

# Python auto generated cache
__pycache__/

# Jetbreain auto generated cache
.idea/

# Default django DB
*.sqlite3
```



`$ django-admin`는 `startapp`과 `startproject`를 실행할 때 사용한다고 생각한다

```bash
$ django-admin startapp board
$ pip install django-extensions ipython
```

pycharm에서 Shift 두 번 누르면 탐색 창이 나오는데 이를 통해 손쉽게 파일을 열 수 있다.

shift+enter는 커서가 어디있든 다음 줄로 행변환한다.

alt+ctrl+enter는 위로 행변환해준다.

ctrl+alt+r을 누르면 `python manage.py`를 생략해서 명령어를 작성해도 되는 명령 창이 열린다.

ctrl+g를 누르면 입력된 번호로 커서를 이동시켜준다.

<img src="images/image 015.png">

db도 볼 수 있는데 sqlite3를 download를 한 후 db.sqlite3를 드래그 해서 하면 된다.

여기서 `auth_user`는 유저관리를 할 수 있는 테이블인데 직접 여기서 수정을 하면 `python manage.py`를 통한 검증 과정을 생략하고 입력되기 때문에 좋지않다.

4xx 에러는 클라이언트 잘못, 5xx에러는 서버쪽 잘못이다. 구현되지 않은 페이지에 접속시 500에러가 뜨는데 이를 404로 바뀌기 위해서는 `get_object_or_404`를 사용해야한다.



*view.py*

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article,Comment
from IPython import embed
# Create your views here.
def article_list(request):
    articles=Article.objects.all()
    return render(request,'board/list.html',{
        'articles': articles,
    })

def article_detail(request,article_id):
    article=get_object_or_404(Article,id=article_id) # 없으면 404에러 출력
    comments = Comment.objects.all()
    return render(request,'board/detail.html',{
        'article': article,
        'comments': comments,
    })

# def new_article(request):
#     return render(request, 'board/new.html')

def create_article(request):
    # 같은 url이 두 개의 역할을 함, 
    if request.method=='GET':
        return render(request, 'board/new.html')
    else:
        article=Article()
        article.title=request.POST.get('title')
        article.content=request.POST.get('content')
        # embed() # 디버깅 할 때 사용 IPython
        article.save()
        return redirect('board:article_detail',article.id)

# def edit_article(request,article_id):
#     pass

def update_article(request,article_id):
    article=get_object_or_404(Article,id=article_id)
    if request.method=='GET':
        return render(request,'board/edit.html',{
            'article':article,
        })
    else:
        article=get_object_or_404(Article,id=article_id)
        article.title=request.POST.get('title')
        article.content=request.POST.get('content')
        article.save()
        return redirect('board:article_detail',article_id)

def delete_article(request,article_id):
    if request.method=='GET':
        return redirect('board:article_detail',article_id)
    else:
        article=get_object_or_404(Article,id=article_id)
        article.delete()
        return redirect('board:article_list')

def create_comment(request, article_id):
    if request.method=='POST':
        comment=Comment()
        # article_id를 굳이 적지 않아도 ORM이 알아서 해줌
        comment.article=get_object_or_404(Article,id=article_id)
        comment.content=request.POST.get('comment')
        comment.save()
    return redirect('board:article_detail',article_id)


def delete_comment(request, article_id,comment_id):
    article=get_object_or_404(Article,id=article_id)
    if request.method=='POST':
        comment=get_object_or_404(Comment,id=comment_id)
        comment.delete()
    return redirect('board:article_detail',article_id)
```

IPython의 embed()를 통해 view.py에서 코드 실행 중 멈춰서 그 시점에서 값을 살펴봐 디버깅을 할 수 있다.



*board/urls.py*

```python
from django.urls import path
from . import views

app_name='board'

urlpatterns=[
    path('',views.article_list,name='article_list'),  # list
    # path('new/',views.new_article,name='new_article'),  # new.html
    path('create/',views.create_article,name='create_article'),  # Create

    path('<int:article_id>/',views.article_detail,name='article_detail'),  # detail.html
    # path('<int:article_id>/edit',views.edit_article,name='edit_article'),  # edit.html
    path('<int:article_id>/update/',views.update_article,name='update_article'),  # Update
    path('<int:article_id>/delete/',views.delete_article,name='delete_article'),  # Destroy
    path('<int:article_id>/create_comment/',views.create_comment,name='create_comment'),
    path('<int:article_id>/delete_comment/<int:comment_id>/',views.delete_comment,name='delete_comment'),
]
```



*fisrt_local/url.py*

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
]

```



*board/models.py*

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.TextField(default='')
    content=models.TextField(default='')
    like=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}: {self.title[:20]}'

class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    content=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.article.title}:{self.content}'
```



*board/templates/board/detail.html*

```html
{% extends 'board/base.html' %}
{% block body %}
    <h1>{{ article.title }}</h1>
    <p>
        {{ article.content }}
    </p>
    <p>
        {{ article.like }}
    </p>
    <a href="{% url 'board:article_list' %}">
        <button>목록으로 가기</button>
    </a>
    <a href="{% url 'board:update_article' article.id %}">
        <button>수정하러 가기</button>
    </a>
    <form action="{% url 'board:delete_article' article.id %}" method='POST'>
        {% csrf_token %}
        <button type="submit">삭제하러 가기</button>
    </form>
    <hr>
{% include 'board/_comment.html' %}
{% endblock %}
```



*board/templates/board/_comment.html*

```html
<form action="{% url 'board:create_comment' article.id %}" method="POST">
    {% csrf_token %}
    <label for="comment">comment</label>
    <input type="text" name="comment" id="comment" autofocus>
</form>

{% if comments %}
    <ul>
        {% for comment in comments %}
            <li>{{ comment.content }}</li>
            <form action="{% url 'board:delete_comment' article_id=article.id comment_id=comment.id %}"
                method="POST">
                {% csrf_token %}
                <button type="submit">DEL</button>
            </form>
        {% endfor %}
    </ul>
{% endif %}
```

`_comment.html` 처럼 _로 시작하는 것은 부품으로 사용하겠다는 의미이다.



*board/templates/board/edit.html*

```html
{% extends 'board/base.html' %}
{% block body %}
<h1>New article</h1>

<form method="POST"> {#<action="{% url 'board:create_article' %}"는 생략됨 #}
    {% csrf_token %}
    <div>
        <label for="title">Title</label>
        <input type="text" name="title" id="title" value={{ article.title }}>
    </div>
    <div>
        <label for="content">Content</label>
        <textarea name="content" id="content" cols="30" rows="10">
            {{ article.content }}
        </textarea>
    </div>
    <div>
        <input type="submit">
    </div>
</form>
{% endblock %}
```



*board/templates/board/list.html*

```html
{% extends 'board/base.html' %}

{% block body %}
    {% if articles %}
    <ul>
        {% for article in articles %}
            <li>
                <a href="{% url 'board:article_detail' article.id %}">
                {{ article.title }}
                </a>
            </li>
        {% endfor %}
    </ul>
    {% endif %}
{% endblock %}
```



*board/templates/board/new.html*

```html
{% extends 'board/base.html' %}
{% block body %}
<h1>New article</h1>

<form method="POST"> {#<action="{% url 'board:create_article' %}"는 생략됨 #}
    {% csrf_token %}
    <div>
        <label for="title">Title</label>
        <input type="text" name="title" id="title">
    </div>
    <div>
        <label for="content">Content</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea>
    </div>
    <div>
        <input type="submit">
    </div>
</form>
{% endblock %}
```



*board/admin.py*

```python
from django.contrib import admin
from .models import Article,Comment
# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
```



## SNS 생성

*first_local/setting.py*

```python
...

# media files, 이미지를 저장할 디렉토리 설정
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
```



*sns/urls.py*

```python
from django.urls import path
from . import views

app_name = 'sns'

urlpatterns = [
    path('',views.posting_list, name='posting_list'),
    path('<int:posting_id>/',views.posting_detail,name='posting_detail'),
    path('create/',views.create_posting,name='create_posting'),

    path('<int:posting_id>/comment/create/', views.create_comment,name='create_comment'),
]
```



*sns/admin.py*

```python
from django.contrib import admin
from .models import Posting,Comment
# Register your models here.


class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','update_at') # 레코드 개별화면 확인
    list_display = ('id','content','created_at','update_at') # 리스트에서 표시할 컬럼
    list_display_links = ('id','content') # 리스트에서 clickable 할 속성

admin.site.register(Posting, PostingModelAdmin)

class CommentModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','update_at') # 레코드 개별화면 확인
    list_display = ('id','posting','content','created_at','update_at') # 리스트에서 표시할 컬럼
    list_display_links = ('id','content') # 리스트에서 clickable 할 속성

admin.site.register(Comment, CommentModelAdmin)
```



*sns/model.py*

```python
from django.db import models
# ImageKit
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.
class Posting(models.Model):
    content = models.TextField()
    icon = models.CharField(max_length=20, default='fas fa-question')
    # upload url (uniform resource location) => /media/posting/origin/20190312/
    # 필요없는 파일까지 다루지 않기 위해 디렉토리를 잘 구분시켜놔야한다.
    # DB에 이미지 주소만 저장이 된다.
    
    # 이미지 원본 저장
    # image = models.ImageField(blank=True, upload_to='posting/origin/%Y%m%d')

    # resize
    image=ProcessedImageField(
        upload_to= 'posting/resize/%Y%m%d',
        # ResizeToFit은 원본 비율로 크기를 늘리거나 작게 만든다.
        processors=[ResizeToFit(width=960, upscale=False)],
        format='JPEG'
    )

    # thumbnail, 이미지가 CACHE에 저장되어 있으나 보이지 않고 코드로 불러올 때 보임.
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(width=320, upscale=False)],
        format='JPEG',
        options={'quality': 60},
    )

    created_at = models.DateTimeField(auto_now_add=True, editable=False)  # 저장된 시점
    update_at = models.DateTimeField(auto_now=True)  # 저장 or 수정된 시점

    # 오버라이드
    def __str__(self):
        return  f'{self.id}: {self.content[:20]}'

    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        print()
        print(f'=== Saved Posting with id: {self.id}')
        print(f'    content: {self.content}')
        if self.image:
            print(f'    image_size: {self.image.width}px * {self.image.height}px: {round(self.image.size/1024)}kb')
        print('=====================================')
        print()

class Comment(models.Model):
    posting=models.ForeignKey(Posting, on_delete=models.CASCADE)
    content=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.posting.content[:10]}: {self.content[:20]}'
```

<img src="images/image 016.png">

오버라이드를 통해 위와 같이 사진을 저장하면 출력할 수 있겠끔 만들 수 있다.

`models.ImageField`를 사용하기 위해서는 `pip install pillow`를 설치해야한다.

`pip install django-imagekit` 를 설치하고 진행한다.



*sns/templates/sns/base.html*

```html
<!doctype html>
<html lang=ko>
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!--bootstrap-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <!--fontawesome icon-->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <title>My SNS</title>
</head>
<body>
<ul class="nav nav-tabs">
    <li class="nav-item">
        <a href="{% url 'sns:posting_list' %}" class="nav-link {% block is_list %}{% endblock %}">SNS</a>
    </li>
    <li class="nav-item">
        <a class="nav-link {% block is_detail %}{% endblock %}" aria-disabled="true" >Posting</a>
    </li>
</ul>
    <div class="container">
        {% block body %}
        {% endblock %}
    </div>
    <!--자바스크립트가 다 로드 되고 나서 cdn을 부른다.-->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```



*sns/templates/sns/list.html*

```html
{% extends 'sns/base.html' %}
{% block is_list %}active{% endblock %}
{% block body %}
{% include 'sns/_forms.html' %}
<hr>
{% if postings %}
    <section class="card-columns">
        {% for posting in postings %}
            <article class="card mb-2">
                <a href="{% url 'sns:posting_detail' posting.id %}">
                    {% if posting.image %}
                        <img src="{{ posting.image_thumbnail.url }}"
                             class="card-img-top image-fluid"
                             alt="{{ posting.image }}">
                    {% else %}
                        <img src="http://picsum.photos/32{{ forloop.counter }}/580/?random"
                             class="card-img-top image-fluid"
                             alt="random_image_{{ forloop.counter }}">
                    {% endif %}
                </a>
                <div class="card-body">
                    <i class="{{ posting.icon }} fa-2x"></i>
                </div>
            </article>
        {% endfor %}

    </section>
{% endif %}
{% endblock %}
```

`{{ forloop.counter }}`는 for문을 돈 횟수를 나타낸다.



*sns/templates/sns/_forms.html*

```html
<header class="mt-3">
    <form action="{% url 'sns:create_posting' %}" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <div class="form-row align-items center">
            <!-- icon select tag -->
            <div class="col-auto my-1">
                <label for="icon" class="sr-only">icon</label>
                <select name="icon" id="icon" class="custom-select mr-sm-2">
{#                    TODO: change icon value to FontAwesome icons#}
                    <option value="far fa-smile">:)</option>
                    <option value="far fa-angry">:(</option>
                    <option value="far fa-smile-wink">;)</option>
                    <option value="fas fa-question">?</option>
                    <option value="fab fa-angrycreative">AngryCreative</option>
                </select>
            </div>
            <!-- content input tag -->
            <div class="col-sm-6 my-1">
                <label for="content" class="sr-only">content</label>
                <input type="text" name="content" id="content" class="form-control" placeholder="Feels like..">
            </div>
            <!-- image/file input tag -->
            <div class="col-sm-4 my-1 input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text">
                        Upload
                    </span>
                </div>
                <div class="custom-file">
                    <input type="file" id="image" name="image" class="custom-file-input" accept="image/*">
                    <label for="image" class="custom-file-label">Choose image</label>
                </div>
            </div>

            <!-- submit button -->
            <div class="col-auto my-1">
                <button type="submit"class="btn btn-primary">submit</button>
            </div>
        </div>
    </form>
</header>
```

`.sr-only`는 bootstarp에서 온 것이며 screen read only로 숨겨주는 역할을 한다.

`input`의 `accept`는 파일 형식을 제한한다.

파일을 올리는 `form`을 구현할 때 항상 `enctype="multipart/form-data"`를 추가시켜야한다.



`python manage.py migrate sns zero` 는 sns와 관련된 db를 모두 날리는 명령어다. 이후 `python manage.py migrate`를 하여 다시 db를 생성한다.



*sns/templates/sns/detail.html*

```html	
{% extends 'sns/base.html' %}
{% block is_detail %}active{% endblock %}
{% block body %}
    <div class="row mt-3">
        <div class="col-12 col-md-6">
            <div class="card">
                {% if positin.image %}
                    <img src="{{ posting.image.url }}"
                         alt="{{ posting.image }}"
                         class="card-img-top image-fluid">
                {% else %}
                    <img src="http://picsum.photos/960/580/?random"
                         alt="random_image"
                         class="card-img-top image-fluid">
                {% endif %}
            </div>
            <div class="card-body">
                <i class="{{ posting.icon }} fa-3x"></i>
                <hr>
                <p class="card-text">
                    {{ posting.content }}
                </p>
            </div>
        </div>
    <div class="col-12 col-md-6">
        <div class="card mb-2">
            <div class="card-body">
                <form action="{% url 'sns:create_comment' posting.id %}" method="POST"}>
                    {% csrf_token %}
                    <label for="comment">Leave comment</label>
                    <input type="text" name="comment" id="comment" class="form-control" autofocus>
                </form>
            </div>
        </div>
        <div class="card">
            <ul class="list-group list-group-flush">
                {% if comments %}
                    {% for comment in comments %}
                        <li class="list-group-item mb-1">
                        {{ comment.content }}
                        </li>
                    {% endfor %}
                {% else %}
                    <li class="list-group-item mb-1">No comment yet..</li>
                {% endif %}
            </ul>
        </div>
    </div>

    </div>
{% endblock %}
```

