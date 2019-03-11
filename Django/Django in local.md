# 윈도우에서 Django 사용하기

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

