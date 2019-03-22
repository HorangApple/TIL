# validation (유효성 검증)

1. front-end

2. model(server-side)

3. DBMS

위 순서로 유효성 검증이 거쳐가는데 대부분 model까지 막아야한다.

```html
<input required type="text" name="title">
```

`required`를 입력하면 빈 칸 입력이 불가해진다. 그러나 개발자모드로 들어가서 이것을 지워지면 입력이 가능해진다.

그렇다고 `views.py`에서 if문을 일일이 사용하기엔 불편하다. 그래서 django에서 제공하는 클래스 form을 사용한다. 이 경우 1,2번이 해결이 된다.

basic CRUD -> Form -> ModelForm 으로 수정을 하여 검증을 강화시킨다.

https://docs.djangoproject.com/en/2.1/ref/forms/validation/

ModelForm은 data validation, input formation, data creation 작업을 해준다.

*shout/views.py*

```python
from django.shortcuts import render,redirect
from .models import Shout
from .forms import ShoutModelForm,ShoutForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
'''
def home(request):
    if request.method == "POST":
        # 고객센터 문의 작성하기
        form = ShoutModelForm(request.POST)
        if form.is_valid():
            # # ShoutForm 사용시
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # Shout.objects.create(title=title,content=content)
            form.save()
            
        # # 지금까지 한 방식
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        
        # # validation을 if문으로 한다면?
        # if title == "" and content =="":
        #     messages.success('마 내용입력해라 마')
        #     return redirect()
        # Shout.objects.create(title=title,content=content)
        return redirect('shouts:home')
        # 고객센터 문의 작성
    else:
        # form 보여주기 & 문의사항 전부 보여주기
        form = ShoutModelForm()
        shouts = Shout.objects.all()
        return render(request, 'shouts/home.html', {
            'shouts': shouts,
            'form': form,
        })
'''
# update와 중복되어 요약
def home(request):
    shouts = Shout.objects.all()
    context={
        'shouts': shouts,
    }
    return render(request,'shouts/home.html',context)

def update(request, id):
    shout = Shout.objects.get(pk=id)
    if request.method == "POST":
        # 수정하기(update)
        form = ShoutModelForm(request.POST, instance=shout)
        if form.is_valid():
            form.save()
            return redirect('shouts:home')
    else:
        # 편집하기(edit)
        form = ShoutModelForm(instance=shout)
        context = {
            'form': form,
        }
        return render(request, 'shouts/form.html', context)

def create(request):
    if request.method == "POST":
        # POST 글을 DB에 저장
        form = ShoutModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shouts:home')
    else:
        # GET 글 작성할 수 있는 form
        form = ShoutModelForm
        context = {
            'form': form,
        }
        return render(request, 'shouts/form.html', context)

def register(request):
    if request.method == "POST":
        # 회원가입 시키기(DB에 사용자 정보를 저장)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        # 회원정보를 받는 form 보여주기
        form = UserCreationForm()
        return render(request, 'shouts/register.html', {'form':form})
```

*shout/urls.py*

```python
from django.urls import path
from . import views
app_name="shouts"
# /shouts/XX
urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('<int:id>/update/', views.update, name="update"),
    path('register/',views.register,name="resigter")
]
```

*shout/models.py*

```python
from django.db import models

# Create your models here.
class Shout(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ": " + self.content
```

*shout/forms.py*

```python
from django import forms
from .models import Shout

class ShoutForm(forms.Form):
    title = forms.CharField(max_length=30)
    content = forms.CharField(max_length=100)


# model을 자동으로 form으로 만들어줌
class ShoutModelForm(forms.ModelForm):
    class Meta:
        model = Shout
        #fields = '__all__'  # 모든 필드
        fields = ['title','content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력해주세요',
                'value': '이건 내용이야'
            })
        }
```

*shout/templates/shouts/form.html*

```html
{% extends 'users/base.html' %}
{% block body %}
{#    {{ request.path }}#}
    {% if request.resolver_match.url_name == 'create' %}
        <h1>문의작성</h1>
    {% else %}
        <h1>수정하기</h1>
    {% endif %}
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock %}
```

*shout/templates/shouts/home.html*

```html
{% extends 'users/base.html' %}

{% block body %}
    <h1>고객센터</h1>
    <a href="{% url 'shouts:create' %}">문의하기</a>
    <hr>
    <h2>문의내용</h2>
    {% for shout in shouts %}
        <p>id: {{ shout.id }} 제목: {{ shout.title }} 내용: {{ shout.content }}</p>
        <a href="{% url 'shouts:update' shout.id %}">[수정]</a>
    {% endfor %}
{% endblock %}
```

*shout/templates/shouts/register.html*

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
```

